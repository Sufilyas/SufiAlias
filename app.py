from dash import Dash, html, dcc, callback, Input, Output
import numpy as np 
import pandas as pd 
import plotly.express as px

app = Dash(__name__)
server = app.server
app.title = "Assignment 3 Sufina"

#df = pd.read_csv("https://raw.githubusercontent.com/Sufilyas/MCM7183Exercise3/main/assets/gdp_1960_2020.csv")

image_path = 'assets/Multimedia_University_logo.png'

app.layout = html.Div(
    style=
    {
        'backgroundImage': 'url("assets/Tired_Happy.png")',  # Change to your background image path
        'backgroundSize': 'cover',  # Ensures the image covers the entire area
        'height': '100vh',  # Full height of the viewport
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',  # Center horizontally
        'justifyContent': 'flex-start',  # Align items at the top
        'color': 'white',  # Optional: Change text color for better visibility
        'padding': '20px'  # Optional: Add some padding for spacing(bg x melekat terus kat atas)
        'border': 'none',  # Ensure no border
        'margin': '0'  # Remove margin
    },
    children=
    [
        html.H1('Assignment 3'),  # Main header
        html.Img(src=image_path),  # Image displayed in the app
        html.Div(id='debug'),  # Placeholder for any debug information or updates
        #dcc.Graph(id='example-graph')  # Placeholder for a Plotly graph
    ]
)

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
