from title import *


bucket = {}

# Get inputs
tickers = input("Enter titles: ('/' as sep)").split("/")
fields = input("Enter fields:").split(" ")
dates = input("Enter desired dates (yyyy-mm-dd):").split(" ")

# Main
# If nothing is specified launch the example
if len(tickers) == 0 or len(fields) == 0 or len(dates) == 0:
    print("Invalid entries. Example will be displayed ")
    bloom_feed = Title('SPX Index', ['open', 'high', 'low', 'last_price'], '2020-01-01', '2020-01-31')
    bloom_feed.display_candle()

else:
    # Fill dictionnary
    if len(dates) > 2:
        print("Incorrect number of arguments for field dates")
    else:
        for i in range(len(tickers)):
            # Check if ref or histo
            if len(dates) < 2:
                bucket[tickers[i]] = Title(tickers[i], fields)
            elif len(dates) == 2:
                bucket[tickers[i]] = Title(tickers[i], fields, dates[0], dates[1])

# Menu
# To be continued...
