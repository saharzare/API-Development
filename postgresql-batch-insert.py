import pandas as pd
#extract data from website
import requests
#connect to database in python
import psycopg2

#Extract data from public API in json format
url='http://api.coincap.io/v2/assets'
header={'Content-Type':'application/json','Accept-Encoding':'deflate'}
response=requests.get(url,header)
data=response.json()['data']
df=pd.DataFrame(data)
df.head(5)

#connect to postgresql
connects=psycopg2.connect(dbname='postgres',
                          user='postgres',
                          password='sahar',
                          host='localhost',
                          port='5432')
cur=connects.cursor()
cur.execute(""" 
    CREATE TABLE IF NOT EXISTS CRYPTOTABLE (
        id SERIAL PRIMARY KEY, 
        rank INT, 
        symbol VARCHAR, 
        name VARCHAR, 
        marketCapUsd FLOAT,
        volumeUsd24Hr FLOAT, 
        priceUsd FLOAT, 
        changePercent24Hr FLOAT
    );
""")

INSERT_QUERY=""" 
INSERT INTO CRYPTOTABLE (rank,sym, name, marketCapUsd, volumeUsd24Hr, priceUsd, changePercent24Hr)
VALUES (%s, %s, %s, %s, %s, %s, %s);
"""
#INSERT DATA INTO TABLES
for index, row in df.iterrows():
    cur.execute(INSERT_QUERY, (int(row['rank']), row['name'], row['symbol'], float(row['marketCapUsd']),float(row['volumeUsd24Hr']), float(row['priceUsd']), row['changePercent24Hr']))

connects.commit()
cur.close()
connects.close()
print("the insertation finished sucessefully")
