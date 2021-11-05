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

#Instruction for gunicorn to detect server
server = app.server


"""
NAVIGATION BARS - BEGINS
"""
gob_logo = "https://raw.githubusercontent.com/Silvertongue26/imss_dashboard/7cf1c60afaf78a9385dce9264855983fba9d1574/assets/imgs/logoheader.svg"
gob_bar = dbc.Row(
    [
        dbc.Row(style={"width": "100%", "marginTop":"5px"}, children=[
            dbc.Col(html.A("Trámites", href="https://www.gob.mx/tramites",
                           className="a-text-navbar",
                           ),
                    className=" d-xl-none d-ls-none d-md-none d-sm-block col-sm-12 col-navbar-light",
                    style={"textAlign": "center"},
                    ),
            dbc.Col(html.A("Gobierno", href="https://www.gob.mx/gobierno",
                           className="a-text-navbar",
                           ),
                    className=" d-xl-none d-ls-none d-md-none d-sm-block col-sm-12 col-navbar-light",
                    ),
        ]),
    ],
    className="g-0 ",
    align="center",
)
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(style={"width": "100%"}, children=[
                dbc.Col(html.Img(src=gob_logo, height="50px", ),
                        className="col-xl-9 col-lg-9 col-md-9 col-sm-9 ",
                        style={"float": "left"}
                        ),
                dbc.Col(html.A("Trámites", href="https://www.gob.mx/tramites",
                               className="a-text-navbar",
                               ),
                        className="d-none d-xl-block d-ls-block d-md-block d-sm-none col-xl-2 col-lg-2 col-md-2 col-sm-3 col-navbar",
                        style={"textAlign": "right"},
                        ),
                dbc.Col(html.A("Gobierno", href="https://www.gob.mx/gobierno",
                               className="a-text-navbar",
                               ),
                        className="d-none d-xl-block d-ls-block d-md-block d-sm-none col-xl-1 col-lg-1 col-md-1 col-sm-3 col-navbar",
                        ),
                dbc.Col(dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        className=" d-lg-none d-md-none col-sm-3  col-navbar",
                        style={'textAlign': "right"}
                        ),
            ]),
            dbc.Collapse(
                gob_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="#0C231E",
    dark=True,
)

sub_bar = dbc.Row(
    [
        dbc.Row(style={"width": "100%", "marginTop":"5px"}, children=[
            dbc.Col(html.A("Trámites", href="https://www.gob.mx/tramites",
                           className="a-text-navbar",
                           ),
                    className=" d-xl-none d-ls-none d-md-none d-sm-block col-sm-12 col-navbar-light",
                    style={"textAlign": "center"},
                    ),
            dbc.Col(html.A("Gobierno", href="https://www.gob.mx/gobierno",
                           className="a-text-navbar",
                           ),
                    className=" d-xl-none d-ls-none d-md-none d-sm-block col-sm-12 col-navbar-light",
                    ),
        ]),
    ],
    className="g-0 ",
    align="center",
)
sub_navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(style={"width": "100%"}, children=[
                dbc.Col(html.A("Plataformas IMSS", href="http://11.254.36.175/",
                               className="a-text-navbar",
                               target="_blank"
                               ),
                        className="offset-xl-9 offset-lg-9 offset-md-9 offset-sm-9 d-none d-xl-block d-ls-block d-md-block d-sm-none col-xl-3 col-lg-3 col-md-3 col-sm-3 col-navbar",
                        style={"textAlign":"right"},
                        ),
                dbc.Col(dbc.NavbarToggler(id="subnavbar-toggler", n_clicks=0),
                        className=" d-lg-none d-md-none offset-sm-9 col-sm-3  col-navbar",
                        style={'textAlign': "right"}
                        ),
            ]),
            dbc.Collapse(
                sub_bar,
                id="subnavbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="#285C4D",
    dark=True,
)
"""
NAVIGATION BARS - END
"""





#Main structure of the page
app.layout = html.Div([
    navbar,
    sub_navbar,

])

"""
NAVBAR FUNCTIONS - BEGINS
"""
# Add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# Add callback for toggling the collapse on small screens
@app.callback(
    Output("subnavbar-collapse", "is_open"),
    [Input("subnavbar-toggler", "n_clicks")],
    [State("subnavbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
"""
NAVBAR FUNCTIONS - ENDS
"""


if __name__ == '__main__':
    app.run_server(debug=True)


