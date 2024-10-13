from dash import Dash, html, dcc
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
        'color': 'white',
        'backgroundImage': 'url("assets/music.jpg")',
        'backgroundSize': 'cover',
        'backgroundPosition': 'center',
        'height': '100vh',
        'width': '100vw',
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'flex-start',  # Aligns children to the start
        'padding': '20px',  # Add some padding
        'margin': '0'
    },
    children=[
        html.H1('Most Streamed Spotify Songs 2024', style={'alignSelf': 'flex-start', 'marginBottom': '20px'}),  # Title at top left
        dcc.Tabs(
            style={'backgroundColor': 'grey'},  # Default tab background color
            children=[
                dcc.Tab(
                    label='Bar Chart',
                    style={'color': 'white', 'backgroundColor': 'grey'},  # Default tab color
                    selected_style={'backgroundColor': 'lightgrey', 'color': 'black'},  # Selected tab color
                    children=[
                        html.Div(style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'height': '80vh',  # Height for the graph container
                            'width': '100%'  # Set to 100% for full width, or adjust to e.g., '80%'
                        }, children=[
                            dcc.Graph(figure=fig1, style={'height': '100%', 'width': '100%'})  # Set graph height and width to fill container
                        ])
                    ]
                ),
                dcc.Tab(
                    label='Line Chart',
                    style={'color': 'white', 'backgroundColor': 'grey'},  # Default tab color
                    selected_style={'backgroundColor': 'lightgrey', 'color': 'black'},  # Selected tab color
                    children=[
                        html.Div(style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'height': '80vh',  # Height for the graph container
                            'width': '100%'  # Set to 100% for full width, or adjust to e.g., '80%'
                        }, children=[
                            dcc.Graph(figure=fig2, style={'height': '100%', 'width': '100%'})  # Set graph height and width to fill container
                        ])
                    ]
                ),
                dcc.Tab(
                    label='Pie Chart',
                    style={'color': 'white', 'backgroundColor': 'grey'},  # Default tab color
                    selected_style={'backgroundColor': 'lightgrey', 'color': 'black'},  # Selected tab color
                    children=[
                        html.Div(style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'height': '80vh',  # Height for the graph container
                            'width': '100%'  # Set to 100% for full width, or adjust to e.g., '80%'
                        }, children=[
                            dcc.Graph(figure=fig3, style={'height': '100%', 'width': '100%'})  # Set graph height and width to fill container
                        ])
                    ]
                )
            ]
        )
    ]
)

# Running the app in debug mode when executed directly
if __name__ == '__main__':
    app.run(debug=True)
