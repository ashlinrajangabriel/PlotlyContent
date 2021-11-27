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

from nsetools import Nse
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])   


nse = Nse()
import pandas as pd
losers=pd.DataFrame(nse.get_top_losers())
winners=pd.DataFrame(nse.get_top_gainers())
columns = losers.columns

#INfluencers are positive and negative win and lossers
def Personnel(influencers):
  for i in range(0,len(influencers)):
    print(influencers.symbol[i],influencers.lowPrice[i])


body_app = dbc.Container([
 dbc.Col([  
   dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in winners.columns],
    data=winners.to_dict('records')
    )
    ]),
 dbc.Col([  
   dash_table.DataTable(
    id='table1',
    columns=[{"name": i, "id": i} for i in losers.columns],
    data=losers.to_dict('records')
    )
    ])
        
    
   ])
   


app.layout =  html.Div(id='parent', children = [body_app])



if __name__ == '__main__':
    app.run_server(debug=True)
