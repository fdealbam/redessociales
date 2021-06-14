

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


medios = pd.read_csv("https://raw.githubusercontent.com/fdealbam/redessociales/main/medios.csv", encoding='latin-1')
redes = pd.read_csv("https://raw.githubusercontent.com/fdealbam/redessociales/main/redes.csv", encoding='latin-1')

totalesredes = pd.read_csv("https://raw.githubusercontent.com/fdealbam/redessociales/main/Seguimiento%20RS%2C%20comunicados%2C%20art%2C%20entrevistas%202021a.csv")
#totfacebook= totalesredes["27-may"][0:1]
#totfacebook





###########################################################################    
# IDENTIFICADORES DE RECUADRO GENERAL 
###########################################################################

#1
#Instagram
seg_tw = redes.iloc[0]["Seguidores"]
imp_tw = redes.iloc[0]["Impresiones"] 
int_tw = redes.iloc[0]["Interacciones"]
nws_tw = redes.iloc[0]["Nuevos seguidores"]
tot_tw = seg_tw+imp_tw+int_tw+nws_tw #Total TW


#FB
seg_fb = redes.iloc[1]["Seguidores"]
imp_fb = redes.iloc[1]["Impresiones"] 
int_fb = redes.iloc[1]["Interacciones"]
nws_fb = redes.iloc[1]["Nuevos seguidores"]
tot_fb = seg_fb+imp_fb+int_fb+nws_fb #Total fb

#IG
seg_insta = redes.iloc[2]["Seguidores"]
imp_insta = redes.iloc[2]["Impresiones"] 
int_insta = redes.iloc[2]["Interacciones"]
nws_insta = redes.iloc[2]["Nuevos seguidores"]


#articulos, comunicados, entrevistas
articulos=medios.iloc[4]['Artículos']
comunicados=medios.iloc[4]['Comunicados']
entrevistas=medios.iloc[4]['Entrevistas']
presenciamed=medios.iloc[4]['Presencia en medios']



#totales secciones
#tot_seg = seg_fb + seg_tw + seg_insta    
#tot_alc = alc_fb + alc_tw + alc_insta
#tot_imp = imp_fb + imp_tw + imp_insta
#tot_eng = eng_fb + eng_tw + eng_insta


tot= totalesredes["27-may"][0:4].astype(int)
tottwitter = tot[0]
totfacebook = tot[1]
totinstagram = tot[2]


###########################################################################    
# gráfica donas
###########################################################################    
    

# Add the grand total row, summing all values in a column
#base = numeralia.loc['Grand Total', :] = numeralia.sum()
#base.to_csv("basetotales.csv")
#abre= pd.read_csv("basetotales.csv")
#abre.rename(columns = {"0":'valor', 'Unnamed: 0':'variable'}, inplace = True)




################################################### 
# Grafica 1. SEGUIDORES
#
#figvac_seguidores = px.pie(redes, values=redes["Seguidores"], names=redes['Redes sociales'],
#                color_discrete_sequence=px.colors.sequential.Peach, hole=.3,
#                    )
#
#
#figvac_seguidores.update_layout(
#    #title="Seguidores",
#                  paper_bgcolor='rgba(0,0,0,0)',
#                  plot_bgcolor='rgba(0,0,0,0)',
#                  autosize=True,
#                  font_color="black",
#                  title_font_size=10,
#                  legend_title_side="left",
#                  title_font_color="black",
#                  width=350,
#                  height=350,
#                  showlegend=False
#                               ),
#    
#colors = ['#B3E5FC']
#
#figvac_seguidores.update_traces(rotation=220,
#                               marker=dict(#colors=colors,
#                                          ))



################################################### 
## Grafica 2. IMPRESIONES


#-GRÁFICA ALCANCE
figvac_alcance = px.pie(redes, values='Impresiones', names='Redes sociales',
                color_discrete_sequence=px.colors.sequential.Brwnyl, hole=.3,
                      )

figvac_alcance.update_layout(
    #title="Alcance",
    paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  autosize=True,
                  font_color="black",
                  title_font_size=10,
                  legend_title_text="top",
                  title_font_color="black",
                  width=400,
                  height=400,
                  showlegend=False),
    
