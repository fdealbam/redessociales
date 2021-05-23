import dash
import matplotlib.pyplot as plt 
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
import geopandas as gpd
import flask
import os
from numpy.core.defchararray import add

yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

today = date.today()
d2 = today.strftime("Fecha de actualización : %d-%m-%Y")



fb_abs = 8766
fb_prc = .69
#####################################################################################################################
#procesos

#Facebook twitter Instagram 
cardredes = dbc.Card(
    dbc.CardBody(
        [
               dbc.Button((["", 
                              html.Br(),
                            html.P(className="fab fa-facebook", 
                                       style={"color": "#01579B",
                                              "background-color": "light",
                                              "font-size": "90px",
                                             "margin-top":"-195px"
                                             
                                             }),
                               
                              
                                html.Br(),
                               ]),style={"background-color": "#FAFAFA"}),
 
            dbc.Button((["", html.P("impresiones", style={"font-size":13}),
                             html.P("alcance", style={"font-size":13}),
                             html.P("engagement", style={"font-size":13}),
                             html.P("seguidores", style={"font-size":13}),
                           
                            ]),style={"background-color": "#FAFAFA"}),
    
            dbc.Button((["", html.P(f"{int(fb_abs):,}", style={"font-size":15, "color":"#1A237E"}),
                              html.P(f"{int(fb_abs):,}", style={"font-size":15}),
                             html.P(f"{int(fb_abs):,}", style={"font-size":15}),
                             html.P(f"{int(fb_abs):,}", style={"font-size":15}),
                            ]),style={"background-color": "#FAFAFA" }),
          
        ]
    ),

    style={"border": "0",
           "card-border": "0",
      
           #"height": 150,
       #    'margin-left': '-30px',
           "background-color": "#FAFAFA",
          },
)

cardredes2 = dbc.Card(
    dbc.CardBody(
        [
               dbc.Button((["", 
                              html.Br(),
                            html.P(className="fab fa-twitter", 
                                       style={"color": "#01579B",
                                              "background-color": "light",
                                              "font-size": "90px",
                                             "margin-top":"-195px"
                                             
                                             }),
                               
                              
                                html.Br(),
                               ]),style={"background-color": "#FAFAFA"}),
 
            dbc.Button((["", html.P("impresiones", style={"font-size":13}),
                             html.P("alcance", style={"font-size":13}),
                             html.P("engagement", style={"font-size":13}),
                             html.P("seguidores", style={"font-size":13}),
                           
                            ]),style={"background-color": "#FAFAFA"}),
    
            dbc.Button((["", html.P(f"{int(fb_abs):,}", style={"font-size":15, "color":"#1A237E"}),
                              html.P(f"{int(fb_abs):,}", style={"font-size":15}),
                             html.P(f"{int(fb_abs):,}", style={"font-size":15}),
                             html.P(f"{int(fb_abs):,}", style={"font-size":15}),
                            ]),style={"background-color": "#FAFAFA" }),
          
        ]
    ),

    style={"border": "0",
           "card-border": "0",
      
           #"height": 150,
       #    'margin-left': '-30px',
           "background-color": "#FAFAFA",
          },
)
#-------------------------------------------------------------------------------------------------------------------

#articles, releases, interviews
#cardredes2 = dbc.Card(
#    dbc.CardBody(
#        [
#               dbc.Button((["", html.P(className="far fa-file-alt", 
#                                       style={"color": "#78909C",
#                                              "background-color": "light",
#                                              "font-size": "40px"}),
#                                html.P(f"{int(fb_abs):,}", style={"font-size":20}),
#                                html.P("artículos", style={"font-size":13}),
#                               ]),style={"background-color": "#FAFAFA"}),
# 
#               dbc.Button((["", html.P(className="fas fa-bullhorn", 
#                                       style={"color": "#78909C",
#                                              "font-size": "40px"}),
#                                html.P(f"{int(fb_abs):,}", style={"font-size":20}),
#                                html.P("comunicados", style={"font-size":13}),
#                               ]),style={"background-color": "#FAFAFA"}),
#    
#               dbc.Button((["", html.P(className="fas fa-users", 
#                                       style={"color": "#78909C",
#                                              "background-color": "light",
#                                              "font-size": "40px"}),
#                                html.P(f"{int(fb_abs):,}", style={"font-size":20}),
#                                html.P("entrevistas", style={"font-size":13}),
#                               ]),style={"background-color": "#FAFAFA" }),
#            
#        ]
#    ),
#
#    style={"border": "0",
#           "card-border": "0",
#      
#           #"height": 150,
#       #    'margin-left': '-30px',
#           "background-color": "#FAFAFA",
#          },
#)

