# etl-pipeline-sql-python

Goal: clean stock price data and load it into Oracle.

## Data source

This project uses the TidyTuesday big tech stock prices dataset, week of 2023-02-07.

Source: https://github.com/rfordatascience/tidytuesday

* Contents: daily prices and trading volume for 14 large tech companies
* Symbols: AAPL, ADBE, AMZN, CRM, CSCO, GOOGL, IBM, INTC, META, MSFT, NFLX, NVDA, ORCL, TSLA
* Date range: 2010-01-04 to 2023-01-24
* Rows: 45,088
* Columns: stock_symbol, date, open, high, low, close, adj_close, volume
* adj_close: the close adjusted for splits and dividends. Use it for return calculations.

The raw file is not stored in this repo. Download it into data/raw/ with:

wget -O data/raw/big_tech_stock_prices.csv https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2023/2023-02-07/big_tech_stock_prices.csv

## Checks on the raw data

Checked before transform:

* No missing values in any column
* No exact duplicate rows

To be checked and recorded here: duplicate (stock_symbol, date) pairs, low and high consistent with open and close, and negative volume.

## Project status

Done:

* extract.py reads the CSV, checks that the required columns exist, and reports the row count and symbols

To do:

* Record the remaining raw-data checks above
* transform.py: convert dates, remove duplicates, check price rules
* schema/create_stock_prices.sql: the target table
* load.py: MERGE into Oracle
* verify.py and a rerun test

## How to run

source ~/venvs/etl/bin/activate
python3 src/extract.py


