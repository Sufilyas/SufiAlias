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
fig1 = px.bar(top_artists, x='Artist', y='Track Score', title='Top 5 Artists by Track Score', color='Artist')
fig2 = px.line(top_artists, x='Artist', y='Track Score', title='Track Score Over Time')
fig3 = px.pie(top_artists, values='Track Score', names='Artist', title='Top 10 Artist Track Score')

app.layout = html.Div(
    style={
        'fontFamily': 'Arial, sans-serif',
        'fontSize': '30px',  # Adjusted font size for better fit
        'color': 'white',
        'backgroundImage': 'url("assets/music.jpg")',
        'backgroundSize': 'cover',
        'backgroundPosition': 'center',
        'height': '100vh',
        'width': '100vw',
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'justifyContent': 'flex-start',  # Keep title at the top
        'padding': '10px',
        'margin': '0'
    },
    children=[
        # Title
        html.Div(
            children=[
                html.H1('Most Streamed Spotify Songs 2024'),
            ],
            style={
                'textAlign': 'center',  # Center the title text
                'marginBottom': '20px',  # Space between title and text
                'color': 'white'
            }
        ),
        
        # Text below the title
        html.Div(
            children=[
                html.P('This dashboard presents data on the top streamed songs on Spotify for the year 2024. '
                       'Explore the charts to see the top artists and their track scores.'),
            ],
            style={
                'textAlign': 'center',  # Center the text
                'color': 'white',
                'fontSize': '18px',  # Adjusted font size
                'marginBottom': '40px',  # Space between text and tabs
            }
        ),
        
        # Tabs for switching between graphs
        dcc.Tabs(
            id="graph-tabs",
            value='tab-bar',  # Default tab
            children=[
                dcc.Tab(label='Top 5 Artists (Bar Chart)', value='tab-bar'),
                dcc.Tab(label='Track Score Over Time (Line Chart)', value='tab-line'),
                dcc.Tab(label='Top 10 Artists (Pie Chart)', value='tab-pie'),
            ],
            style={'width': '80%', 'margin': '0 auto'}  # Style to center tabs
        ),
        
        # Graph below the tabs
        html.Div(id='graph-content')  # This will hold the graphs based on the selected tab
    ]
)

# Callback to update graph based on selected tab
@app.callback(
    dcc.Output('graph-content', 'children'),
    [dcc.Input('graph-tabs', 'value')]
)
def render_content(tab):
    if tab == 'tab-bar':
        return dcc.Graph(id='bar-chart', figure=fig1)
    elif tab == 'tab-line':
        return dcc.Graph(id='line-chart', figure=fig2)
    elif tab == 'tab-pie':
        return dcc.Graph(id='pie-chart', figure=fig3)

# Running the app in debug mode when executed directly
if __name__ == '__main__':
    app.run(debug=True)
