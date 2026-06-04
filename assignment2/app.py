from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os

app = Dash(__name__)

stock_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'StockData.csv')).dropna()

#extracting data
avg_open_by_company = stock_df.groupby('Company')['Open'].mean().reset_index()
avg_close_by_company = stock_df.groupby('Company')['Close'].mean().reset_index()
avg_high_by_company = stock_df.groupby('Company')['High'].mean().reset_index()
avg_low_by_company = stock_df.groupby('Company')['Low'].mean().reset_index()

app.layout = html.Div(className = "parent", children = [
    dcc.Dropdown(
            id='month_dropdown_comp',
            options=stock_df['Month'].unique(),
            value=stock_df['Month'].unique()[0],
            clearable=False,
            style={'width': '50%'}
        ),
    html.Div(className = "child1", children = [
        dcc.Graph(id='bar_chart_comp', style={'width': '100%'})
    ]),
    html.Div(className = "child2", children = [
        dcc.Graph(id='box_plot_comp', style={'width': '100%'})
    ])
])
if __name__ == '__main__':
    app.run(debug=True)