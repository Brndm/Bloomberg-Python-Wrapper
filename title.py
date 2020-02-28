import pandas as pd
from xbbg import blp
import plotly.graph_objects as go


class Title:
    tick = ''
    histo_data = pd.DataFrame()

    # Constructors
    # Reference data constructor
    def __init__(self, ticker, fields):
        self.tick = ticker
        self.histo_data = blp.bdp(tickers=ticker, flds=fields)

    # Historical data constructor
    def __init__(self, ticker, fields, startdate, enddate):
        self.tick = ticker
        self.histo_data = blp.bdh(tickers=ticker, flds=fields, start_date=startdate, end_date=enddate)

    # Methods
    def display_candle(self):
        df = pd.DataFrame(self.histo_data.values, columns=['open', 'high', 'low', 'last_price'])
        df['Date'] = self.histo_data.axes[0]
        fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['open'], high=df['high'], low=df['low'],
                                             close=df['last_price'])])
        fig.update_layout(title=self.tick, xaxis_rangeslider_visible=False)  # Remove to add range slider
        fig.show()

    # BDS
    # Intraday bars
    # Corporate earnings
    # write to excel
