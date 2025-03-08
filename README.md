# 1-ETL API for Data Pipeline
### Crypto Data Batch Insert (PostgreSQL)

#### 📌 Overview
This project automates the process of inserting cryptocurrency data into a **PostgreSQL database** using **Pandas** and **Psycopg2**. It ensures proper error handling and batch processing.

#### 🚀 Features
- Extracts cryptocurrency data from a Pandas DataFrame
- Inserts data into a PostgreSQL table (`CRYPTOTABLE`)
- Handles errors gracefully with rollback & retries
- Optimized for batch processing

#### 🛠️ Requirements
- Python 3.x
- PostgreSQL
- Pandas
- Psycopg2

#### ⚙️ Setup & Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/saharzare/crypto-data-insert-pgsql.git
   cd crypto-data-insert-pgsql

