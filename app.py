from dash import Dash, html, dcc
import numpy as np 
import pandas as pd 
import plotly.express as px

app = Dash(__name__)
server = app.server
app.title = "Final Project"

# Read the data
df = pd.read_csv("https://raw.githubusercontent.com/Sufilyas/SufiAlias/main/assets/Most_Streamed_Spotify_Songs_2024.csv", encoding='ISO-8859-1')

# Calculate average track scores for each artist
artist_scores = df.groupby('Artist', as_index=False)['Track Score'].mean()
top_artists = artist_scores.nlargest(10, 'Track Score')

# Create the figures for each tab
fig1 = px.bar(top_artists, x='Artist', y='Track Score', title='Top Artists by Track Score', color='Artist')
fig2 = px.line(top_artists, x='Artist', y='Track Score', title='Track Score Over Time', color='Artist')
fig3 = px.pie(top_artists, names='Artist', values='Track Score', title='Track Score Distribution')

app.layout = html.Div(
    style={
        'fontFamily': 'Arial, sans-serif',
        'fontSize': '40px',
        'color': 'white',
        'backgroundImage': 'url("assets/music.jpg")',
        'backgroundSize': 'cover',
        'backgroundPosition': 'center',  
        'backgroundRepeat': 'no-repeat',
        'height': '100vh',
        'width': '100vw',
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'flex-start',
        'justifyContent': 'flex-start',
        'padding': '0',  
        'margin': '0' 
    },
    children=[
        html.H1('Most Streamed Spotify Songs 2024'),
        dcc.Tabs([
            dcc.Tab(label='Bar Chart', children=[
                html.Div(style={
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'height': '50vh',
                    'width': '100%'  # Set to 100% for proper alignment
                }, children=[
                    dcc.Graph(figure=fig1)
                ])
            ]),
            dcc.Tab(label='Line Chart', children=[
                html.Div(style={
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'height': '50vh',
                    'width': '100%'  # Set to 100% for proper alignment
                }, children=[
                    dcc.Graph(figure=fig2)
                ])
            ]),
            dcc.Tab(label='Pie Chart', children=[
                html.Div(style={
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'height': '50vh',
                    'width': '100%'  # Set to 100% for proper alignment
                }, children=[
                    dcc.Graph(figure=fig3)
                ])
            ])
        ])
    ]
)

# Running the app in debug mode when executed directly
if __name__ == '__main__':
    app.run(debug=True)
