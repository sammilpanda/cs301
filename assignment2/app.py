from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os

app = Dash(__name__)

stock_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'StockData.csv')).dropna()

if __name__ == '__main__':
    app.run(debug=True)