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
        "https://raw.githubusercontent.com/Silvertongue26/imss_dashboard/main/assets/css/layout.css"
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
            dbc.Col(html.A("Plataformas IMSS", href="http://11.254.36.175/",
                               className="a-text-navbar",
                               target="_blank"
                               ),
                    className=" d-xl-none d-ls-none d-md-none d-sm-block col-sm-12 col-navbar-light",
                    style={"textAlign": "center"},
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
"""
GRAPH 1 - DATA MANIPULATION BEGINS
"""
#Data cleaning for graph 1
df_vacc_mex = pd.read_csv("https://raw.githubusercontent.com/Silvertongue26/imss_dashboard/main/data/graph1_vaccinated_mx.csv")
df_vacc_mex.pop('location')
df_vacc_mex.pop('vaccine')
#df_vacc_mex.pop('people_vaccinated')
#df_vacc_mex.pop('people_fully_vaccinated')
df_vacc_mex.pop('total_vaccinations')
df_vacc_mex.pop('total_boosters')
df_vacc_mex.pop('source_url')


#Create object
fig = go.Figure()

fig.add_trace(go.Scatter(x=list(df_vacc_mex.date), y=list(df_vacc_mex.people_vaccinated),
                         mode='lines',
                         name='Total de vacunados'
                         ))
fig.add_trace(go.Scatter(x=list(df_vacc_mex.date), y=list(df_vacc_mex.people_fully_vaccinated),
                         mode='lines',
                         name='Esquemas completos'
                         ))
#fig.add_trace(go.Scatter(x=list(df_vacc_mex.date), y=list(df_vacc_mex.total_vaccinations),
                         #mode='lines',
                         #name='Total de vacunas'))


# Set plot laypout options
fig.update_layout(
    legend=dict(
        # title_text="Avance de vacunación en México"
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ),
    # Add range slider
    xaxis=dict(
        rangeselector = dict(
            buttons = list([
                dict(
                    count = 1,
                    label = "Último mes",
                    step = "month",
                    stepmode = "backward"
                ),
                dict(
                    count = 6,
                    label = "Últimos 6 meses",
                    step = "month",
                    stepmode = "backward"
                ),
                dict(count=1,
                     label = "Último año",
                     step = "year",
                     stepmode = "backward"
                ),
                dict(
                    count = 1,
                    label = "Todo",
                    step = "all"
                )
            ])
        ),
        rangeslider = dict(visible=True),
        type = "date"
    ),
    hovermode='x'
)

"""
GRAPH 1 - DATA MANIPULATION ENDS
"""




"""
BODY - BEGINS
"""
body = dbc.Container([
        dbc.Row([
            dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            html.H1("Informe de vacunación en México")
                        ], className='col-xl-12 col-lg-12 col-md-12 col-sm-12',
                        style={"marginTop": "5%"}),
                        dbc.Col([
                            html.P(["En esta entrega resumo la información disponible al 9 de octubre de 2021 "
                                   "correspondiente al fin de la semana epidemiológica 40— sobre el avance en "
                                   "la aplicación de vacunas contra covid-19 en México. Como he mencionado en "
                                   "actualizaciones anteriores, al no existir una base de datos abierta con "
                                   "registros de vacunación, este análisis se basa en información presentada por "
                                   "personal de la Secretaría de Salud federal en conferencias de prensa o en sus "
                                   "redes sociales. Ante la imposibilidad de verificar datos, se acepta la información "
                                   "presentada por las autoridades sanitarias como cierta, y cuando una cifra publicada "
                                   "es distinta a otra presentada con anterioridad, se toma como buena la cifra más reciente."],
                                   style={"fontSize":"1.2em", 'textAlign': "justify"})
                        ],
                        className='d-none d-xl-block d-lg-block d-md-block d-sm-none col-xl-12 col-lg-12 col-md-12 col-sm-12'),
                    ])
                ],
                className='col-xl-10 col-lg-9 col-md-9 col-sm-10'
            ),
            dbc.Col([
                    html.Img(src="https://raw.githubusercontent.com/Silvertongue26/imss_dashboard/main/assets/imgs/imss-1.svg", width="100%")
                ],
                className='col-xl-2 col-lg-3 col-md-3 col-sm-2'
            ),
        ], style={"marginTop": "50px", 'textAlign': "center"}),
        dbc.Row([
            dbc.Col([
                html.P(["En esta entrega se resume la información disponible al 01 de noviembre de 2021 "
                        "correspondiente al fin de la semana epidemiológica 44— sobre el avance en "
                        "la aplicación de vacunas contra covid-19 en México. Como se ha mencionado en "
                        "actualizaciones anteriores, al no existir una base de datos abierta con "
                        "registros de vacunación, este análisis se basa en información presentada por "
                        "personal de la Secretaría de Salud federal en conferencias de prensa o en sus "
                        "redes sociales. Ante la imposibilidad de verificar datos, se acepta la información "
                        "presentada por las autoridades sanitarias como cierta, y cuando una cifra publicada "
                        "es distinta a otra presentada con anterioridad, se toma como buena la cifra más reciente."],
                       style={"fontSize": "1.2em", 'textAlign': "justify"})
            ],
            className='d-xl-none d-lg-none d-md-none d-sm-block col-xl-12 col-lg-12 col-md-12 col-sm-12'),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.H3(["Avance de vacunación en México"], style={"textAlign":"center"}),
                        html.P("En esta gráfica se muestra el avance progresivo de vacunación a nivel nacional, "
                               "así como el número total de vacunados y con esquema completo."),
                        html.Div([dcc.Graph(figure=fig)])
                    ], className='col-xl-12 col-lg-12 col-md-12 col-sm-12',
                    ),
                ])],
                className="col-xl-6 col-lg-6 col-md-6 col-sm-12",
            ),
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.H3(["Avance de vacunación del personal IMSS"], style={"textAlign":"center"}),
                        html.P("En esta gráfica se muestra el avance de vacunación del personal laboral del IMSS incluyendo "
                               "personal médico y administrativo."),
                        html.Div([dcc.Graph(figure=fig)])
                    ], className='col-xl-12 col-lg-12 col-md-12 col-sm-12',
                    ),
                ])],
                className="col-xl-6 col-lg-6 col-md-6 col-sm-12",
            ),



        ],style={"marginTop": "5%"}),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.H3(["Vigilancia Genómica"], style={"textAlign": "center"}),
                        html.P("La Red Regional de Vigilancia Genómica COVID-19 fue creada en 2020, no sólo como un mecanismo para fortalecer la capacidad de secuenciación de los laboratorios participantes,"
                               " si no como estrategia para incrementar la cantidad de datos de secuenciación disponibles a nivel global,"
                               " lo cual es crítico para mejorar el desarrollo de protocolos de diagnóstico,"
                               " generar información para el desarrollo de vacunas y para entender mejor los patrones de evolución del SARS-CoV-2."
                               "Actualmente se han encontrado 152.456 secuencias del virus"),
                        html.Div([dcc.Graph(figure=fig)])
                    ], className='col-xl-12 col-lg-12 col-md-12 col-sm-12',
                    ),
                ])],
                className="col-xl-12 col-lg-12 col-md-12 col-sm-12",
            ),

        ], style={"marginTop": "5%"}),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.H3(["Eficiencia de vacunas"], style={"textAlign": "center"}),
                        html.P("La efectividad de la vacuna es una medida que calcula cuán fuerte es la protección "
                               "inmunológica que provee para evitar un futuro contagio, la hospitalización o una eventual"
                               " muerte, por el otro. Según la Organización Mundial de la Salud (OMS), se han registrado "
                               "hasta mayo de 2021 un total de 13 vacunas distintas contra el COVID-19."),
                        html.P("La OMS, ha aprobado el uso de emergencia de los fármacos de Pfizer/BioNTech, AstraZeneca, Janssen, Moderna, Sinopharm y Sinovac, si bien ha asegurado que analiza otras vacunas ampliamente usadas como Sputnik V. La OMS y la comunidad científica consideran que una vacuna, contra cualquier enfermedad, es exitosa cuando su efectividad supera el 50 %, como pasa con todas las aprobadas contra la covid."),
                        html.Div([dcc.Graph(figure=fig)])
                    ], className='col-xl-12 col-lg-12 col-md-12 col-sm-12',
                    ),
                ])],
                className="col-xl-12 col-lg-12 col-md-12 col-sm-12",
            ),

        ], style={"marginTop": "5%"}),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.H3(["Conclusiones"], style={"textAlign": "center"}),
                        html.P("Conforme a lo presentado en el análisis previo, se puede observar una gran parte de "
                               "la población, con una sola dósis o sin dósis alguna. Forzando a la adquisición de nuevas "
                               "vacunas, debido a que en muchos casos, el tiempo de protección de la vacuna, ya ha expirado. "
                               "Teniendo en mente que el virus del COVID-19 se volverá una enfermedad concurrente, se tiene que pensar "
                               "en la adquisición constante de vacunas y un esquema de vacunación permanente. "),
                        html.P("Un factor a considerar en la adquisición de vacunas, es la eficiencia contra las diversas cepas presentes en el país. "
                               "En los últimos meses, la cepa predominante es la Delta, por lo que las vacunas de marca Pfizer, Sputnik y Moderna son las que han demostrado una mayor eficiencia."),
                    ], className='col-xl-12 col-lg-12 col-md-12 col-sm-12',
                    ),
                ])],
                className="col-xl-12 col-lg-12 col-md-12 col-sm-12",
            ),
        ], style={"marginTop": "5%"}),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.H3(["Referencias"], style={"textAlign": "left"}),
                        html.P("-¿Cuál es la efectividad actual de las vacunas contra el Covid-19? "),
                        html.A('https://www.forbes.com.mx/cual-es-la-efectividad-actual-de-las-vacunas-contra-el-covid-19/', href='https://www.forbes.com.mx/cual-es-la-efectividad-actual-de-las-vacunas-contra-el-covid-19/'),
                        html.Br(),
                        html.Br(),
                        html.P("-Characteristics of Persons with Covid-19 "),
                        html.A('https://www.nejm.org/doi/full/10.1056/nejmoa2108891', href='https://www.nejm.org/doi/full/10.1056/nejmoa2108891'),
                        html.Br(),
                        html.Br(),
                        html.P("-Mexcov2 "),
                        html.A('http://mexcov2.ibt.unam.mx:8080/COVID-TRACKER/tablero', href='http://mexcov2.ibt.unam.mx:8080/COVID-TRACKER/tablero'),
                        html.Br(),
                        html.Br(),
                        html.P("-Red Regional de Vigilancia Genómica de COVID-19 "),
                        html.A('https://www.paho.org/es/temas/influenza/red-regional-vigilancia-genomica-covid-19', href='https://www.paho.org/es/temas/influenza/red-regional-vigilancia-genomica-covid-19'),
                        html.Br(),
                        html.Br(),
                        html.P("-Tracking SARS-CoV-2 variants "),
                        html.A('https://www.who.int/en/activities/tracking-SARS-CoV-2-variants/', href='https://www.who.int/en/activities/tracking-SARS-CoV-2-variants/'),
                        html.Br(),
                        html.Br(),
                        html.P("-European Centre for Disease Prevention and Control "),
                        html.A('https://www.ecdc.europa.eu/en/covid-19/variants-concern', href='https://www.ecdc.europa.eu/en/covid-19/variants-concern'),
                        html.Br(),
                        html.Br(),
                        html.P("-Mexico Covid-19 Line List "),
                        html.A('https://global.health/deepdive/mexico', href='https://global.health/deepdive/mexico'),
                        html.Br(),
                        html.Br(),
                        html.P("-Tracking of Variants "),
                        html.A('https://www.gisaid.org/hcov19-variants/', href='https://www.gisaid.org/hcov19-variants/'),
                        html.Br(),
                        html.Br(),
                        html.P("-Datos Abiertos Mx "),
                        html.A('https://datos.gob.mx/busca/dataset?tags=covid-19', href='https://datos.gob.mx/busca/dataset?tags=covid-19'),
                        html.Br(),
                        html.Br(),

                    ], className='col-xl-12 col-lg-12 col-md-12 col-sm-12',
                    ),
                ])],
                className="col-xl-12 col-lg-12 col-md-12 col-sm-12",
            ),
        ], style={"marginTop": "5%"}),

])
"""
BODY - ENDS
"""




#Main structure of the page
app.layout = html.Div([
    navbar,
    sub_navbar,
    body,
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


