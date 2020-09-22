import pandas as pd
import numpy as np
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Tanner Beasley Portfolio"


# Create navigation bar at top of page
navbar = dbc.NavbarSimple(
    brand = 'Tanner Beasley Portfolio',
    brand_href = "https://www.linkedin.com/in/tanner-beasley/",
    brand_external_link = True
)


# Create tabs
experiences_jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.Center([html.H2(["Notable Experiences"])]),
                html.Hr(),
                html.Center(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            "Tennessee Valley Authority", 
                                            outline = True,
                                            block = True
                                        )
                                    ],
                                    width = 6),

                                dbc.Col(
                                    [
                                        dbc.Button(
                                            "Melton Scholar Program", 
                                            outline = True,
                                            block = True
                                        )
                                    ],
                                    width = 6
                                )
                            ]
                        )
                    ]
                )
                
            ],
            fluid = True
        )
    ]
)

education_jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.Center([html.H2(["Education"])]),
                html.Hr(),
                html.Center(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            "Undergraduate Studies", 
                                            outline = True,
                                             block = True
                                        )
                                    ],
                                    width = 6
                                ),

                                dbc.Col(
                                    [
                                        dbc.Button(
                                            "Graduate Studies", 
                                            outline = True,
                                            block = True
                                        )
                                    ],
                                    width = 6
                                )
                            ]
                        )
                    ]
                )
                
            ],
            fluid = True
        )
    ]
)

skills_jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.Center([html.H2(["Skills"])]),
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Center(
                                    [
                                        dbc.Button(
                                            html.H4(["Python"]),
                                            outline = True,
                                            block = True
                                        )
                                    ]
                                )
                            ],
                            width = 4
                        ),
                        
                        dbc.Col(
                            [
                                html.Center(
                                    [
                                        dbc.Button(
                                            html.H4(["R"]),
                                            outline = True,
                                            block = True
                                        )
                                    ]
                                )
                            ],
                            width = 4
                        ),
                        
                        dbc.Col(
                            [
                                html.Center(
                                    [
                                        dbc.Button(
                                            html.H4(["SQL"]), 
                                            outline = True,
                                            block = True
                                        )
                                    ]
                                )
                            ],
                            width = 4
                        )
                    ]
                )
            ]
        )
    ]
)

resume_tab = dbc.Tab(
    [
        dbc.Container(
            [
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                experiences_jumbotron
                            ],
                            width = 6
                        ),
                        
                        dbc.Col(
                            [
                                education_jumbotron
                            ],
                            width = 6
                        )
                    ]
                ),
                
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                skills_jumbotron
                            ],
                            width = 12
                        )
                    ]
                )
            ]
        )
    ],
    
    label = "Resume"
)

tabs = dbc.Tabs(
    [
        resume_tab
    ]
)


app.layout = dbc.Container(
    [
        navbar,
        dbc.Container([tabs], fluid = True)
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)