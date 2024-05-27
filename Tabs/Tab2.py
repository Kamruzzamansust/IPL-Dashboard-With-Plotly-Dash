import plotly.colors as colors
import dash_bootstrap_components as dbc
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
# from page2_function import card2 ,married_count , unmarried_count , owner, not_owner ,male,female
import plotly.colors as colors
import dash_bootstrap_components as dbc
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
import dash_table
# from page2_function import card2 ,married_count , unmarried_count , owner, not_owner ,male,female
import plotly.express as px
import plotly.colors as colors
import dash_bootstrap_components as dbc
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
# from page2_function import card2 ,married_count , unmarried_count , owner, not_owner ,male,female
from functions import * 
import dash_table
import os 
from PIL import Image
import plotly.express as px
import dash_ag_grid as ag
import openpyxl
from fuzzywuzzy import fuzz













unique_batters = df1['batter'].unique()






Tab2 =dbc.Row(
    dbc.Col(
        [
            dbc.Row(
                [   
                    dbc.Col(
                        [
                            html.H5('All Batsamn Stat',style  = {'text-align':'center'})
                        ],style = {'height':'30px'}
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Col(
                        [
                            ag.AgGrid(
                                  style={"height": 570, "width": 1670},
        id='datatable',
        columnDefs=[
            {"headerName": i, "field": i} for i in batsman_stat.columns
        ],
        rowData=batsman_stat.to_dict('records'),
        defaultColDef={"filter": "agTextColumnFilter"},
        #rowSelection='multiple',
        #paginationPageSize=10,
        #domLayout='autoHeight',
        #suppressMenuHide=True,
    )
                        ],style = {'padding-left':'100px',"height": '570px','backgroundColor':'white'}
                    )
                        ]
                    )
                ]
            ),
            dbc.Row(
    [
        dbc.Col(
            [
                dcc.Dropdown(id='batter-dropdown',
                              
                              
                              options=[{'label': batter, 'value': batter} for batter in unique_batters],)
            ],style = {'height':'50px','backgroundColor':'white','margin-top':'20px'}
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
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                              html.H5('Total Runs',style = {'text-align':'center'})
                                          ],style = {'height':'50px','backgroundColor':'white','border':'1px solid black'}
                                      )
                                  ]
                              ),
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                             html.Div(id='batsman-total-run',style={'font-size': '60px', 'font-weight': 'bold','margin-top':'20px','text-align':'center'})
                                          ],style = {'height':'250px','backgroundColor':'white','border-radius':'5px','border':'2px solid black'}
                                      )
                                  ]
                              ),
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                               html.H5('Match played',style = {'text-align':'center'})
                                          ],style = {'height':'50px','backgroundColor':'white','border':'1px solid black'}
                                      )
                                  ]
                              ),
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                              html.Div(id='batsman-total-match',style={'font-size': '60px', 'font-weight': 'bold','margin-top':'20px','text-align':'center'})

                                          ],style = {'height':'250px','backgroundColor':'white','border-radius':'5px','border':'2px solid black'}
                                      )
                                  ]
                              ),
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                               html.H5('Man Of the Match',style = {'text-align':'center'})
                                          ],style = {'height':'50px','backgroundColor':'white','border':'1px solid black'}
                                      )
                                  ]
                              ),
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                              html.Div(id='player-of-the-match',style={'font-size': '60px', 'font-weight': 'bold','margin-top':'20px','text-align':'center'})
                                          ],style = {'height':'250px','backgroundColor':'white','border-radius':'5px','border':'2px solid black'}
                                      )
                                  ]
                              ),

                          ],
                      )
                  ]
              )  
            ],width = 1,style = {'height':'1000px','backgroundColor':'white'}
        ),
        dbc.Col(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                              html.Div(id='Selected-batsman',style={'font-size': '60px', 'font-weight': 'bold','margin-top':'20px','text-align':'center'})
                            ],style = {'height':'150px','backgroundColor':'white'}
                        )
                        
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                               dcc.Graph('Runs_per_over',figure = {},style = {'height':'360px'})
                            ],style = {'height':'370px','backgroundColor':'white'}
                        )
                        
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                              dcc.Graph('Dismissal',figure = {},style = {'height':'360px'})
                            ],style = {'height':'370px','backgroundColor':'white'}
                        )
                        
                    ]
                )
            ],width = 10,style = {'height':'800px','backgroundColor':'white'}
        ),
         dbc.Col(
            [
                   dbc.Row(
                  [
                      dbc.Col(
                          [
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                              html.H5('30 +',style = {'text-align':'center'})
                                          ],style = {'height':'50px','backgroundColor':'white','border':'1px solid black'}
                                      )
                                  ]
                              ),
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                              html.Div(id='thirty_plus_runs',style={'font-size': '60px', 'font-weight': 'bold','margin-top':'20px','text-align':'center'})
                                          ],style = {'height':'250px','backgroundColor':'white','border-radius':'5px','border':'2px solid black'}
                                      )
                                  ]
                              ),
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                              html.H5('Total IPL 100',style = {'text-align':'center'})
                                          ],style = {'height':'50px','backgroundColor':'white','border':'1px solid black'}
                                      )
                                  ]
                              ),
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                              html.Div(id='Hundred_plus_runs',style={'font-size': '60px', 'font-weight': 'bold','margin-top':'20px','text-align':'center'})
                                          ],style = {'height':'250px','backgroundColor':'white','border-radius':'5px','border':'2px solid black'}
                                      )
                                  ]
                              ),
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                              html.H5('Total 50',style = {'text-align':'center'})
                                          ],style = {'height':'50px','backgroundColor':'white','border':'1px solid black'}
                                      )
                                  ]
                              ),
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                             html.Div(id='fifty_plus_runs',style={'font-size': '60px', 'font-weight': 'bold','margin-top':'20px','text-align':'center'}) 
                                          ],style = {'height':'250px','backgroundColor':'white','border-radius':'5px','border':'2px solid black'}
                                      )
                                  ]
                              ),

                          ],
                      )
                  ]
              )   
            ],width = 1,style = {'height':'1000px','backgroundColor':'white'}
        ),
       
    ],style = {'marggin-top':'40px'}
)
            
        ]
    )
)