#--------------------------------------------------------------------------------------------------------------------
botonmedio = dbc.Card(
    dbc.CardBody(
        [
               dbc.Button((["", html.P("impresiones de la página" ,
                                       style={"color": "#78909C",
                                              "background-color": "light",
                                              "font-size": "15px"}),
                                html.P(f"{int(fb_abs):,}", style={"font-size":30}),
                             #   html.P(className="fas fa-sort-up", 
                             #          style={"font-size":25,
                             #                "color":"green"}),
                               html.P(f"{int(fb_prc):,}" "%    ▲", 
                                       style={ "font-size": "15px"})
                               ]),style={"background-color": "#FAFAFA"}),
 
               dbc.Button((["", html.P("usuarios",
                                       style={"color": "#78909C",
                                              "font-size": "15px"}),
                                html.P(f"{int(fb_abs):,}", style={"font-size":30}),
                                html.P(f"{int(fb_prc):,}" "%    ▼", 
                                       style={ "font-size": "15px"})
                               ]),style={"background-color": "#FAFAFA"}),
    
               dbc.Button((["", html.P("historias compartidas",
                                       style={"color": "#78909C",
                                              "background-color": "light",
                                              "font-size": "15px"}),
                                html.P(f"{int(fb_abs):,}", style={"font-size":30}),
                                html.P(f"{int(fb_prc):,}" "%    ▼", 
                                       style={ "font-size": "15px"})
                               ]),style={"background-color": "#FAFAFA" }),
            
               dbc.Button((["", html.P("    retweet",
                                       style={"color": "#78909C",
                                              "background-color": "light",
                                              "font-size": "15px",
                                             "text-align":"center"}),
                                html.P(f"{int(fb_abs):,}", style={"font-size":30}),
                              html.P(f"{int(fb_prc):,}" "%    ▲", 
                                       style={ "font-size": "15px"})
                               ]),style={"background-color": "#FAFAFA" }),
            
        ]
    ),

    style={"border": "0",
           "card-border": "0",
      
           #"height": 150,
       #    'margin-left': '-30px',
           "background-color": "#FAFAFA",
          },
)
##############################################################################################################


#GRAFICAS
##########################################################################Grafica redes
labels = ['facebook','instagram','twitter ','otros']
values = [4500, 2500, 1053, 500]

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

fig.update_layout(
    autosize=False,
    width=350,
    height=280,
    title_text="Share of media types",
    paper_bgcolor='#FAFAFA',)
#fig.show()


#-------------prepara para dash
cardgraph = dbc.Card(
    dbc.CardBody(
        [dcc.Graph(figure=fig)]))
#########################################################################################

################################################################################Grafica last 30 days
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

figtime = go.Figure([go.Scatter(x=df['Date'], y=df['AAPL.High'])])
figtime.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")
figtime.update_layout(
    template="plotly_white",
    autosize=False,
    width=900,
    height=250,
    title_text="seguidores nuevos (últimos 30 días)",
    paper_bgcolor='#FAFAFA',)



#-------------prepara para dash
cardgraph30days = dbc.Card(
    dbc.CardBody(
        [dcc.Graph(figure=figtime)]),
    style={#"width": "20rem", 
          "border": "0",
           "card-border": "0",
           #"height": 150,
         'margin-left': '-30px',
           "background-color": "#FAFAFA",
          },)
######################################################################################################################
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Codigo del dashboard <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
###################################################################################################################### 


# identificadores
FONT_AWESOMEpro1 = "{% static 'fontawesome_pro/js/all.min.js' %}"
FONT_AWESOMEpro = "{% static 'fontawesome_pro/css/all.min.css' %}"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"


server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. 
                                                LUX, 
                                                FONT_AWESOMEpro1,
                                                FONT_AWESOME, 
                                                FONT_AWESOMEpro], server=server)

body = html.Div([
  
 ###################################titulos del dash     
    html.Br(),
    
        dbc.Row(
            [dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Vacunas/blob/main/SRE.JPG?raw=true?raw=true"),
                        width={'size': 1,  "offset": 1 }),
             dbc.Col(html.H5("Secretaría de Relaciones Exteriores, "
                            "Subsecretaría para Asuntos Multilaterales y "
                            "Derechos Humanos"),
                        width={'size': 6, 'offset' : 0}), 
        ],justify="start"),
    
    dbc.Row(
           [dbc.Col(html.H6(d2),           #Fecha de actualización
               width={'size' : "auto", 'offset' : 2})]),
  
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    #------------------------------------social media followers
    #------------------------------------Titulo smf
     dbc.Row([dbc.Col(html.P("seguidores en redes sociales",
                        #Style de letra
                             style={"font-size": "45px",
                              "color": "grey",
                              #'textAlign': 'center',
                               #"font-weight": 'bold',
                               "font-family": "Open Sans"
                              }),
                      #style del espacio ocupado
                      style={"margin-left": "30px"}
            ),]),
      html.Br(),
    html.Br(),       
    #---------------------------Cuadro social media-----------------------------

    dbc.Row([
        dbc.Col([dbc.Card(cardredes),],style={"width": "35%"}),
        dbc.Col([dbc.Card(botonmedio),],style={"width": "75%"}),#Variables Vivienda
        dbc.Col([dbc.Card(cardgraph)],style={"width": "200px"})
     ]),
    
    #-
      #-----------------------------------------articles, interviews and 
     
    dbc.Row([
         dbc.Col(dbc.Card(cardredes2))],
        style={
            
            "margin-top": "-140px",
            'width': '34%',
          #  'height': '56px',
            
            }),
        html.Br(),
 #################################################################
    dbc.Row([
        dbc.Col(dbc.Card(cardgraph30days))] ,
        style={
            
          #  "margin-top": "-240px",
            'width': "900px",
            'height': '56px',
            
            }),                      
   
            

 #----------------------------------Grafica total por red -------------------------------------
           

    
 #----------------------------------Grafica total por red -------------------------------------

    html.Br(),
    html.Br(),
    html.Br(),

    
               
                
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
])



app.layout = html.Div([ body, 
                      # buttons, metropolis# layer2,
                       #collapse, fade
                      ],style={
            'margin-top': '0px',
            'margin-left': '10px',
            'width': '1400px',
            'height': '1413px',
            'backgroundColor': '#FAFAFA'
            })


if __name__ == '__main__':
    app.run_server()
