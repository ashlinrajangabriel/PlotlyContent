# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 10:57:58 2021

@author: scarl
"""

import dash
import dash_html_components as html
import plotly.graph_objects as go
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
import numpy as np
import dash_table as dt
import dash_table
import colorlover
import dash_html_components as html
from nsetools import Nse
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])   


nse = Nse()
import pandas as pd
losers=pd.DataFrame(nse.get_top_losers())
winners=pd.DataFrame(nse.get_top_gainers())
columns = losers.columns

#Pricedifference
losers['HighLowDifference'] = losers['ltp']-losers['openPrice']
winners['HighLowDifference'] = winners['ltp']-winners['openPrice']
losers.drop('series', axis=1, inplace=True)
winners.drop('series', axis=1, inplace=True)

PLOTLY_LOGO = "https://www.pngkey.com/png/full/773-7732073_multichoice-is-delighted-todeliver-the-best-movies-m.png"

navbar = dbc.Navbar( id = 'navbar', children = [
    dbc.Row([
        dbc.Col(html.Img(src = PLOTLY_LOGO, height = "40px")),

        dbc.Col(
             
            dbc.NavbarBrand(" Stock Crash Dashboard", style = {'margin-left': '130px','text-align':'center','color':'white', 'fontSize':'25px','fontFamily':'Times New Roman'}
                            )
            
            ),
        
        dbc.Col(
            dbc.NavLink("Performers",href='/',active='exact', style = {'margin-left': '130px','text-align':'center','color':'white', 'fontSize':'20px','fontFamily':'Times New Roman'}) 
            )
        
        
        ],align = "center"
       ),
    
    
    ], color = '#000000')


#INfluencers are positive and negative win and lossers
def Personnel(influencers):
  for i in range(0,len(influencers)):
    print(influencers.symbol[i],influencers.lowPrice[i])

###############################################
body_app = dbc.Container([
    html.Br(),
    html.Hr(),
    html.H3("Exceeding performers"),
dbc.Row([ 
dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in winners.columns],
    data=winners.to_dict('records')
    ),
   html.Br()
   ])
     ,     

 html.Br(),
  html.Br(),
  
   html.H3("Exceeding Losers"),
dbc.Row([ 
dash_table.DataTable(
    id='table1',
    data=losers.to_dict('records'),
    sort_action='native',
    columns=[
        {"name": i, "id": i} for i in losers.columns
    ],
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{netPrice} < 0',
                'column_id': 'netPrice'
            },
            'color': 'tomato',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{netPrice} > 0',
                'column_id': 'netPrice'
            },
            'textDecoration': 'underline'
        }
    ]

    )
  ]
            )
        
    
   ],style = {'margin-left': '10px'})


    


app.layout =  html.Div(id='parent', children = [navbar,body_app])



if __name__ == '__main__':
    app.run_server(debug=True)
