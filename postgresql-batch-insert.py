import pandas as pd
# extract data from website
import requests
# connect to database in python
import psycopg2

# Extract data from public API in JSON format
url = 'http://api.coincap.io/v2/assets'
header = {'Content-Type': 'application/json', 'Accept-Encoding': 'deflate'}
response = requests.get(url, header)
data = response.json()['data']
df = pd.DataFrame(data)
df.head(5)

# Connect to PostgreSQL
connects = psycopg2.connect(dbname='postgres',
                             user='postgres',
                             password='xxxx',
                             host='localhost',
                             port='5432')
cur = connects.cursor()

# Create the table if it doesn't exist
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

# Prepare the INSERT query
INSERT_QUERY = """ 
INSERT INTO CRYPTOTABLE (rank, symbol, name, marketCapUsd, volumeUsd24Hr, priceUsd, changePercent24Hr)
VALUES (%s, %s, %s, %s, %s, %s, %s);
"""

# Begin transaction and insert data into table with error handling
try:
    # Start a transaction block
    for index, row in df.iterrows():
        cur.execute(INSERT_QUERY, (
            int(row['rank']),
            row['symbol'],
            row['name'],
            float(row['marketCapUsd']),
            float(row['volumeUsd24Hr']),
            float(row['priceUsd']),
            row['changePercent24Hr']
        ))

    # Commit the transaction if all goes well
    connects.commit()
    print("Insertion finished successfully")

except Exception as e:
    # If an error occurs, rollback the transaction
    connects.rollback()
    print(f"Error occurred: {e}")
    print("Transaction rolled back.")

finally:
    # Close the cursor and connection
    cur.close()
    connects.close()
