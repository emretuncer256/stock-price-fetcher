# Stock Price Data Fetcher

This Python script fetches historical stock prices for a specific 
company within a specified date range. It utilizes the `yfinance` 
library to download the data and returns a pandas `DataFrame` containing 
the historical stock price data.

## Requirements <img src="https://pypi-camo.freetls.fastly.net/0618c2e453bcdee07417f23ffb7c37ccce0edbfb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d322e372c253230332e362b2d626c75652e7376673f7374796c653d666c6174">
To install requirements:
```shell
pip install yfinance pandas
```
The core packages are `pandas` and `yfinance`.
The [requirements.txt](./requirements.txt) file contains other packages downloaded along with `pandas` and `yfinance`.

#### or
To install requirements.txt packages:
```shell
pip install -r requirements.txt
```

## Usage
To use this script, you need to provide the following parameters:

1. [ ] `company (str)`: Company symbol (e.g., 'AAPL', 'GOOGL').

2. [ ] `start_date (str or date)`: Start date of the data range 
in the format `'YYYY-MM-DD'` or as a `date` object.

3. [ ] `end_date (str or date)`: End date of the data range in 
the format `'YYYY-MM-DD'` or as a `date` object.

4. [ ] `debug (bool, optional)`: If `True`, displays 
additional information including the number of rows, 
number of columns, elapsed time, and the company symbol. Defaults to `False`.

#### Example Usage
./demo/fetch_aapl_data.py
```python
from datetime import date
import pandas as pd
from data_fetcher import fetch_data

# Fetch data for AAPL from January 1, 2016, to December 30, 2023, with debug information.
data = fetch_data('AAPL', date(2016, 1, 1), date(2023, 12, 30), debug=True)

# Check if data is not None before further processing.
if data is not None:
    data.to_csv('AAPL.csv')
    print("Data fetched and saved to AAPL.csv.")
else:
    print("Failed to fetch data.")
```

Note: Make sure you have the pandas and yfinance libraries installed before running the script.

Please adjust the parameters according to your requirements and run the script to fetch and save the historical stock price data.

#### License
This script is licensed under the MIT License. For more information about the MIT License, please read: [LICENSE](./LICENSE) or visit: [MIT License](https://opensource.org/license/mit/)

