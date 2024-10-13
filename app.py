from dash import Dash, html, dcc, callback, Input, Output
import numpy as np 
import pandas as pd 
import plotly.express as px

app = Dash(__name__)
server = app.server
app.title = "Assignment 3 Sufina"

df = pd.read_csv("https://raw.githubusercontent.com/Sufilyas/SufiAlias/main/assets/Most_Streamed_Spotify_Songs_2024.csv", encoding='ISO-8859-1')

image_path = 'assets/Multimedia_University_logo.png'

app.layout = html.Div(
    style=
 {
        'fontFamily': 'Arial, sans-serif',  # Change to your preferred font
        'fontSize': '20px',  # Font size
        'color': 'white',  # Text color
        'backgroundImage': 'url("assets/Tired_Happy.png")',
        'backgroundSize': 'cover',
        'height': '100vh',
        'width': '100vw',
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center', #alignment dia kat center
        'justifyContent': 'flex-start', # text start from above, if want in mid put center
        'padding': '20px', #spacing from the edge and word
        'border': 'none', #make sure no border
        'margin': '0' #to remove margin
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
