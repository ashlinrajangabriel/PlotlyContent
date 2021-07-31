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


#IndustryGroups
################################ Financial Services#####################################
Financial_Services =IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Financial Services')  & (IndustryGroupsRevenue['Quarter'] == 'Q3' ) ]

#Q2Fins=IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Financial Services')  & (IndustryGroupsRevenue['Quarter'] == 'Q2' ) ]
#Q3Fins=IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Financial Services')  & (IndustryGroupsRevenue['Quarter'] == 'Q3' ) ]

##############################Communications, Media & Technology #######################
Communications_Media_Technology =IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Communications, Media & Technology')  & (IndustryGroupsRevenue['Quarter'] == 'Q3' ) ]


###############################Health and public services ##############################
Health_public_services =IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Health and public services')  & (IndustryGroupsRevenue['Quarter'] == 'Q3' ) ]

######################################Products##########################################

Products =IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Products')  & (IndustryGroupsRevenue['Quarter'] == 'Q3' ) ]

######################################Products##########################################

Resources =IndustryGroupsRevenue[ (IndustryGroupsRevenue['Industry Groups'] == 'Resources')  & (IndustryGroupsRevenue['Quarter'] == 'Q3' ) ]


########################################EPS 
EPSGAAPAdjusted
EPS =EPSGAAPAdjusted[ (EPSGAAPAdjusted['Quarter'] == 'Q3' ) & (EPSGAAPAdjusted['EPS (GAAP)'].notnull() )]

EPS = EPS[(['Fiscal Year', 'Quarter', 'EPS (GAAP)','Currency'])]

########################################Operating Margin

OperatingMargin = EPSGAAPAdjusted[ (EPSGAAPAdjusted['Quarter'] == 'Q3' ) & (EPSGAAPAdjusted['Component'] == 'Operating Margin'  )]
OperatingMargin = OperatingMargin[(['Fiscal Year', 'Quarter', 'Component','Scale','Amount'])]


########################################################################################################
###########################################################Returning to cash to shareholders
#Strong free cash flow



#Share repurchases


#Quarterly cash dividend declared



#Dividends paid

###############################################################################################################
#SERVICES
########################################## TABLE
EPSGAAPAdjusted[ (EPSGAAPAdjusted['Quarter'] == 'Q3' ) & (EPSGAAPAdjusted['Component'] == 'Operating Margin'  )]

#Highlights of Strategic Priorities #Type of Growth

Highlights_of_Strategic_Priorities = EPSGAAPAdjusted[ (EPSGAAPAdjusted['Quarter'] == 'Q3' ) & (EPSGAAPAdjusted['Highlights of Strategic Priorities'].notnull() )]
Highlights_of_Strategic_Priorities = Highlights_of_Strategic_Priorities[(['Fiscal Year', 'Quarter','Highlights of Strategic Priorities', 'Type of Growth'])]

#Highlights of Revenue Growth by Services #Type of Growth
Highlights_of_RevenueGrowthByServices = EPSGAAPAdjusted[ (EPSGAAPAdjusted['Quarter'] == 'Q3' ) & (EPSGAAPAdjusted['Highlights of Revenue Growth by Services'].notnull() )]
Highlights_of_RevenueGrowthByServices = Highlights_of_RevenueGrowthByServices[(['Fiscal Year', 'Quarter','Highlights of Revenue Growth by Services', 'Type of Growth'])]

#NEW BOOKINGS

New_Bookings = EPSGAAPAdjusted[ (EPSGAAPAdjusted['Quarter'] == 'Q3' ) & (EPSGAAPAdjusted['Component'] == 'New Bookings'  )]
New_Bookings = New_Bookings[(['Fiscal Year', 'Quarter', 'Component','Scale','Amount'])]


####################################END OF Q3


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
    html.Hr(style = {'height':'25px','color':'gray','background-color':'#15479e','width':'100%'}),
    
    #Eps & Returning Cash to shareholders.
    dbc.Row([
    
    #EPS Card Operating Margin
    dbc.Row([
             dbc.Col([dbc.Card(id = 'EPS_Card',style={'height':'190px','width':'190px'})]),
             dbc.Col([dbc.Card(id = 'OperatingMarginCard',style={'height':'190px'})]),
             #bc.Col([dbc.Card(id = 'card_num6',style={'height':'150px'})]),
             #html.Hr(style = {'height':'26px','color':'gray','background-color':'##15479e','width':'650px'})
             
             ]) ,
    #EPS Card Operating Margin
    dbc.Row([
             dbc.Col([dbc.Card(id = 'Strong_Free_cashflow',style={'height':'190px','width':'190px'})]),
             dbc.Col(
                 [dbc.Card(id = 'Share_Repurchases',style={'height':'190px'})],
                 #[dbc.Card(id = 'dividends_paid',style={'height':'190px'})]
                 
                 
                 ),
             dbc.Col([dbc.Card(id = 'Quarterly cash dividend',style={'height':'190px','width':'190px'})]),
             #bc.Col([dbc.Card(id = 'card_num6',style={'height':'150px'})]),
             #html.Hr(style = {'height':'26px','color':'gray','background-color':'##15479e','width':'650px'})
             
             ]) ,    
    
    
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
    
    return Revenue_Card_Content,Markets_Revenue_Card_Content,Performance_card_Content

#html.Hr(style = {'height':'26px','color':'gray','background-color':'##15479e','width':'650px'})


if __name__ == "__main__":
    app.run_server()
    #debug = True