colors = ['#B3E5FC']

figvac_alcance.update_traces(rotation=220,
                               marker=dict(#colors=colors
                                          ))




################################################### 
# Grafica 3. Interacciones


#Grafica impresiones

figvac_impresiones = px.pie(redes, values='Interacciones', names='Redes sociales',
                color_discrete_sequence=px.colors.sequential.Tealgrn, hole=.3)

figvac_impresiones.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  #title="Impresiones",
                  plot_bgcolor='rgba(0,0,0,0)',
                  autosize=True,
                  font_color="black",
                  title_font_size=10,
                  legend_title_text="top",
                  title_font_color="black",
                  width=400,
                  height=400,
                  showlegend=False),
    
colors = ['#B3E5FC']

figvac_impresiones.update_traces(rotation=250,
                               marker=dict(#colors=colors
                                          ))



################################################### 
# Grafica 4. Nuevos Seguidores

figvac_newseguidores = px.pie(redes, values='Nuevos seguidores', names='Redes sociales',
                color_discrete_sequence=px.colors.sequential.Purp, hole=.3)

figvac_newseguidores.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  #title="Engagement ",
                  plot_bgcolor='rgba(0,0,0,0)',
                  autosize=True,
                  font_color="black",
                  title_font_size=10,
                  legend_title_text="top",
                  title_font_color="black",
                  width=350,
                  height=350,
                  showlegend=False),
    
colors = ['#B3E5FC']

figvac_newseguidores.update_traces(rotation=265,
                               marker=dict(#colors=colors
                                          ))





###########################################################################
# Grafica BARRAS. SEGUIDORES DE FACEBOOK
###########################################################################


#figaro2 = go.Figure()
#figaro2.add_trace(go.Bar(x=numeralia2['Periodo'],y=numeralia2['Nuevos seguidores'],
#                marker_color="#01579B"  # cambiar nuemeritos de rgb
#               ))
#figaro2.update_layout(
#    paper_bgcolor='rgba(0,0,0,0)',
#    plot_bgcolor='rgba(0,0,0,0)',
#    xaxis_tickangle=-45,
#    template = 'simple_white',
#    #title='Seguidores Facebook',
#    title_font_size= 14,
#    xaxis_tickfont_size= 16,
#    width=1600,
#    height=600
#    )



figtres = go.Figure(data=[
    go.Bar(name='Twitter', x=numeralia2["Periodo"], y=numeralia2["Nuevos seguidores"], marker_color='#82B1FF'),
    go.Bar(name='Facebook', x=numeralia["Periodo"], y=numeralia2["Nuevos likes"], marker_color='#1A237E'),
    go.Bar(name='Instagram', x=numeralia2["Periodo"], y=numeralia2["Nuevos seguidores.1"], marker_color='#880E4F'),
])
# Change the bar mode
figtres.update_layout(height=600,width=1550,barmode='group',paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',xaxis_tickfont_size= 16,title_font_size= 18,
                    #legend = dict(font = dict(family = "Sitka Text", size = 16, color = "black")),
                  legend_title = dict(font = dict(family = "Sitka Text", size = 22, color = "black")))


###########################################################################    
# RECUADRO GENERAL 
###########################################################################

# Tabla
table_header = [
    html.Thead(html.Tr([#html.Th("Seguidores",style={"font-size":28, "font-family":"Arial Black","color":"lightgray","text-align": "center"}),
                        html.Th("Impresiones",style={"font-size":28, "font-family":"Arial Black","color":"lightgray","text-align": "center"}),
                        html.Th("Interacciones",style={"font-size":28, "font-family":"Arial Black","color":"lightgray","text-align": "center"}),
                        html.Th("Nuevos seguidores",style={"font-size":28, "font-family":"Arial Black","color":"lightgray","text-align": "center",}),
                       ]))
]

