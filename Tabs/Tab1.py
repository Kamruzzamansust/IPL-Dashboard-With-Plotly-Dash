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

valuation = pd.read_excel('D:\All_data_science_project\DASH\IPL\Data\Team_Valuation.xlsx')
#print(f"valuation{valuation}")
df1 = pd.read_csv('D:\All_data_science_project\DASH\IPL\Data\deliveries.csv')
df2 = pd.read_csv('D:\All_data_science_project\DASH\IPL\Data\matches.csv')
df2.rename(columns={'id': 'match_id'},inplace= True)
df2['date'] = pd.to_datetime(df2['date'])
df2['year'] = df2['date'].dt.year
df2['team1'] = df2['team1'].replace({'Rising Pune Supergiants': 'Rising Pune Supergiant'})
df2['team2'] = df2['team2'].replace({'Rising Pune Supergiants': 'Rising Pune Supergiant'})

# Count the number of matches played by each team using unique match IDs
matches_played_by_team = pd.concat([df2.groupby('team1')['match_id'].nunique(), 
                                    df2.groupby('team2')['match_id'].nunique()]).groupby(level=0).sum()

#print("Number of matches played by each team:")
matches_played_by_team = matches_played_by_team.reset_index()
matches_played_by_team = matches_played_by_team.rename(columns={'index': 'Team_name', 'match_id': 'match_played'})


#team wise wins 

team_wise_wins = df2['winner'].value_counts()

#print("Team-wise winner count:")
team_wise_wins = team_wise_wins.reset_index()
team_wise_wins = team_wise_wins.rename(columns={'winner': 'Team_name', 'count': 'Number_of_times_wins'})

team_wise_wins



# create new df 

newdf = team_wise_wins.merge(matches_played_by_team,on = 'Team_name' , how='right')


# calculate winning percentage 
newdf['winning_percentage'] = (newdf['Number_of_times_wins']/newdf['match_played']) * 100
#print(newdf)


#calculate number of sixes 
sixes_df = df1[df1['batsman_runs'] == 6]

# Count the number of sixes for each team
sixes_by_team = sixes_df['batting_team'].value_counts()

# Rename the columns
sixes_by_team = sixes_by_team.reset_index()
sixes_by_team = sixes_by_team.rename(columns={'count': 'Number_of_sixes', 'batting_team': 'Team_name'})

#print("Number of sixes scored by each team:")
sixes_by_team

#calculate number of fours 

# Filter the dataset for rows where batsman_runs is 4
fours_by_team = df1[df1['batsman_runs'] == 4]

# Count the number of fours for each team
fours_by_team = fours_by_team['batting_team'].value_counts()

# Rename the columns
fours_by_team = fours_by_team.reset_index()
fours_by_team = fours_by_team.rename(columns={'count': 'Number_of_fours', 'batting_team': 'Team_name'})

#print("Number of fours scored by each team:")
fours_by_team

#calculate total runs

total_runs_by_team = df1.groupby('batting_team')['total_runs'].sum().reset_index()

# Rename the columns
total_runs_by_team = total_runs_by_team.rename(columns={'batting_team': 'Team_name'})

#print("Total runs for each team:")
(total_runs_by_team) 

merged_df = sixes_by_team.merge(newdf,on = 'Team_name' , how='right')
merged_df = fours_by_team.merge(merged_df,on='Team_name',how ='inner')
merged_df = total_runs_by_team.merge(merged_df,on = 'Team_name',how='inner')

#print(merged_df)





# calculate wins per year 

# Convert 'date' column to datetime format
df2['date'] = pd.to_datetime(df2['date'])

# Extracting year from the 'date' column
df2['year'] = df2['date'].dt.year

# Grouping by year and winner, then counting the occurrences
yearly_team_wins = df2.groupby(['year', 'winner']).size().reset_index(name='wins')

#print("Yearly wins by each team:")
#print(yearly_team_wins)

# calculate nuber of sixes per year 

# Convert the 'date' column to datetime if it's not already in datetime format
Y = df1[['match_id','batsman_runs','batting_team']].merge(df2[['match_id','date']])

Y['date'] = pd.to_datetime(Y['date'])

# Group by 'batting_team', 'date' (year), and 'batsman_runs', then count the occurrences
Fours_per_team_per_year = Y[Y['batsman_runs'] == 4].groupby([Y['batting_team'], Y['date'].dt.year])['batsman_runs'].count().reset_index()

# Rename columns for clarity
Fours_per_team_per_year.columns = ['batting_team', 'year', 'number_of_fours']

# Display the result
#print(Fours_per_team_per_year)





#yes no 

# Grouping by year and winner, then counting the occurrences
yearly_team_wins = df2.groupby(['year', 'winner']).size().reset_index(name='wins')

# Grouping to get the final winners
finals_winners = df2[df2['match_type'] == 'Final'].groupby('year')['winner'].last().reset_index()

# Merging the two DataFrames
result = pd.merge(yearly_team_wins, finals_winners, on='year', how='left')

# Renaming the columns
result.rename(columns={'winner_x': 'winner', 'winner_y': 'final_winner'}, inplace=True)

# Adding a column to indicate if a team won the final
result['final_winner'] = result.apply(lambda row: 'Yes' if row['winner'] == row['final_winner'] else 'No', axis=1)

#print("Yearly wins by each team with final winner indication:")
#print(result)

























image_directory = r'D:\All_data_science_project\DASH\IPL\asset'  # Assuming the asset folder is in the same directory

