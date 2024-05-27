

import dash
from dash import html, dcc,Input,Output,State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import dash
#import dash_canvas
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd 
import dash_table
import requests
import numpy as np
import plotly.colors as colors
#from Tabs import Tab1,Tab2,Tab3
import sys
from pathlib import Path
import sys
from pathlib  import Path
# from page1_function import * 
# from data_import import *
import dash
from dash import html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd
# from graph import *
from datetime import datetime
from functions import *
import dash_ag_grid as ag
dash.register_page(__name__,path = '/',name ='Home')





df4 = pd.read_csv('D:\All_data_science_project\DASH\IPL\Data\Geocoding.csv')
df3 =pd.read_csv('D:\All_data_science_project\DASH\IPL\Data\stadium.csv')
#print(df3)
df4.rename(columns={'Address': 'Stadium'},inplace=True)
df=df3.merge(df4,on = 'Stadium',how = 'inner')

#print('#########################################')

#print(df)


#Extract latitude and longitude
df[['Latitude', 'Longitude']] = df['Coordinates'].str.split(',', expand=True)

# # Convert longitude to float
df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')

try:
  # Assuming 'Latitude' mostly contains numeric values
  df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
except:
  # If conversion fails, handle the error (e.g., print a message)
  print("Error converting Latitude to numeric")

# # Now 'Latitude' should be of type float
#print(df['Latitude'].dtype)

















row_1 = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                               dbc.Row([
                                 dbc.Col(
                                   [
                                     html.H4("Total Match Conducted",style = {'text-align':'center','margin-top':'10px'})
                                   ],style = {'height':'30px'}
                                 )
                               ]),
                               dbc.Row([
                                 dbc.Col(
                                   [
                                     html.H1(mm,style = {'text-align':'center','margin-top':'50px'})
                                   ],style = {'height':'200px','backgroundColor':'white','margin-top':'20px','border-radius':'10px','border': '1px solid black'}
                                 )
                               ])
                            ],width = 6,style = {'height':'250px','backgroundColor':'white'}
                        ),
                        dbc.Col(
                            [
                                dbc.Row([
                                 dbc.Col(
                                   [
                                     html.H4("Total City ",style = {'text-align':'center','margin-top':'10px'})
                                   ],style = {'height':'30px'}
                                 )
                               ]),
                               dbc.Row([
                                 dbc.Col(
                                   [
                                     html.H1("36",style = {'text-align':'center','margin-top':'50px'})
                                   ],style = {'height':'200px','backgroundColor':'white','margin-top':'20px','border-radius':'10px','border': '1px solid black','margin-left':'2px'}
                                 )
                               ])
                            ],width = 6,style = {'height':'250px','backgroundColor':'white'}
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                    dbc.Row([
                                 dbc.Col(
                                   [
                                     html.H4("Total Stadium",style = {'text-align':'center','margin-top':'10px'})
                                   ],style = {'height':'30px'}
                                 )
                               ]),
                               dbc.Row([
                                 dbc.Col(
                                   [
                                     html.H1("39",style = {'text-align':'center','margin-top':'50px'})
                                   ],style = {'height':'200px','backgroundColor':'white','margin-top':'20px','border-radius':'10px','border': '1px solid black'}
                                 )
                               ])
                            ],width = 6,style = {'height':'250px','backgroundColor':'white'}
                        ),
                        dbc.Col(
                            [
                               dbc.Row([
                                 dbc.Col(
                                   [
                                     html.H4("Total Player",style = {'text-align':'center','margin-top':'10px'})
                                   ],style = {'height':'30px'}
                                 )
                               ]),
                               dbc.Row([
                                 dbc.Col(
                                   [
                                     html.H1(694,style = {'text-align':'center','margin-top':'50px'})
                                   ],style = {'height':'200px','backgroundColor':'white','margin-top':'20px','border-radius':'10px','border': '1px solid black','margin-left':'2px'}
                                 )
                               ])     
                            ],width = 6,style = {'height':'250px','backgroundColor':'white'}
                        )
                    ]
                )
            ],width = 4,style = {'height':'500px','backgroundColor':'yellow'}
        ),
        dbc.Col(
            [
                dcc.Graph('stadium-scatter-mapbox',figure= mapbox(),style ={'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)','margin-top':'20px'})
            ],style = {'margin-top':'10px','boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'}
        )
    ],style = {'backgroundColor':'white'}
)


row_2 = dbc.Row(
  [
    dbc.Col(
      [
         dbc.Row(
           [
             dbc.Col(
               [
    #              ag.AgGrid(
    #                               style={"height": 500, "width": 300},
    #     id='datatable',
    #     columnDefs=[
    #         {"headerName": i, "field": i} for i in highest_runs_per_stadium.reset_index().columns
    #     ],
    #     rowData=highest_runs_per_stadium.reset_index().to_dict('records'),
    #     #rowSelection='multiple',
    #     #paginationPageSize=10,
    #     #domLayout='autoHeight',
    #     #suppressMenuHide=True,
    # )      
                dbc.Row(
                  [
                    dbc.Col(
                      [
                        html.H5('Highest Runs In Each Stadium')
                      ],style = {'height':'40px','margin-top':'30px'}
                    )
                  ]
                ),
                dbc.Row(
                  [
                    dbc.Col(
                      [
                                      ag.AgGrid(
                                  style={"height": 350, "width": 300},
        id='datatable',
        columnDefs=[
            {"headerName": i, "field": i} for i in highest_runs_per_stadium.reset_index().columns
        ],
        rowData=highest_runs_per_stadium.reset_index().to_dict('records'),
        #rowSelection='multiple',
        #paginationPageSize=10,
        #domLayout='autoHeight',
        #suppressMenuHide=True,
    )  
                      ],style = {'height':'400px'}
                    )
                  ]
                ),
                


               ],width = 2,style = {'height':'410px','backgroundColor':'white'}
             ),
             dbc.Col(
               [
                 dcc.Graph('Total-runs-each-year-in-ipl',figure = total_ipl_run())
               ]
             )
           ]
         ),
         dbc.Row(
           [
             dbc.Col(
               [
                 dbc.Row(
                  [
                    dbc.Col(
                      [
                        html.H5('Matches Played In each Stadium',style ={'margin-top':'40px'})
                      ],style = {'height':'40px','margin-top':'30px'}
                    )
                  ]
                ),
                dbc.Row(
                  [
                    dbc.Col(
                      [
                                      ag.AgGrid(
                                  style={"height": 350, "width": 300},
        id='datatable',
        columnDefs=[
            {"headerName": i, "field": i} for i in matches_per_stadium.columns
        ],
        rowData=matches_per_stadium.to_dict('records'),
        #rowSelection='multiple',
        #paginationPageSize=10,
        #domLayout='autoHeight',
        #suppressMenuHide=True,
    )  
                      ],width = 2 ,style = {'height':'400px','margin-top':'50px'}
                    ),
                    dbc.Col(
                      [
                        dcc.Graph('Total-runs-each-year-in-ipl',figure = total_ipl_wickets())
                      ],style = {'height':'500px','backgroundColor':'white'}
                    )
                  ]
                )

               ],style = {'backgroundColor':'white'}
             )
           ]
         )
      ],style = {'height':'410px','backgroundColor':'white'}
    ),
    
  ]
)


layout = dbc.Container(
    [
         row_1   ,
         row_2

    ], fluid=True, style={
                          'height':'1700px','backgroundColor':'white',
                          'border':'1px solid white'
                          
                          
                          }
)
