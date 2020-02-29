import pandas as pd
from xbbg import blp
import plotly.graph_objects as go


class Title:
    tick = None
    ref_data = None
    histo_data = None

    # Constructors
    def __init__(self, args):
        if len(args) == 2:
            self.init_ref(args[0], args[1])
        else:
            self.init_histo(args[0], args[1], args[2], args[3])

    # Reference data constructor
    def init_ref(self, ticker, fields):
        self.tick = ticker
        self.ref_data = blp.bdp(tickers=ticker, flds=fields)

    # Historical data constructor
    def init_histo(self, ticker, fields, startdate, enddate):
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

    # Accessor
    def get_data(self):
        try:
            return self.histo_data
        except NameError:
            try:
                return self.ref_data
            except NameError:
                print("An error occurred, Trying to access non initialized member in Title class")
