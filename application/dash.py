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
import flask
import os



numeralia = pd.read_csv("https://raw.githubusercontent.com/fdealbam/redessociales/main/Numeralia%20redes%20sociales.csv", error_bad_lines=False)
#Falta renombrar columnas de la bd final 
numeralia2 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/redessociales/main/Numeralia%20redes%20sociales.csv", error_bad_lines=False)

##########################################################################     titulo
redes = html.Div([
   dbc.Row(
            [dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Vacunas/blob/main/SRE.JPG?raw=true?raw=true"),
                        width={'size': 1,  "offset": 1 }),
             dbc.Col(html.H5("Secretaría de Relaciones Exteriores, "
                            "Subsecretaría para Asuntos Multilaterales y "
                            "Derechos Humanos"),
                        width={'size': 6, 'offset' : 0}), 
        ],justify="start"),
    
    dbc.Row(
        [dbc.Col(html.H1(['Redes Sociales ']),
                style={"color": "red", 'text-transform': "uppercase", 
                       "font-weight": 'bolder', "font-stretch": "condensed",
                      "font-size": "x-large" },
                width={ "offset":2 }),
    ]),
  
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
    style={'margin-left': '.7em',
           'height': '21em',
           'width': '7em', }
)
#############################################################################  gráfica donas
#tratamiento para gráfica 
# Add the grand total row, summing all values in a column
base = numeralia.loc['Grand Total', :] = numeralia.sum()
base.to_csv("basetotales.csv")
abre= pd.read_csv("basetotales.csv")
abre.rename(columns = {"0":'valor', 'Unnamed: 0':'variable'}, inplace = True)

#seleccionar columnas seguidores
seguidor = abre[(abre["variable"] == "Nuevos seguidores")|
                  (abre["variable"] == "Nuevos seguidores.1")|
                  (abre["variable"] == "Nuevos likes")]


seguidor.to_csv("seguidores.csv")
seguidores = pd.read_csv("seguidores.csv")
################################################### grafica
figvac_seguidores = px.pie(seguidores, values='valor', names='variable',
                color_discrete_sequence=px.colors.sequential.Turbo, hole=.5, 
                    )

figvac_seguidores.update_layout(
    title="Seguidores",
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  autosize=True,
                  font_color="black",
                  title_font_color="black",
                  width=250,
                  height=250,
                  showlegend=False
                               ),
    
colors = ['#B3E5FC']

figvac_seguidores.update_traces(rotation=90,
                               marker=dict(colors=colors))

#---------------------------------------------------------------------------------------GRAFICA ALCANCE
#seleccionar columnas alcance
alcanc = abre[(abre["variable"] == "Cantidad de posts")|
                (abre["variable"] == "Número de tweets")|
                (abre["variable"] == "Número de posts")]


alcanc.to_csv("alcance.csv")
alcance = pd.read_csv("alcance.csv")

#-GRÁFICA ALCANCE
figvac_alcance = px.pie(alcance, values='valor', names='variable',
                color_discrete_sequence=px.colors.sequential.Turbo, hole=.5,
                      )

figvac_alcance.update_layout(
    title="Alcance",
    paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  autosize=True,
                  font_color="black",
                  title_font_color="black",
                  width=250,
                  height=250,
                  showlegend=False),
    
colors = ['#B3E5FC']

figvac_alcance.update_traces(rotation=90,
                               marker=dict(colors=colors))


####--------------------------------------------------------------------------------GRAFICA IMPRESIONES
#seleccionar columnas impresiones
impresione = abre[(abre["variable"] == "Cantidad de comentarios")|
                  (abre["variable"] == "Retweets realizados")|
                  (abre["variable"] == "Número de Stories")]


impresione.to_csv("impresiones.csv")
impresiones = pd.read_csv("impresiones.csv")
#Grafica impresiones

figvac_impresiones = px.pie(impresiones, values='valor', names='variable',
                color_discrete_sequence=px.colors.sequential.Turbo, hole=.5)

figvac_impresiones.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  title="Impresiones",
                  plot_bgcolor='rgba(0,0,0,0)',
                  autosize=True,
                  font_color="black",
                  title_font_color="black",
                  width=250,
                  height=250,
                  showlegend=False),
    
colors = ['#B3E5FC']

figvac_impresiones.update_traces(rotation=90,
                               marker=dict(colors=colors))

############################################################################## ENGAGEMENT


#seleccionar columnas engagement
engagemen= abre[(abre["variable"] == "Mensajes recibidos.2")|
                (abre["variable"] == "Mensajes recibidos")|
                (abre["variable"] == "Mensajes recibidos.1")]


engagemen.to_csv("engagement.csv")
engagement = pd.read_csv("engagement.csv")
figvac_engagement = px.pie(engagement, values='valor', names='variable',
                color_discrete_sequence=px.colors.sequential.Turbo, hole=.5)

figvac_engagement.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  title="Engagement ",
                  plot_bgcolor='rgba(0,0,0,0)',
                  autosize=True,
                  font_color="black",
                  title_font_color="black",
                  width=250,
                  height=250,
                  showlegend=False),
    
colors = ['#B3E5FC']

figvac_engagement.update_traces(rotation=90,
                               marker=dict(colors=colors))

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
seg_fb = numeralia2["Nuevos likes"].sum()
alc_fb = numeralia2["Cantidad de posts"].sum()
imp_fb = numeralia2["Cantidad de comentarios"].sum()
eng_fb = numeralia2["Mensajes recibidos.2"].sum()

#2
#identificadores TWITTER
seg_tw =  numeralia2["Nuevos seguidores"].sum()
alc_tw =  numeralia2["Número de tweets"].sum()
imp_tw =  numeralia2["Retweets realizados"].sum()
eng_tw =  numeralia2["Mensajes recibidos"].sum()

#3
#identificadores INSTAGRAM
seg_insta = numeralia2["Nuevos seguidores.1"].sum()
alc_insta = numeralia2["Número de posts"].sum()
imp_insta = numeralia2["Número de Stories"].sum()
eng_insta = numeralia2["Mensajes recibidos.1"].sum()


#articulos, comunicados, entrevistas
articulos   = numeralia2["Cantidad de artículos"].sum()
comunicados = numeralia2["Cantidad de comunicados"].sum()
entrevistas = numeralia2["Cantidad de entrevistas"].sum()



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
    [redes, cardredes, tableseguidores,tablealcance ,tableImpresiones,tableEngagement,
     html.Br(),
    # html.P("prueba"),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=figvac_seguidores, config= "autosize")),
        dbc.Col(dcc.Graph(figure=figvac_alcance, config= "autosize"), 
                style={"margin-left": "-115px"}),
        dbc.Col(dcc.Graph(figure=figvac_impresiones, config= "autosize"),
                style={"margin-left": "-115px"}),
        dbc.Col(dcc.Graph(figure=figvac_engagement, config= "autosize"),
                style={"margin-left": "-115px"}),
    ],style={"width":"1000px"}),
     html.Br(),
     
    # graficaseguidores, graficaalcance,graficaimpresiones,
     grafica,
 
    
 
    ], 
            style={
          #  'margin-top': '0px',
           # 'margin-left': '5px',
           # 'width': '1400px',
            #'height': '1413px',
         #   'backgroundColor': 'white'
            },)


if __name__ == '__main__':
    app.run_server()
 
