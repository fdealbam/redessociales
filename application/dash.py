import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
#import geopandas as gpd
import flask
import os



numeralia = pd.read_csv("https://raw.githubusercontent.com/fdealbam/redessociales/main/Numeralia%20redes%20sociales.csv", error_bad_lines=False)
#Falta renombrar columnas de la bd final 


##########################################################################     titulo
redes = html.Div([
  html.P("Redes sociales"),
    
  
  html.Br(),
  html.Br(),
])

###########################################################################    iconos: Facebook twitter Instagram 
cardredes = dbc.Card(
    dbc.CardBody(
        [html.Br(),
  html.Br(),
               dbc.Button(([
                            dbc.Row(html.P(className="fab fa-facebook", 
                                       style={"color": "#01579B" ,
                                             "font-size": "40px"}
                                          )),
                   html.Br(),

                               
                            dbc.Row(html.P(className="fab fa-twitter", 
                                       style={"color": "#01579B",
                                             "font-size": "40px"}
                                          )),
                   html.Br(),

                            dbc.Row(html.P(className="fab fa-instagram", 
                                       style={"color": "#C51162",
                                             "font-size": "40px"}
                                          )),
                            html.Br(),
                               ]))]) ,
    style={'margin-left': '.74em',
           'height': '21em',
           'width': '7em', }
)

#############################################################################  gráfica 

#GRAFICA PARA MEJORAR

figaro2 = go.Figure()
figaro2.add_trace(go.Bar(x=numeralia['Periodo'],y=numeralia['Nuevos seguidores'],
                marker_color='salmon'  # cambiar nuemeritos de rgb
               ))
figaro2.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 6,
    yaxis=dict(
        title='Nuevos seguidores FB',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    #autosize=False,
    width=800,
    height=400
    )


#PARA LA APP
grafica  = dbc.Card(
    dbc.CardBody(dcc.Graph(figure=figaro2, config= "autosize")))
################################################################################# TABLAS SEGUIDORES, ALCANCE...
#1
#identificadores FACEBOOK
seg_fb = numeralia["Nuevos likes"].sum()
alc_fb = numeralia["Cantidad de posts"].sum()
imp_fb = numeralia["Cantidad de comentarios"].sum()
eng_fb = numeralia["Mensajes recibidos.2"].sum()

#2
#identificadores TWITTER
seg_tw =  numeralia["Nuevos seguidores"].sum()
alc_tw =  numeralia["Número de tweets"].sum()
imp_tw =  numeralia["Retweets realizados"].sum()
eng_tw =  numeralia["Mensajes recibidos"].sum()

#3
#identificadores INSTAGRAM
seg_insta = numeralia["Nuevos seguidores.1"].sum()
alc_insta = numeralia["Número de posts"].sum()
imp_insta = numeralia["Número de Stories"].sum()
eng_insta = numeralia["Mensajes recibidos.1"].sum()


#articulos, comunicados, entrevistas
articulos   = numeralia["Cantidad de artículos"].sum()
comunicados = numeralia["Cantidad de comunicados"].sum()
entrevistas = numeralia["Cantidad de entrevistas"].sum()



################################################################################# 1 seguidores
table_header_S = [
    html.Thead(html.Tr([html.Th("Seguidores")]))
]

row1_s = html.Tr([html.Td(f"{seg_fb:,d}",style={"font-size":18, "font-family":"Sitka Text","color":"salmon"})  ])
row2_s = html.Tr([html.Td(f"{seg_tw:,d}",style={"font-size":22, "font-family":"Sitka Text","color":"salmon",})  ])
row3_s = html.Tr([html.Td(f"{seg_insta:,d}",style={"font-size":18, "font-family":"Sitka Text","color":"salmon"})  ])


table_body_s = [html.Tbody([row1_s, row2_s, row3_s,])]

tableseguidores = dbc.Table(table_header_S + table_body_s, bordered=True, 
                            style={'width': '7em', 
                                   "margin-top":"-304px",
                                   "margin-left":"130px",
                                  "background-color":"#FAFAFA"} )

################################################################################# 2 alcance
#(posts o tweets publicados)
table_header_A = [
    html.Thead(html.Tr([html.Th("alcance")]))
]

row1_a = html.Tr([html.Td(f"{alc_fb:,d}",style={"font-size":18, "font-family":"Sitka Text","color":"brown"})  ])
row2_a = html.Tr([html.Td(f"{alc_tw:,d}",style={"font-size":18, "font-family":"Sitka Text","color":"brown"})  ])
row3_a = html.Tr([html.Td(f"{alc_insta:,d}",style={"font-size":18, "font-family":"Sitka Text","color":"brown"})  ])


