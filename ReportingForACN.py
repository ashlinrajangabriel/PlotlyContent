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






xls = pd.ExcelFile(r'C:\Users\Asus\Desktop\PersonalResearch\(***)\Data\ACNReporting.xlsx')
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
             dbc.Col([dbc.Card(id = 'card_num1',style={'height':'150px'})]),
             dbc.Col([dbc.Card(id = 'card_num2',style={'height':'150px'})]),
             dbc.Col([dbc.Card(id = 'card_num3',style={'height':'150px'})]),
             
             ]) ,
    html.Br(),
    html.Br(),             
    dbc.Row([
             dbc.Col([dbc.Card(id = 'Accenture_Total_Revenue_Card',style={'height':'200px','width':'190px'})]),
             dbc.Col([dbc.Card(id = 'card_num5',style={'height':'150px'})]),
             dbc.Col([dbc.Card(id = 'card_num6',style={'height':'150px'})]),
             
             ]) 
             ],

             style = {'backgroundColor':'#f7f7f7'},
             fluid = True)

       
    


app.layout = html.Div(id='parent', children = [navbar,body_app])


#Lets create callback

@app.callback([
                Output('Accenture_Total_Revenue_Card','children')
              ],
                [Input('dropdown_Quarter_base','value'),
                 Input('dropdown_Quarter_Comparison','value')])

def update_cards(base,comparison):
    Revenue_base = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == base)  ].groupby(['Fiscal Year','Quarter','Q1FY21 Performance','Format','Currency']).agg({'Revenues and Growth in Local Currency':'sum'}).reset_index()['Revenues and Growth in Local Currency'][0].round(2)
    Revenue_comp = GeoMarketsRevenue[ (GeoMarketsRevenue['Quarter'] == comparison)  ].groupby(['Fiscal Year','Quarter','Q1FY21 Performance','Format','Currency']).agg({'Revenues and Growth in Local Currency':'sum'}).reset_index()['Revenues and Growth in Local Currency'][0].round(2)
    diff = np.round(Revenue_base - Revenue_comp,2)
    Total_Revenue_Content = [
        
        dbc.CardBody(
            [
                html.Hr(style = {'height':'26px','color':'gray','background-color':'#702c94','width':'150px'}),
                html.H6('Total Revenue', style = {'font':'light','textAlign':'center'}),
                html.H3('{0}{1}{2}'.format("$",Revenue_base,"B"), style = {'color':'#090059','textAlign':'center'}),
                
                dcc.Markdown( 
                    dangerously_allow_html = True, 
                    children = ["<sub>+{0}{1}{2}</sub>".format('$',diff,'M')], style = {'textAlign':'center'})
                
                ]
                   
            )  
        ]
    return Total_Revenue_Content





if __name__ == "__main__":
    app.run_server()
    #debug = True

