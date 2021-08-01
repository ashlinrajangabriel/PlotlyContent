# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:54:25 2021

@author: anmol
"""
################################### Important Point ##############################
#################################
###    Please add debug = True in line 399 if you are running the code using Anaconda Prompt 
###    and want to autoupdate the changes while making the changes.  

import dash
import dash_html_components as html
import plotly.graph_objects as go
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd






xls = pd.ExcelFile(r'C:\Users\Asus\Desktop\PersonalResearch\Accenture\Data\ACNReporting.xlsx')
GeoMarketsRevenue = pd.read_excel(xls, 'Geo Markets Revenue')
IndustryGroupsRevenue = pd.read_excel(xls, 'Industry Groups-Revenue')
EPSGAAPAdjusted = pd.read_excel(xls, 'EPS-GAAP-Adjusted')




################################ Revenues  ###################################
TOTAL_REVENUES = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == 'Q3')  ].groupby(['Fiscal Year','Quarter','Q1FY21 Performance','Format','Currency']).agg({'Revenues and Growth in Local Currency':'sum'}).reset_index()
TOTAL_REVENUES["CURRENCY"] ='$'
GEO_REVENUES = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == 'Q3')  ].groupby(['Fiscal Year','Geographical Markets','PercentIncrease','Quarter','Format','Currency']).agg({'Revenues and Growth in Local Currency':'sum'}).reset_index()
GEO_REVENUES["CURRENCY"] ='$'
IndustryGroupsRevenue["CURRENCY"] = '$'





app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])   

PLOTLY_LOGO = "https://www.pngkit.com/png/full/198-1986371_accenture-logo-transparent-accenture-greater-than-logo.png"

navbar = dbc.Navbar( id = 'navbar', children = [
    dbc.Row([
        dbc.Col(html.Img(src = PLOTLY_LOGO, height = "40px")),

        dbc.Col(
             
            dbc.NavbarBrand("Earnings Dashboard", style = {'margin-left': '130px','text-align':'center','color':'white', 'fontSize':'25px','fontFamily':'Times New Roman'}
                            )
            
            )
        
        
        ],align = "center",
        no_gutters = True),
    
    
    ], color = '#655e9e')


##Drop down 
card_content_dropdwn = [
    dbc.CardBody(
        [
            html.H6('FiscalYear 2021', style = {'textAlign':'center'}),
            
            dbc.Row([
                
                dbc.Col([
                    
                    html.H6('Current Quarter'),
                    
                    dcc.Dropdown( id = 'dropdown_Quarter_base',
        options = [
            {'label':i, 'value':i } for i in GeoMarketsRevenue.sort_values('Fiscal Year')['Quarter'].drop_duplicates()
        
            ],
        value = 'Q2',
        
        )
                    
                    
                    ]),
                
                dbc.Col([
                    
                    html.H6('Reference Quarter'),
                    
                    dcc.Dropdown( id = 'dropdown_Quarter_Comparison',
        options = [
            {'label':i, 'value':i } for i in GeoMarketsRevenue.sort_values('Fiscal Year')['Quarter'].drop_duplicates()
        
            ],
        value = 'Q3',
        
        )
                    
                    
                    ]),
                
                
                
                
                ])
            
            ]
        )
    
    
    
    ]


###############################################
body_app = dbc.Container([
    html.Br(),
    html.Br(),
    
    dbc.Row([
             dbc.Col([dbc.Card(card_content_dropdwn,style={'height':'150px'})],width=4),
             dbc.Col([dbc.Card(id = 'card_performance_description',style={'height':'150px'})])
             
             ]) ,
    html.Br(),
    html.Br(),     
    #Market segmentation        
    dbc.Row([
             dbc.Col([dbc.Card(id = 'Accenture_Total_Revenue_Card',style={'height':'190px','width':'190px'})]),
             dbc.Col([dbc.Card(id = 'Market_Market_Card',style={'height':'190px'})]),
             #bc.Col([dbc.Card(id = 'card_num6',style={'height':'150px'})]),
             #html.Hr(style = {'height':'26px','color':'gray','background-color':'##15479e','width':'650px'})
             
             ]) ,

    
    html.Br(),     
    #Industry segmentation        
    dbc.Row([
              dbc.Card(id = 'IndustryGroups_Card',style={'width':'1280px'})

             ]) ,
    html.Hr(style = {'height':'25px','color':'gray','background-color':'#15479e','width':'100%'}),
        
    
    #Eps & Returning Cash to shareholders.
    dbc.Row([
    
    #EPS Card Operating Margin
    dbc.Col([
             dbc.Row([dbc.Card(id = 'EPS_Card',style={'height':'190px','width':'190px'})]),
             dbc.Row([dbc.Card(id = 'OPS_Card',style={'height':'190px'})]),
             #bc.Col([dbc.Card(id = 'card_num6',style={'height':'150px'})]),
             #html.Hr(style = {'height':'26px','color':'gray','background-color':'##15479e','width':'650px'})
             
             ]) ,
    
    #EPS Card Operating Margin
    dbc.Row([
             dbc.Row([
                 dbc.Col([
                 dbc.Card(id = 'Strong_Free_cashflow_card',style={'height':'190px','width':'190px'}),
                 ]),
                 dbc.Col([
                 dbc.Card(id = 'Share_Repurchases_card',style={'height':'190px','width':'190px'}),
                 dbc.Card(id = 'Dividends_paid_card',style={'height':'190px','width':'190px'}),
                    ]),
                 

             dbc.Col([dbc.Card(id = 'Quarterly_cash_dividend',style={'height':'190px','width':'190px'})]),
             #bc.Col([dbc.Card(id = 'card_num6',style={'height':'150px'})]),
             #html.Hr(style = {'height':'26px','color':'gray','background-color':'##15479e','width':'650px'})
             
             ])
             ]),    
    
#FreeCashFlow_Card_Content,ShareRepurchases_Card_Content,Dividend_Card_Content,Quarterly_CashDividend_Content    
    ]),
    html.Hr(style = {'height':'25px','color':'gray','background-color':'#15479e','width':'100%'}),    
    
    
    
    ##Next container dbc 
    
    
    #Block ends container
             ],

             style = {'backgroundColor':'#f7f7f7'},
             fluid = True)
    
       
    


app.layout = html.Div(id='parent', children = [navbar,body_app])


#Lets create callback

@app.callback([
                Output('Accenture_Total_Revenue_Card','children'),
                Output('Market_Market_Card','children'),
                Output('card_performance_description','children'),
                Output('IndustryGroups_Card', 'children'),
                Output('EPS_Card', 'children'),
                Output('OPS_Card', 'children'),
                Output('Strong_Free_cashflow_card', 'children'),
                Output('Share_Repurchases_card', 'children'),
                Output('Dividends_paid_card', 'children'),
                Output('Quarterly_cash_dividend', 'children'),

              ],
                [Input('dropdown_Quarter_base','value'),
                 Input('dropdown_Quarter_Comparison','value')])

def update_cards(base,comparison):

#Card performance description
    Performance_Description = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == base)]['Q1FY21 Performance'].dropna().drop_duplicates().reset_index()['Q1FY21 Performance'][0]
    Performance_Description = Performance_Description
########################################################    
    Revenue_base = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == base)  ].groupby(['Fiscal Year','Quarter','Q1FY21 Performance','Format','Currency']).agg({'Revenues and Growth in Local Currency':'sum'}).reset_index()['Revenues and Growth in Local Currency'][0].round(2)
    Revenue_comp = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == comparison)  ].groupby(['Fiscal Year','Quarter','Q1FY21 Performance','Format','Currency']).agg({'Revenues and Growth in Local Currency':'sum'}).reset_index()['Revenues and Growth in Local Currency'][0].round(2)

    revenue_difference = np.round(Revenue_base - Revenue_comp,2)
    if revenue_difference >= 0:
        revenue_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',revenue_difference,'B')],style={'textAlign':'center'})
    elif revenue_difference <=0 :
         revenue_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(revenue_difference),'B')],style={'textAlign':'center'})
################### #EUROPE  
    EUROPE_Revenue_base = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == base)  ].groupby(['Fiscal Year','Quarter','Geographical Markets']).agg({'Revenues and Growth in Local Currency':'sum'}).reset_index()['Revenues and Growth in Local Currency'][0].round(2)
    EUROPE_Revenue_comp = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == comparison)  ].groupby(['Fiscal Year','Quarter','Geographical Markets']).agg({'Revenues and Growth in Local Currency':'sum'}).reset_index()['Revenues and Growth in Local Currency'][0].round(2)
    EUROPE_revenue_difference = np.round(EUROPE_Revenue_base - EUROPE_Revenue_comp,2)   
    if EUROPE_revenue_difference >= 0:
        EUROPE_revenue_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',EUROPE_revenue_difference,'B')],style={'textAlign':'center'})
    elif EUROPE_revenue_difference <=0 :
         EUROPE_revenue_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(EUROPE_revenue_difference),'B')],style={'textAlign':'center'})         
         
#################################################         
###################  North America
    NorthAmerica_Revenue_base = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == base)  ].groupby(['Fiscal Year','Quarter','Geographical Markets']).agg({'Revenues and Growth in Local Currency':'sum'}).reset_index()['Revenues and Growth in Local Currency'][2].round(2)
    NorthAmerica_Revenue_comp = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == comparison)  ].groupby(['Fiscal Year','Quarter','Geographical Markets']).agg({'Revenues and Growth in Local Currency':'sum'}).reset_index()['Revenues and Growth in Local Currency'][2].round(2)
    NorthAmerica_revenue_difference = np.round(NorthAmerica_Revenue_base - NorthAmerica_Revenue_comp,2)   
    if NorthAmerica_revenue_difference >= 0:
        NorthAmerica_revenue_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',NorthAmerica_revenue_difference,'B')],style={'textAlign':'center'})
    elif NorthAmerica_revenue_difference <=0 :
         NorthAmerica_revenue_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(NorthAmerica_revenue_difference),'B')],style={'textAlign':'center'})         
   
#####GrowthMarkets
    GrowthMarkets_Revenue_base = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == base)  ].groupby(['Fiscal Year','Quarter','Geographical Markets']).agg({'Revenues and Growth in Local Currency':'sum'}).reset_index()['Revenues and Growth in Local Currency'][1].round(2)
    GrowthMarkets_Revenue_comp = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == comparison)  ].groupby(['Fiscal Year','Quarter','Geographical Markets']).agg({'Revenues and Growth in Local Currency':'sum'}).reset_index()['Revenues and Growth in Local Currency'][1].round(2)
    GrowthMarkets_revenue_difference = np.round(GrowthMarkets_Revenue_base - GrowthMarkets_Revenue_comp,2)   
    if GrowthMarkets_revenue_difference >= 0:
        GrowthMarkets_revenue_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',GrowthMarkets_revenue_difference,'B')],style={'textAlign':'center'})
    elif GrowthMarkets_revenue_difference <=0 :
         GrowthMarkets_revenue_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(GrowthMarkets_revenue_difference),'B')],style={'textAlign':'center'})         

         
##########EPS 
    EPS_base = EPSGAAPAdjusted[ (EPSGAAPAdjusted['Quarter'] == base)  ].groupby(['Fiscal Year','Quarter']).agg({'EPS (GAAP)':'sum'}).reset_index()['EPS (GAAP)'][0].round(2)
    EPS_comp = EPSGAAPAdjusted[ (EPSGAAPAdjusted['Quarter'] == comparison)  ].groupby(['Fiscal Year','Quarter']).agg({'EPS (GAAP)':'sum'}).reset_index()['EPS (GAAP)'][0].round(2)
    EPS_difference = np.round(EPS_base - EPS_comp,2)   
    print(EPS_difference)
    if EPS_difference >= 0:
        EPS_sign_flip  = dcc.Markdown( dangerously_allow_html = True, children = ["<sub>+{0}{1}{2}</sub>".format('$',(EPS_difference),'B')],style={'textAlign':'center'})         
                                                 
    elif EPS_difference <=0 :
        EPS_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(EPS_difference),'B')],style={'textAlign':'center'})         

         

####OPerating margin
    #Operating Margin

    Operating_Margin_base= EPSGAAPAdjusted[(EPSGAAPAdjusted['Component'] == 'Operating Margin') & (EPSGAAPAdjusted['Quarter'] == base)  ].groupby(['Fiscal Year','Quarter','Component']).agg({'Amount':'sum'}).reset_index()['Amount'][0].round(2)
    Operating_Margin_comp= EPSGAAPAdjusted[(EPSGAAPAdjusted['Component'] == 'Operating Margin') & (EPSGAAPAdjusted['Quarter'] == comparison)  ].groupby(['Fiscal Year','Quarter','Component']).agg({'Amount':'sum'}).reset_index()['Amount'][0].round(2)
    Operating_Margin_difference = np.round(Operating_Margin_base- EPS_comp,2)   
    if Operating_Margin_difference >= 0:
        Operating_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',Operating_Margin_difference,'%')],style={'textAlign':'center'})
    elif Operating_Margin_difference <=0 :
        Operating_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(Operating_Margin_difference),'%')],style={'textAlign':'center'})         

################################################################################################################
#########Industry gorups  IndustryGroupsRevenue

##########Communications , Media and Technology 
    COMM_MEDIA_TEC__Services_base = IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Communications, Media & Technology')  & (IndustryGroupsRevenue['Quarter'] == base ) ]["Amount"].reset_index()['Amount'][0]
    COMM_MEDIA_TEC__Services_comp = IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Communications, Media & Technology')  & (IndustryGroupsRevenue['Quarter'] == comparison ) ]["Amount"].reset_index()['Amount'][0]
    COMM_MEDIA_TEC__Margin_difference = np.round(COMM_MEDIA_TEC__Services_base- COMM_MEDIA_TEC__Services_comp,2)   
    if COMM_MEDIA_TEC__Margin_difference >= 0:
        COMM_MEDIA_TEC__Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',COMM_MEDIA_TEC__Margin_difference,'B')],style={'textAlign':'center'})
    elif COMM_MEDIA_TEC__Margin_difference <=0 :
        COMM_MEDIA_TEC__Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(COMM_MEDIA_TEC__Margin_difference),'B')],style={'textAlign':'center'})         
    

###########Financial services

    Financial_Services_base = IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Financial Services')  & (IndustryGroupsRevenue['Quarter'] == base ) ]["Amount"].reset_index()['Amount'][0]
    Financial_Services_comp = IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Financial Services')  & (IndustryGroupsRevenue['Quarter'] == comparison ) ]["Amount"].reset_index()['Amount'][0]
    Financial_Margin_difference = np.round(Financial_Services_base- Financial_Services_comp,2)   
    if Financial_Margin_difference >= 0:
        Financial_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',Financial_Margin_difference,'B')],style={'textAlign':'center'})
    elif Financial_Margin_difference <=0 :
        Financial_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(Financial_Margin_difference),'B')],style={'textAlign':'center'})         
    


###Health & Public services 
    HEALTH_Services_base = IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Health and public services')  & (IndustryGroupsRevenue['Quarter'] == base ) ]["Amount"].reset_index()['Amount'][0]
    HEALTH_Services_comp = IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Health and public services')  & (IndustryGroupsRevenue['Quarter'] == comparison ) ]["Amount"].reset_index()['Amount'][0]
    HEALTH_Margin_difference = np.round(HEALTH_Services_base- HEALTH_Services_comp,2)   
    if HEALTH_Margin_difference >= 0:
        HEALTH_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',HEALTH_Margin_difference,'B')],style={'textAlign':'center'})
    elif HEALTH_Margin_difference <=0 :
        HEALTH_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(HEALTH_Margin_difference),'B')],style={'textAlign':'center'})         
    


#####Products #####Resources
    Products_Services_base = IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Products')  & (IndustryGroupsRevenue['Quarter'] == base ) ]["Amount"].reset_index()['Amount'][0]
    Products_Services_comp = IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Products')  & (IndustryGroupsRevenue['Quarter'] == comparison ) ]["Amount"].reset_index()['Amount'][0]
    Products_Margin_difference = np.round(Products_Services_base- Products_Services_comp,2)   
    if Products_Margin_difference >= 0:
        Products_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',Products_Margin_difference,'B')],style={'textAlign':'center'})
    elif Products_Margin_difference <=0 :
        Products_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(Products_Margin_difference),'B')],style={'textAlign':'center'})         

#####Resources
    Resources_Services_base = IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Resources')  & (IndustryGroupsRevenue['Quarter'] == base ) ]["Amount"].reset_index()['Amount'][0]
    Resources_Services_comp = IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Resources')  & (IndustryGroupsRevenue['Quarter'] == comparison ) ]["Amount"].reset_index()['Amount'][0]
    Resources_Margin_difference = np.round(Resources_Services_base- Resources_Services_comp,2)   
    if Resources_Margin_difference >= 0:
        Resources_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',Resources_Margin_difference,'B')],style={'textAlign':'center'})
    elif Resources_Margin_difference <=0 :
        Resources_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(Resources_Margin_difference),'B')],style={'textAlign':'center'})         
    
#####Returning cash to shareholders

#Strong free cashflow 
    Strong_free_Cashflow_Margin_base= EPSGAAPAdjusted[(EPSGAAPAdjusted['Component'] == 'Very strong free cash flow') & (EPSGAAPAdjusted['Quarter'] == base)  ].groupby(['Fiscal Year','Quarter','Component']).agg({'Amount':'sum'}).reset_index()['Amount'][0].round(2)
    Strong_free_Cashflow_Margin_comp= EPSGAAPAdjusted[(EPSGAAPAdjusted['Component'] == 'Very strong free cash flow') & (EPSGAAPAdjusted['Quarter'] == comparison)  ].groupby(['Fiscal Year','Quarter','Component']).agg({'Amount':'sum'}).reset_index()['Amount'][0].round(2)
    Strong_free_Cashflow_Margin_difference = np.round(Strong_free_Cashflow_Margin_base- Strong_free_Cashflow_Margin_comp,2)   
    if Strong_free_Cashflow_Margin_difference >= 0:
        Strong_free_Cashflow_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',Strong_free_Cashflow_Margin_difference,'B')],style={'textAlign':'center'})
    elif Strong_free_Cashflow_Margin_difference <=0 :
        Strong_free_Cashflow_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(Strong_free_Cashflow_Margin_difference),'B')],style={'textAlign':'center'})         


#Share repurchases 
    Share_repurchases_Margin_base= EPSGAAPAdjusted[(EPSGAAPAdjusted['Component'] == 'Share repurchases') & (EPSGAAPAdjusted['Quarter'] == base)  ].groupby(['Fiscal Year','Quarter','Component']).agg({'Amount':'sum'}).reset_index()['Amount'][0].round(2)
    Share_repurchases_Margin_comp= EPSGAAPAdjusted[(EPSGAAPAdjusted['Component'] == 'Share repurchases') & (EPSGAAPAdjusted['Quarter'] == comparison)  ].groupby(['Fiscal Year','Quarter','Component']).agg({'Amount':'sum'}).reset_index()['Amount'][0].round(2)
    Share_repurchases_Margin_difference = np.round(Share_repurchases_Margin_base- Share_repurchases_Margin_comp,2)   
    if Share_repurchases_Margin_difference >= 0:
        Share_repurchases_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',Share_repurchases_Margin_difference,'M')],style={'textAlign':'center'})
    elif Share_repurchases_Margin_difference <=0 :
        Share_repurchases_Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(Share_repurchases_Margin_difference),'M')],style={'textAlign':'center'})         


#Dividend paid 

    DIVIDEND_PAID__Margin_base= EPSGAAPAdjusted[(EPSGAAPAdjusted['Component'] == 'Dividends paid') & (EPSGAAPAdjusted['Quarter'] == base)  ].groupby(['Fiscal Year','Quarter','Component']).agg({'Amount':'sum'}).reset_index()['Amount'][0].round(2)
    DIVIDEND_PAID__Margin_comp= EPSGAAPAdjusted[(EPSGAAPAdjusted['Component'] == 'Dividends paid') & (EPSGAAPAdjusted['Quarter'] == comparison)  ].groupby(['Fiscal Year','Quarter','Component']).agg({'Amount':'sum'}).reset_index()['Amount'][0].round(2)
    DIVIDEND_PAID__Margin_difference = np.round(DIVIDEND_PAID__Margin_base- DIVIDEND_PAID__Margin_comp,2)   
    if DIVIDEND_PAID__Margin_difference >= 0:
        DIVIDEND_PAID__Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',DIVIDEND_PAID__Margin_difference,'M')],style={'textAlign':'center'})
    elif DIVIDEND_PAID__Margin_difference <=0 :
        DIVIDEND_PAID__Margin_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(DIVIDEND_PAID__Margin_difference),'M')],style={'textAlign':'center'})         

#Quarterly cash dividend 
    Quarterly_Cash_dividend_base= EPSGAAPAdjusted[(EPSGAAPAdjusted['Component'] == 'Quarterly cash dividend declared') & (EPSGAAPAdjusted['Quarter'] == base)  ].groupby(['Fiscal Year','Quarter','Component']).agg({'Amount':'sum'}).reset_index()['Amount'][0].round(2)
    Quarterly_Cash_dividend_comp= EPSGAAPAdjusted[(EPSGAAPAdjusted['Component'] == 'Quarterly cash dividend declared') & (EPSGAAPAdjusted['Quarter'] == comparison)  ].groupby(['Fiscal Year','Quarter','Component']).agg({'Amount':'sum'}).reset_index()['Amount'][0].round(2)
    Quarterly_Cash_dividend_difference = np.round(Quarterly_Cash_dividend_base- Quarterly_Cash_dividend_comp,2)   
    if Quarterly_Cash_dividend_difference >= 0:
        Quarterly_Cash_dividend_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',Quarterly_Cash_dividend_difference,'per share')],style={'textAlign':'center'})
    elif Quarterly_Cash_dividend_difference <=0 :
        Quarterly_Cash_dividend_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(Quarterly_Cash_dividend_difference),'per share')],style={'textAlign':'center'})         


#New bookings 

    NewBookings_base= EPSGAAPAdjusted[(EPSGAAPAdjusted['Component'] == 'New Bookings') & (EPSGAAPAdjusted['Quarter'] == base)  ].groupby(['Fiscal Year','Quarter','Component']).agg({'Amount':'sum'}).reset_index()['Amount'][0].round(2)
    NewBookings_comp= EPSGAAPAdjusted[(EPSGAAPAdjusted['Component'] == 'New Bookings') & (EPSGAAPAdjusted['Quarter'] == comparison)  ].groupby(['Fiscal Year','Quarter','Component']).agg({'Amount':'sum'}).reset_index()['Amount'][0].round(2)
    NewBookings_difference = np.round(NewBookings_base- NewBookings_comp,2)   
    if NewBookings_difference >= 0:
        NewBookings_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                                  children = ["<sub>+{0}{1}{2}</sub>".format('$',NewBookings_difference,'B')],style={'textAlign':'center'})
    elif NewBookings_difference <=0 :
        NewBookings_sign_flip  = dcc.Markdown( dangerously_allow_html = True, 
                                           children = ["<sub>+{0}{1}{2}</sub>".format('$',np.abs(NewBookings_difference),'B')],style={'textAlign':'center'})         

     
         
         
         
#################################################      Your cards contents are below
##############Performance card
    Performance_card_Content = [
        
        dbc.CardBody(
            [
                #html.Hr(style = {'height':'20px','color':'gray','background-color':'#702c94','width':'400px'}),
                html.H3('Performance', style = {'font':'light','textAlign':'Left'}),
                html.H6('{0}'.format(str(Performance_Description)), style = {'color':'#090059','textAlign':'center'}),
                
             
                
                
                
                
                ],
            
                   
            )  
        ]
    


#########################################Revenue card 
    Revenue_Card_Content = [
        
        dbc.CardBody(
            [
                html.Hr(style = {'height':'26px','color':'gray','background-color':'#702c94','width':'150px'}),
                html.H6('Total Revenue', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",Revenue_base,"B"), style = {'color':'#090059','textAlign':'center'}),
                
                revenue_sign_flip
                
                
                
                
                ],
            
                   
            )  
        ]
    
    Markets_Revenue_Card_Content = [
        
        dbc.CardBody([
                html.Hr(style = {'height':'26px','color':'gray','background-color':'#702c94','width':'650px'}),
                dbc.Row([
               
                dbc.Col([
                html.H6('European Markets', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",EUROPE_Revenue_base,"B"), style = {'color':'#090059','textAlign':'center'}),

                EUROPE_revenue_sign_flip,
                ]),
                #North AMerica
                dbc.Col([
                html.H6('North American Markets', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",NorthAmerica_Revenue_base,"B"), style = {'color':'#090059','textAlign':'center'}),
              
                NorthAmerica_revenue_sign_flip
                ]),
                
                #Growth markets
                dbc.Col([
                html.H6('Growth Markets', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",GrowthMarkets_Revenue_base,"B"), style = {'color':'#090059','textAlign':'center'}),
              
                GrowthMarkets_revenue_sign_flip
                
                ])
                
                     ])
            ]),
            
        
        ]
    IndustryGroups_Card_Content = [
        
        dbc.CardBody([
                html.Hr(style = {'height':'26px','color':'gray','background-color':'#702c94','width':'650px'}),
                dbc.Row([
               
                dbc.Col([
                html.H6('Communication Media & Technology', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",COMM_MEDIA_TEC__Services_base,"B"), style = {'color':'#090059','textAlign':'center'}),

                COMM_MEDIA_TEC__Margin_sign_flip,
                ]),
                #Financial
                dbc.Col([
                html.H6('Financial Services', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",Financial_Services_base,"B"), style = {'color':'#090059','textAlign':'center'}),
              
                Financial_Margin_sign_flip
                ]),
                
                #Health
                dbc.Col([
                html.H6('Health & Public services', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",HEALTH_Services_base,"B"), style = {'color':'#090059','textAlign':'center'}),
              
                HEALTH_Margin_sign_flip
                
                ]),
                #Products
                dbc.Col([
                html.H6('Products', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",Products_Services_base,"B"), style = {'color':'#090059','textAlign':'center'}),
              
                Products_Margin_sign_flip
                
                ]),
                #Resources
                dbc.Col([
                html.H6('Resources', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",Resources_Services_base,"B"), style = {'color':'#090059','textAlign':'center'}),
              
                Resources_Margin_sign_flip
                
                ]),
                
                     ])
            ]),
            
        
        ]    
    
    EPS_Card_Content = [
        
        dbc.CardBody(
            
           
                
            [
                html.Hr(style = {'height':'26px','color':'gray','background-color':'#15479e','width':'150px'}),
                html.H6('EPS', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",EPS_base,""), style = {'color':'#090059','textAlign':'center'}),
                
                EPS_sign_flip
                
                
                
                
                ] ,
            
                
                  
            
                   
            )  
        
        ]
    #############OPS Card content
    OPS_Card_Content = [
        
        dbc.CardBody(
            
           
                
 [
                html.Hr(style = {'height':'26px','color':'gray','background-color':'#15479e','width':'150px'}),
                html.H6('EPS', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",Operating_Margin_base,"%"), style = {'color':'#090059','textAlign':'center'}),
                
                Operating_Margin_sign_flip
                
                
                
                
                ] ,    
                
                  
            
                   
            )  
        
        ]
    
    ############Strong free cash flow
    FreeCashFlow_Card_Content = [
        
        dbc.CardBody(
            
           
                
 [
                #html.Hr(style = {'height':'26px','color':'gray','background-color':'#15479e','width':'150px'}),
                html.H6('Strong free cash flow', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",Strong_free_Cashflow_Margin_base,"B"), style = {'color':'#090059','textAlign':'center'}),
                
                Strong_free_Cashflow_Margin_sign_flip
                
                
                
                
                ] ,    
                
                  
            
                   
            )  
        
        ]    
    
    ####### Share repurchases + Dividends paid
    ShareRepurchases_Card_Content = [
        
        dbc.CardBody(
            
           
                
 [
                #html.Hr(style = {'height':'26px','color':'gray','background-color':'#15479e','width':'150px'}),
                html.H6('Share Repurchases', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",Share_repurchases_Margin_base,"M"), style = {'color':'#090059','textAlign':'center'}),
                
                Share_repurchases_Margin_sign_flip
                
                
                
                
                ] ,    
                
                  
            
                   
            )  
        
        ]        
    
    ##Dividend paid
    Dividend_Card_Content = [
        
        dbc.CardBody(
            
           
                
 [
                #html.Hr(style = {'height':'26px','color':'gray','background-color':'#15479e','width':'150px'}),
                html.H6('Dividends paid', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",DIVIDEND_PAID__Margin_base,"M"), style = {'color':'#090059','textAlign':'center'}),
                
                DIVIDEND_PAID__Margin_sign_flip
                
                
                
                
                ] ,    
                
                  
            
                   
            )  
        
        ]          
    
    ##Quarterly Cash dividend in Jun 2021
    Quarterly_CashDividend_Content = [
        
        dbc.CardBody(
            
           
                
 [
                #html.Hr(style = {'height':'26px','color':'gray','background-color':'#15479e','width':'150px'}),
                html.H6('Dividends paid', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",Quarterly_Cash_dividend_base,"per share"), style = {'color':'#090059','textAlign':'center'}),
                
                Quarterly_Cash_dividend_sign_flip
                
                
                
                
                ] ,    
                
                  
            
                   
            )  
        
        ]          
        
    return Revenue_Card_Content,Markets_Revenue_Card_Content,Performance_card_Content,IndustryGroups_Card_Content,EPS_Card_Content,OPS_Card_Content,FreeCashFlow_Card_Content,ShareRepurchases_Card_Content,Dividend_Card_Content,Quarterly_CashDividend_Content

#html.Hr(style = {'height':'26px','color':'gray','background-color':'##15479e','width':'650px'})



if __name__ == "__main__":
    app.run_server()
    #debug = True

