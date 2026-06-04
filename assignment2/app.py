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
    html.Div(className = "child1", children = [
        html.H1("Stock Data Analysis"),
        html.Label("Select Month:"),
        dcc.Dropdown(
            id='month_dropdown_comp',
            options=[{'label': month, 'value': month} for month in stock_df['Month'].unique()],
            value=stock_df['Month'].unique()[0]
        )
    ]),
    html.Div(className = "child2", children = [
        html.Div(className = "bar_chart", children = [
            dcc.Graph(id='bar_chart_comp', style={'width': '100%'})
        ]),
        html.Div(className = "box_plot", children = [
            dcc.Graph(id='box_plot_comp', style={'width': '100%'})
        ])
    ]),
])

@app.callback(
    [Output('bar_chart_comp', 'figure'),
     Output('box_plot_comp', 'figure')],
    [Input('month_dropdown_comp', 'value')]
)

def update_charts(selected_month):
    filtered_df = stock_df[stock_df['Month'] == selected_month]
    
    bar_fig = px.bar(avg_open_by_company, x='Company', y='Open', title=f'Average Open Price by Company in {selected_month}')
    
    box_fig = px.box(filtered_df, x='Company', y='Close', title=f'Close Price Distribution by Company in {selected_month}')
    
    return bar_fig, box_fig

if __name__ == '__main__':
    app.run(debug=True)