image_urls = [
    "ipl1.webp",
    "ipl2.webp",
    "img3.jpg",
    "d1.webp",
    "d2.webp",
    "d3.webp",

    "ipl4.jpg",

    #img3.jpeg"
]

data = []
for image_file in image_urls:
    file_path = os.path.join(image_directory, image_file)  # Construct full path
    img = Image.open(file_path)
    img=img.resize((270, 125),Image.LANCZOS)
    data.append(img)

image_urls2 = [
    "chennai.png",
    "mumbai.png",
    "kkr.png",
    "rr.png",
    
    # "d2.webp",
    # "d3.webp",
     'logo.png'
    #img3.jpeg"
]

data2 = []
for image_file in image_urls2:
    file_path = os.path.join(image_directory, image_file)  # Construct full path
    img = Image.open(file_path)
    img=img.resize((270, 125),Image.LANCZOS)
    data2.append(img)





Tab1 =  dbc.Row(
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
                                          card2('Total Team',df2)                
                                     ],style = {'backgroundColor':'','height':'270px'}
                                 ),
                                
                             ]
                         ),
                         dbc.Row(
                             [
                                                       dbc.Col(
                   [
                        dbc.Carousel(
    items=[
        {"key": "3", "src": data[2]},
        {"key": "1", "src": data[0]},
        {"key": "2", "src": data[1]},
        
        {"key": "6", "src": data[6]},
        {"key": "4", "src": data[3]},
        {"key": "5", "src": data[5]},
        
        
    

       
    ],
    controls=True,
    indicators=True,
    slide = True,
    interval=1500

)
                   ], width =6 ,style = {'backgroundColor':'white','height':'270px','boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'}
               ),
               dbc.Col(
                   [
                        dbc.Carousel(
    items=[
        {"key": "1", "src": data2[0]},
        {"key": "2", "src": data2[1]},
        
        {"key": "3", "src": data2[3]},
        {"key": "3", "src": data2[2]},


       
    ],
    controls=True,
    indicators=True,
    slide = True,
    interval=1500

)
                   ], width =6 ,style = {'backgroundColor':'white','height':'270px','boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'}
               ),

                             ]
                         )
                          ],width = 8 
                      ),
                      dbc.Col(
                          [
                              dbc.Row([
                                  dbc.Col([
                                      success(df2)
                                  ])
                              ]),
                              dbc.Row(
                                  [
                                      dbc.Col(
                                          [
                                              ag.AgGrid(
                                  style={"height": 270, "width": 570},
        id='datatable',
        columnDefs=[
            {"headerName": i, "field": i} for i in valuation.columns
        ],
        rowData=valuation.to_dict('records'),
        #rowSelection='multiple',
        #paginationPageSize=10,
        #domLayout='autoHeight',
        #suppressMenuHide=True,
    )
                                          ],style = {'margin-top':'5px'}
                                      )
                                  ]
                              )
                              

                          ],width = 4,style = {'backgroundColor':'white','height':'268px'}
                      )
                  ] #success(df2)
              ),
              dbc.Row(
                  [
                      dbc.Col(
                          [
                              ag.AgGrid(
                                  style={"height": 400, "width": 1240},
        id='datatable',
        columnDefs=[
            {"headerName": i, "field": i} for i in merged_df.columns
        ],
        rowData=merged_df.to_dict('records'),
        #rowSelection='multiple',
        #paginationPageSize=10,
        #domLayout='autoHeight',
        #suppressMenuHide=True,
    )
                          ] ,width = 8,style = {'height':'358px','margin-top':'20px'}
                      ),
                      dbc.Col(
                          [
                              html.Div([
    html.H1("Indian Premier League (IPL)"),
    html.P("The Indian Premier League (IPL), also known as the TATA IPL for sponsorship reasons, is a men's Twenty20 (T20) cricket league held annually in India. Founded by the BCCI in 2007, the league features ten city-based franchise teams. The IPL usually takes place during the summer, between March and May each year."),
     html.Img(src=data2[4], style={'width': '510px'})
])
                          ],style =  {'margin-top':'10px'}
                      )
                  ]
              ),
              dbc.Row(
                  [
                      dbc.Col(
                          [
                              dcc.Dropdown(
        id='Team-dropdown',
        options=[{'label': Team, 'value': Team} for Team in df2['team1'].unique()],
        value= df2['team1'].unique()[0] # Set initial selected value (optional)
    )
                          ],style =  {'margin-top':'10px','height':'40px'}
                      ),
                      dbc.Col(
                          [
    #                          dcc.Dropdown(
    #     id='year-dropdown',
    #     options=[{'label': year, 'value': year} for year in df2['year'].unique()],
    #     value=df2['year'].unique()[0] # Set the initial value
    # ),
                          ],style =  {'margin-top':'10px','height':'40px'}
                      ),

                  ]
              ),
              dbc.Row(
                  [
                      dbc.Col(
                          [
                              dcc.Graph('year-over-runs',figure = {})
                          ]
                      ),
                      dbc.Col(
                          [
                              dcc.Graph('year-over-wickets',figure = {})
                          ]
                      )
                  ]
              ),
              dbc.Row(
                  [
                      dbc.Col(
                          [
                              dcc.Graph('year-over-wins',figure = {})
                          ]
                      )
                  ]
              )

            ],style = {'height':'2000px','backgroundColor':'white','boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'}
        )
    ]
)
