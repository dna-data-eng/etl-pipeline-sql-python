# etl-pipeline-sql-python

Goal: clean stock price data and load it into  Oracle.


## Data source

This project uses the TidyTuesday big tech stock prices dataset, week of 2023-02-07.

* Contents: daily prices and volume for large tech companies.
* Columns: stock_symbol, date, open, high, low, close, adj_close, volume.
* Time range: starts on 2010-01-04. Confirm the last date in the pipeline, not here.
* adj_close is the close adjusted for splits and dividends. Use it for return calculations.

The raw file is not stored in this repo. Download it into data/raw/ with:

wget -O data/raw/big_tech_stock_prices.csv https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2023/2023-02-07/big_tech_stock_prices.csv