row1_fb = html.Tr([#html.Td(f"{seg_fb:,d}",style={"font-size":38, "font-family":"Sitka Text","color":"#1A237E","text-align": "center"}),
                  html.Td(f"{imp_fb:,d}", style={"font-size":38, "font-family":"Sitka Text","color":"#1A237E","text-align": "center"}),
                  html.Td(f"{int_fb:,d}",style={"font-size":38, "font-family":"Sitka Text","color":"#1A237E","text-align": "center"}),
                  html.Td(f"{nws_fb:,d}",style={"font-size":38, "font-family":"Sitka Text","color":"#1A237E","text-align": "center"}),
                   ])
row2_tw = html.Tr([#html.Td(f"{seg_tw:,d}",style={"font-size":48, "font-family":"Sitka Text","color":"#82B1FF","text-align": "center",}),
                  html.Td(f"{imp_tw:,d}",style={"font-size":48, "font-family":"Sitka Text","color":"#82B1FF","text-align": "center"}),
                  html.Td(f"{int_tw:,d}",style={"font-size":48, "font-family":"Sitka Text","color":"#82B1FF","text-align": "center"}),
                  html.Td(f"{nws_tw:,d}",style={"font-size":48, "font-family":"Sitka Text","color":"#82B1FF","text-align": "center"}), 
                 ])
row3_it = html.Tr([#html.Td(f"{seg_insta:,d}",style={"font-size":38, "font-family":"Sitka Text","color":"#880E4F","text-align": "center"}),
                   html.Td(f"{imp_insta:,d}",style={"font-size":38, "font-family":"Sitka Text","color":"#880E4F","text-align": "center"}),
                   html.Td(f"{int_insta:,d}",style={"font-size":38, "font-family":"Sitka Text","color":"#880E4F","text-align": "center"}),
                   html.Td(f"{nws_insta:,d}",style={"font-size":38, "font-family":"Sitka Text","color":"#880E4F","text-align": "center"})
                  ])

row_gs= html.Tr([#html.Td(dcc.Graph(figure=figvac_seguidores)),
                 html.Td(dcc.Graph(figure=figvac_alcance)),
                 html.Td(dcc.Graph(figure=figvac_impresiones)),
                 html.Td(dcc.Graph(figure=figvac_newseguidores)), 
                 
                ])

table_body = [html.Tbody([row2_tw, row1_fb,  row3_it, row_gs])]





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

