from datetime import date

from data_fetcher import fetch_data

# Fetch data for AAPL from January 1, 2016, to December 30, 2023, with debug information.
data = fetch_data('AAPL', date(2016, 1, 1), date(2023, 12, 30), debug=True)

# Check if data is not None before further processing.
if data is not None:
    data.to_csv('AAPL.csv')
    print("Data fetched and saved to AAPL.csv.")
else:
    print("Failed to fetch data.")
