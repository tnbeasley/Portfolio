import pandas as pd
import numpy as np
import dash
from dash.dependencies import Input, Output, State
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


# About me - experiences
## Modals/Callbacks
### TVA
tva_modal = html.Div(
    [
        dbc.Button(
            "Tennessee Valley Authority",
            id = "openTvaModal",
            outline = True,
            block = True
        ),
        dbc.Modal(
            [
                dbc.ModalHeader("Tennessee Valley Authority"),
                dbc.ModalBody(
                    [
                        html.Li("Partner with multiple departments to lead the programming of an R Shiny application used to inform future prices of TVA by simulating various billing structures and expected effects on customer segments"),
                        html.Li("Integrate SQL data uploads and imports within R to optimize application performance and store results from simulations for other teams to access and analyze"),
                        html.Li("Construct R Shiny Dashboard to convey retail pricing trends across the Tennessee Valley over last 5 years"),
                        html.Li("Develop rapport with customer consultants while processing over 50% of fiscal year 2020 rate change requests"),
                        html.Li("Spearhead creation of departmental process performance benchmarks and program a reproducible R markdown report to easily present performance trends and patterns"),
                        html.Br(),
                        html.A([html.Center([
                            html.Img(src = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/US-TennesseeValleyAuthority-Logo.svg/1200px-US-TennesseeValleyAuthority-Logo.svg.png",
                                     width = 200,
                                     height = 200)])],
                            href = "https://www.tva.com"
                        )
                    ]
                ),
                dbc.ModalFooter(
                    dbc.Button("Close", id = "closeTvaModal", className="ml-auto")
                )
            ],
            id = "tvaModal",
            centered = True,
            size = "lg"
        )
    ]
)
@app.callback(
    Output("tvaModal", "is_open"),
    [Input("openTvaModal", "n_clicks"), Input("closeTvaModal", "n_clicks")],
    [State("tvaModal", "is_open")]
)
def toggle_tva_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

### Melton Scholars
melton_modal = html.Div(
    [
        dbc.Button(
            "Melton Scholar Program",
            id = "openMeltonModal",
            outline = True,
            block = True
        ),
        dbc.Modal(
            [
                dbc.ModalHeader("Melton Scholar Program"),
                dbc.ModalBody(),
                dbc.ModalFooter(
                    dbc.Button("Close", id = "closeMeltonModal", className="ml-auto")
                )
            ],
            id = "meltonModal",
            centered = True
        )
    ]
)
@app.callback(
    Output("meltonModal", "is_open"),
    [Input("openMeltonModal", "n_clicks"), Input("closeMeltonModal", "n_clicks")],
    [State("meltonModal", "is_open")]
)
def toggle_tva_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

## Jumbotron
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
                                        tva_modal
                                    ],
                                    width = 6),

                                dbc.Col(
                                    [
                                        melton_modal
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
    ],
    fluid = True
)


# About me - skills
## Modals/callbacks


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
                                            "Python",
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
                                            "R",
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
                                            "SQL", 
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
            ],
            fluid = True
        )
    ],
    fluid = True
)


# About me - education
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
    ],
    fluid = True
)


# Tabs
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
                            width = 12
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
                ),
                
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                education_jumbotron
                            ],
                            width = 12
                        )
                    ]
                )
            ]
        )
    ],
    
    label = "About Me"
)

tabs = dbc.Tabs(
    [
        resume_tab
    ]
)


# App layout
app.layout = dbc.Container(
    [
        navbar,
        dbc.Container([tabs], fluid = True)
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)