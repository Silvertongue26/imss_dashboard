"""
IMPORTS BEGINS
"""
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os.path
import gunicorn

import dash_bootstrap_components as dbc
import dash
from dash import Input, Output, State, html, dcc


"""
IMPORTS END
"""

app = dash.Dash(
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "/assets/css/layout.css"
    ],
    #assets_external_path = "/assets/css/layout.css",
    #external_scripts = []
)

server = app.server
print("pandas: "+pd.__version__)
#print("plotly: "+px.__version__)
app.layout = html.Div([
        html.P("WASABI")

    ])



if __name__ == '__main__':
    app.run_server(debug=True)