table_body_a = [html.Tbody([row1_a, row2_a, row3_a,])]

tablealcance = dbc.Table(table_header_A + table_body_a, bordered=True, 
                            style={'width': '7em', 
                                   "margin-top":"-311px",
                                   "margin-left":"290px",
                                  "background-color":"#FAFAFA"} )
################################################################################## 3 impresiones
# comentarios, retweets, stories
table_header_I = [
    html.Thead(html.Tr([html.Th("Impresiones")]))
]

row1_I = html.Tr([html.Td(f"{imp_fb:,d}",style={"font-size":18, "font-family":"Sitka Text","color":"green"})  ])
row2_I = html.Tr([html.Td(f"{imp_tw:,d}",style={"font-size":18, "font-family":"Sitka Text","color":"green"})  ])
row3_I = html.Tr([html.Td(f"{imp_insta:,d}",style={"font-size":18, "font-family":"Sitka Text","color":"green"})  ])


table_body_I = [html.Tbody([row1_I, row2_I, row3_I,])]

tableImpresiones = dbc.Table(table_header_I + table_body_I, bordered=True, 
                            style={'width': '7em', 
                                   "margin-top":"-311px",
                                   "margin-left":"430px",
                                  "background-color":"#FAFAFA"} )

################################################################################## 4 Engagement
#mensajes recibidos
table_header_eg = [
    html.Thead(html.Tr([html.Th("Engagement")]))
]

row1_eg = html.Tr([html.Td(f"{eng_fb:,d}",style={"font-size":18, "font-family":"Sitka Text","color":"blue"})  ])
row2_eg = html.Tr([html.Td(f"{eng_tw:,d}",style={"font-size":18, "font-family":"Sitka Text","color":"blue"})  ])
row3_eg = html.Tr([html.Td(f"{eng_insta:,d}",style={"font-size":18, "font-family":"Sitka Text","color":"blue"})  ])


table_body_eg = [html.Tbody([row1_eg, row2_eg, row3_eg,])]

tableEngagement = dbc.Table(table_header_eg + table_body_eg, bordered=True, 
                            style={'width': '7em', 
                                   "margin-top":"-311px",
                                   "margin-left":"589px",
                                  "background-color":"#FAFAFA"} )


############################################################################### BOTONES ARTICULOS, COMUNICADOS, ENTREVISTAS
articulos= dbc.Card(
    dbc.CardBody(dbc.Button((["", html.P(className="far fa-file-alt", 
                                       style={"color": "#78909C",
                                              "background-color": "light",
                                              "font-size": "40px"}),
                                html.P(f"{int(articulos):,}", style={"font-size":25}),
                                html.P("artículos", style={"font-size":15}),
                               ]),style={"background-color": "#FAFAFA"}))),
########################################################################
# A P P 
########################################################################

FONT_AWESOMEpro1 = "{% static 'fontawesome_pro/js/all.min.js' %}"
FONT_AWESOMEpro = "{% static 'fontawesome_pro/css/all.min.css' %}"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
server = flask.Flask(__name__)    
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. 
                                                #CERULEAN, 
                                                #COSMO, 
                                                #CYBORG, 
                                                #DARKLY, 
                                                #FLATLY, 
                                                #JOURNAL, 
                                                #LITERA, 
                                                #LUMEN, #SIRVE 
                                                LUX, 
                                                #MATERIA, 
                                                #MINTY, 
                                                #PULSE, 
                                                #SANDSTONE, #SIRVE 
                                                #SIMPLEX, 
                                                #SKETCHY, 
                                                #SLATE, 
                                                #SOLAR, 
                                                #SPACELAB, 
                                                #SUPERHERO, 
                                                #UNITED, 
                                                #YETI, 
                                                FONT_AWESOMEpro1,
                                                FONT_AWESOME, 
                                                FONT_AWESOMEpro], server=server)

app.layout = html.Div(
    [redes, cardredes, tableseguidores,tablealcance ,tableImpresiones,tableEngagement,  grafica ], 
            style={
          #  'margin-top': '0px',
           # 'margin-left': '5px',
           # 'width': '1400px',
            #'height': '1413px',
         #   'backgroundColor': 'white'
            },)


if __name__ == '__main__':
    app.run_server()
 
