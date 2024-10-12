from dash import Dash, html, dcc, callback, Input, Output
import numpy as np 
import pandas as pd 
import plotly.express as px

#H1 is the header for writing
#app.title give the file a name otherwise they name defaultly

app = Dash(__name__)
app.title = "Assignment 3 Sufina"
server = app.server

#df = pd.read_csv("https://raw.githubusercontent.com/Sufilyas/MCM7183Exercise3/main/assets/gdp_1960_2020.csv")



image_path = 'assets/Multimedia_University_logo.png'


    return fig,fig2

if __name__ == '__main__':
    #dah ok baru remove debug tu
    app.run(debug=True)
