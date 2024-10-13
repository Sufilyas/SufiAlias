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
fig2 = px.line(top_artists, x='Artist', y='Track Score', title='Track Score Over Time')
fig3 = px.pie(top_artists, names='Artist', values='Track Score', title='Track Score Distribution')

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
            children=[html.H1('Most Streamed Spotify Songs 2024')],
            style={
                'textAlign': 'center',  # Center the title text
                'marginBottom': '30px',  # Space between title and text
                'color': 'white'
            }
        ),
        
        # Text below the title
        html.Div(
            children=[html.P('This is the data of top songs listened to on Spotify for 2024')],
            style={
                'textAlign': 'center',  # Center the text
                'color': 'white',
                'fontSize': '20px',  # Adjusted font size
                'marginBottom': '40px',  # Space between text and tabs
            }
        ),
        
        # Tabs for charts
        dcc.Tabs([
            dcc.Tab(label='Bar Chart', children=[
                dcc.Graph(figure=fig1)  # First tab with bar chart
            ]),
            dcc.Tab(label='Line Graph', children=[
                dcc.Graph(figure=fig2)  # Second tab with line plot
            ]),
            dcc.Tab(label='Pie Chart', children=[
                dcc.Graph(figure=fig3)  # Third tab with pie chart
            ])
        ])  
    ]  
)

# Running the app in debug mode when executed directly
if __name__ == '__main__':
    app.run(debug=True)
