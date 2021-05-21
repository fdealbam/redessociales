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
#------------------------------Graficas-----------------------------------------------------------------------------


labels = ['facebook','instagram','twitter ','otros']
values = [4500, 2500, 1053, 500]

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

fig.update_layout(
    autosize=False,
    width=500,
    height=500,
    title_text="Share of media types",
    paper_bgcolor='#FAFAFA',)
#fig.show()







df = px.data.stocks()
figtime = px.line(df, x="date", y=df.columns,
              hover_data={"date": "|%B %d, %Y"},
              title='custom tick labels')
figtime.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")
figtime.update_layout(
    template="plotly_white",
    autosize=False,
    width=1000,
    height=500,
    title_text="News suscribers (last 60 days)",
    paper_bgcolor='#FAFAFA',)
#figtime.show()
#####################################################################################################################
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
     dbc.Row([dbc.Col(html.P("Social media followers",
                        #Style de letra
                             style={"font-size": "40px",
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
    
    #---------------------------Facebook-----------------------------------------
      dbc.Row([
          
          dbc.Col(
               dbc.Button((["", html.P(className="fab fa-facebook", 
                                       style={"color": "#01579B",
                                              "background-color": "light",
                                              "font-size": "50px"}),
                                html.P(f"{int(fb_abs):,}", style={"font-size":30}),
                                html.P("Likes", style={"font-size":15}),
                               ]),style={"background-color": "#FAFAFA",
                                       
                                        "offset": 1,
                                        "size":1})),
     #---------------------------Twitter------------------------------------------ 
          dbc.Col(
               dbc.Button((["", html.P(className="fab fa-twitter", 
                                       style={"color": "#80D8FF",
                                             # "background-color": "",
                                              "font-size": "50px"}),
                                html.P(f"{int(fb_abs):,}", style={"font-size":30}),
                                html.P("Followers", style={"font-size":15}),
                               ]),style={"background-color": "#FAFAFA",
                                    
                                        "offset": 1,
                                        "size":1}),),
          
       #---------------------------Instagram------------------------------------- 
        dbc.Col(
               dbc.Button((["", html.P(className="fab fa-instagram", 
                                       style={"color": "#C51162",
                                              "background-color": "light",
                                              "font-size": "50px"}),
                                html.P(f"{int(fb_abs):,}", style={"font-size":30}),
                                html.P("Publishing", style={"font-size":15}),
                               ]),style={"background-color": "#FAFAFA",
                                        "offset": 1,
                                        "size":1,
                                        "margin-right": "800px"})),#],#style={,

 #----------------------------------Grafica total por red -------------------------------------
           dbc.Col(dcc.Graph(figure=fig),style={"margin-left": "800px",
                                               "margin-top":"-290px"})],), 

    
 #----------------------------------Grafica total por red -------------------------------------
           dbc.Row(
               [
                   dbc.Col(dcc.Graph(figure=figtime),style={#"margin-left": "800px",
                                               "margin-top":"-50px"})],), 
    html.Br(),
    html.Br(),
    html.Br(),
    #------------------------------------------Cuadros 
    dbc.Row(
        [
            
            dbc.Col(dbc.Button(([html.P("El monto total de Noviembre 2020 fue de: "), 
                 html.P(f"{int(fb_abs):,}",  
                        style={
                               "color": "dark", 
                               #"font-weight": 'bold',
                               "font-size": "40px",
                               "font-family": "Montserrat",        
                               #"font-weight": 'bold'
                        }),                      
       ]),style={ "background-color": "light",
                  "box-shadow": "50px 90px 100px gray",
                  'margin-left': '100px',
                 } ,disabled=True)),]),
            
            
            
            
            dbc.Row([
            dbc.Col(html.H6("Diciembre"),
                   # width= 3, 
                    width= { "size": 2, "offset":1}),
            dbc.Col(html.H6("Enero")),
                  # width={'size' : "auto","offset":1}),
            dbc.Col(html.H6("Febrero")),
                  # width={'size' : "auto","offset":1}),
            dbc.Col(html.H6("Marzo")),
                  # width={'size' : "auto","offset":1}),
            dbc.Col(html.H6("Abril")),
                  # width={'size' : "auto", "offset":1}),
            dbc.Col(html.H6("Mayo")),
                  # width={'size' : "auto", "offset":1}),

           ], align='left'),
    
               
                
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

    
