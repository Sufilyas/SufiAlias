from dash import Dash, html, dcc, callback, Input, Output
import numpy as np 
import pandas as pd 
import plotly.express as px

# Initialize the Dash app
app = Dash(__name__)
app.title = "Assignment 3 Sufina"
server = app.server  # Exposing the server to Gunicorn

# Add some layout or content (example with a header)
app.layout = html.Div([
    html.H1("Welcome to Assignment 3"),
    dcc.Graph(id='graph')
])

# Optional: Example of a simple callback to update a graph
# @app.callback(
#     Output('graph', 'figure'),
#     Input('graph', 'id')
# )
# def update_graph(_):
#     df = pd.DataFrame({
#         'Category': ['A', 'B', 'C'],
#         'Values': [10, 20, 30]
#     })
#     fig = px.bar(df, x='Category', y='Values')
#     return fig

# Running the app in debug mode when executed directly
if __name__ == '__main__':
    app.run(debug=True)