app.layout = html.Div([
    
    ###################################################
    #TITULO
    ##################################################
  html.Br(),
  html.Br(),

    dbc.Row(
            [dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Vacunas/blob/main/SRE.JPG?raw=true?raw=true"),
                        width={'size': 1,  "offset": 1 }),
             dbc.Col(html.H5("Secretaría de Relaciones Exteriores, "
                            "Subsecretaría para Asuntos Multilaterales y "
                            "Derechos Humanos"),
                        width={'size': 3, 'offset' : 0}), 
        ],justify="start"),
  html.Br(),
  html.P("Período: del 1o de enero al 30 de abril 2021", 
         style={"font-size":20, "margin-left":"250px",
                                "font-family":"Sitka Text","color":"gray",}),
  html.Br(),
  html.Br(),
  html.Br(),
  html.Br(),
  html.Br(),
    dbc.Row(
        [dbc.Col(html.P(['Impacto de la imagen institucional']),
                style={"font-size":58, "margin-left":"120px",
                                "font-family":"Sitka Text","color":"purple",
                                "text-align": "left"}),
         
        html.P('En este dashboard se presentan análisis de los distintos impactos que en redes sociales tiene la Subsecretaría, específicamente en Twitter, Facebook e Instagram, en el intervalo que comprenden del mes de enero a abril 2021.',
                style={"font-size":22, "margin-left":"130px",
                                "font-family":"Sitka Text",
                                "color":"black",
                                "text-align": "left"}),
         
    ], ),
  html.Br(),
  html.Br(),
  html.Br(),
  html.Br(),
  html.Br(),
  html.Br(),
    dbc.Row(
        [dbc.Col(html.P(['Total de seguidores (ene-abr)']),
                style={"font-size":40, "margin-left":"450px",
                                "font-family":"Sitka Text","color":"purple",
                                "text-align": "left"}),
    ], ),
  html.Br(),
    
    #Cuadros totales generales 
    dbc.Row([
        dbc.Col(dbc.Button(([html.P(className="fab fa-twitter", 
                                       style={"color": "#01579B",
                                              "background-color": "light",
                                              "font-size": "80px"}),
        html.P("Twitter", style={"font-size": "20px",
                                              "font-family":"Sitka Text"}), 
                 html.P(f"{int(seg_tw):,}",  
                        style={
                               "color": "dark", 
                               #"font-weight": 'bold',
                               "font-size": "40px",
                               "font-family": "Sitka Text",        
                               #"font-weight": 'bold'
                        }),                      
       ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px black",
              
                  'margin-left': '250px',
                 } ,disabled=True)),
    
#     dbc.Button(([html.P("Alcance", style={"font-size": "20px",
#                                             "font-family":"Sitka Text"}), 
#                html.P((tot_alc),  
#                       style={
#                              "color": "dark", 
#                              #"font-weight": 'bold',
#                              "font-size": "40px",
#                              "font-family": "Sitka Text",        
#                              #"font-weight": 'bold'
#                       }),                      
#      ]),style={ "background-color": "light",
#                 "box-shadow": "10px 20px 30px gray",
#                 'margin-left': '225px',
#                } ,disabled=True),
#   
         dbc.Col(dbc.Button(([html.P(className="fab fa-facebook", 
                                       style={"color": "#01579B",
                                              "background-color": "light",
                                              "font-size": "80px"}),
                        html.P("Facebook", style={"font-size": "20px",
                                              "font-family":"Sitka Text"}), 
                        html.P(f"{int(seg_fb):,}",  
                        style={
                               "color": "dark", 
                               #"font-weight": 'bold',
                               "font-size": "40px",
                               "font-family": "Sitka Text",        
                               #"font-weight": 'bold'
                        }),                             
                         ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px black",
                  'margin-left': '150px',
                 } ,disabled=True)),
    
      dbc.Col(dbc.Button(([html.P(className="fab fa-instagram", 
                                       style={"color": "#C51162",
                                              "background-color": "light",
                                              "font-size": "80px"}),
                        html.P("Instagram", style={"font-size": "20px",
                                              "font-family":"Sitka Text"}), 
                        html.P(f"{int(seg_insta):,}",  
                        style={
                               "color": "dark", 
                               #"font-weight": 'bold',
                               "font-size": "40px",
                               "font-family": "Sitka Text",        
                               #"font-weight": 'bold'
                        }),                             
       ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px black",
                 'margin-left': '80px',
                 } ,disabled=True), )
    ], ),
  html.Br(),
  html.Br(),
  html.Br(),
 html.Br(),
  html.Br(),
  html.Br(),
  html.Br(),
  html.Br(),
    dbc.Row(
        [dbc.Col(html.P(['Imagen institucional (ene-abr)']),
                style={"font-size":40, "margin-left":"450px",
                                "font-family":"Sitka Text","color":"purple",
                                "text-align": "left"}),
    ]),
 #######################################################
    #ICONOS
 ####################################################
  dbc.Button(([
      dbc.Row(html.P(className="fab fa-twitter",style={'margin-top':'1.9em', "color": "#01579B","font-size": "75px"})),
                   html.Br(),
      dbc.Row(html.P(className="fab fa-facebook",style={"color": "#01579B" ,"font-size": "75px"} )),
                   html.Br(),
      dbc.Row(html.P(className="fab fa-instagram",style={"color": "#C51162", "font-size": "75px"})),
                   html.Br(),
                               ]),disabled=True ,style={'margin-left':'.7em',
                                          'margin-top':'.50em',
                                          'height': '21em',
                                          'width': '7em', }),
    ###########################################################
    #TABLA GENERAL 
    ##########################################################
    dbc.Table(table_header + table_body, bordered=True, 
                            style={'width': '7em', 
                                   "margin-top":"-250px",
                                   "margin-left":"130px",
                                  "background-color":"#FAFAFA"} ),
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),

    
    ##############################################################
#GRAFICA BARRAS
   #############################################################
  html.P("Nuevos seguidores, según red",style={"font-size":40, "margin-left":"100px",
                               "font-family":"Sitka Text","color":"purple",
                               "text-align": "left"}),

   dbc.Row([
       dbc.Col(dcc.Graph(figure=figtres),#, config= "autosize"),
               style={"margin-left": "10px",
                     }),
   ]),
   
   
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
    
    html.P("Influencia en medios (ene-abr)",style={"font-size":40, "margin-left":"450px",
                                "font-family":"Sitka Text","color":"purple",
                                "text-align": "left"}),

    
    
################################################################
#### BOTONES ARTICULOS, COMUNICADOS, ENTREVISTAS
################################################################
    
     dbc.Row([

     # Presencia en medios     
     dbc.Button(([html.P(className="far fa-newspaper", 
                                       style={"color": "#78909C",
                                              "background-color": "light",
                                              "font-size": "90px"}),
                                html.Br(),
                                html.Br(),
                                html.P(f"{int(presenciamed):,}", style={"font-size":65, "font-family":"Sitka Text","color":"#82B1FF","text-align": "center",}),
                                html.Br(),
                                html.P("Presencia en medios", style={"font-size":20}),
                               ]),style={"margin-left": "150px",
                                         #"margin-right": "120px",
                                         "background-color": "#FAFAFA"}),
 
         
         
     # Entrevistas    
               dbc.Button(([html.P(className="fas fa-users", 
                                       style={"color": "#78909C",
                                              "background-color": "light",
                                              "font-size": "80px"}),
                                html.Br(),
                                html.Br(),
                            html.P(f"{int(entrevistas):,}", 
                                   style={"font-size":65, "font-family":"Sitka Text","color":"#82B1FF","text-align": "center",}),
                                html.Br(),
                                html.P("Entrevistas", style={"font-size":20}),
                                        ]),style={"background-color": "#FAFAFA",
                                         "margin-left": "150px",         
                                         #"margin-right": "50px",
                                        }),      

     # Comunicados    
               dbc.Button(([html.P(className="fas fa-bullhorn", 
                                       style={"color": "#78909C",
                                              "font-size": "80px"}),
                                html.Br(),
                                html.Br(),
                                html.P(f"{int(comunicados):,}", style={"font-size":65, "font-family":"Sitka Text","color":"#82B1FF","text-align": "center",}),
                                html.Br(),
                                html.P("Comunicados", style={"font-size":20}),
                               ]),style={#"margin-right": "50px",
                                         "margin-left": "150px",
                                         "background-color": "#FAFAFA"}),

     # ARticulos    
     dbc.Button(([html.P(className="far fa-file-alt", 
                                       style={"color": "#78909C",
                                              "background-color": "light",
                                              "font-size": "80px"}),
                                html.Br(),
                                html.Br(),
                                html.P(f"{int(articulos):,}", style={"font-size":65, "font-family":"Sitka Text","color":"#82B1FF","text-align": "center",}),
                                html.Br(),
                                html.P("artículos", style={"font-size":20}),
                               ]),style={"margin-left": "150px",
                                         #"margin-right": "120px",
                                         "background-color": "#FAFAFA"}),
 

         
         
         
     ]),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
  
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),

       dbc.Row(
            [dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Vacunas/blob/main/SRE.JPG?raw=true?raw=true"),
                        width={'size': 1,  "offset": 8 }),
             dbc.Col(html.H5("Secretaría de Relaciones Exteriores, "
                            "Subsecretaría para Asuntos Multilaterales y "
                            "Derechos Humanos"),
                        width={'size': 3, 'offset' : 0}), 
        ],justify="start"),
       html.Br(),
       html.Br(),
       html.Br(),
    
 
    ], 
            style={
          #  'margin-top': '0px',
           # 'margin-left': '5px',
            'width': '1400px',
            #'height': '1413px',
         #   'backgroundColor': 'white'
            },)



if __name__ == '__main__':
    app.run_server()
    
