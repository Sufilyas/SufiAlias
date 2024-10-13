from dash import Dash, html, dcc, callback, Input, Output
import numpy as np 
import pandas as pd 
import plotly.express as px

app = Dash(__name__)
server = app.server
app.title = "Final Project"

df = pd.read_csv("https://raw.githubusercontent.com/Sufilyas/SufiAlias/main/assets/Most_Streamed_Spotify_Songs_2024.csv", encoding='ISO-8859-1')

# Calculate average track scores for each artist
artist_scores = df.groupby('Artist', as_index=False)['Track Score'].mean()
top_artists = artist_scores.nlargest(10, 'Track Score')

app.layout = html.Div(
    style=
 {
        'fontFamily': 'Arial, sans-serif',  # Change to your preferred font
        'fontSize': '40px',  # Font size
        'color': 'white',  # Text color
        'backgroundImage': 'url("assets/music.jpg")',
        'backgroundSize': 'cover',
        'height': '100vh',
        'width': '100vw',
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'flex-start', #alignment dia  flex-start/center/flex-end
        'justifyContent': 'flex-start', # text start from above, if want in mid put center
        'padding': '20px', #spacing from the edge and word
        'border': 'none', #make sure no border
        'margin': '0' #to remove margin
    },
    children=
    [
        html.H1('Most Stream Spotify Songs 2024'),  # Main header
       # html.Img(src=image_path),  # Image displayed in the app
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
