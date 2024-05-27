import plotly.colors as colors
import dash_bootstrap_components as dbc
from Tabs.Tab1 import Tab1 
from Tabs.Tab2 import Tab2
from Tabs.Tab3 import Tab3
from Tabs.Tab4 import Tab4
from dash import html , dcc, Input,Output,State,callback
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
import plotly.express as px
from functions import *
from fuzzywuzzy import fuzz
from fuzzywuzzy import process




app = dash.Dash(__name__)

dash.register_page(__name__, path = '/Analytics', name = 'Analytics')

valuation = pd.read_excel('D:\All_data_science_project\DASH\IPL\Data\Team_Valuation.xlsx')
print(f"valuation{valuation}")
df1 = pd.read_csv('D:\All_data_science_project\DASH\IPL\Data\deliveries.csv')
df2 = pd.read_csv('D:\All_data_science_project\DASH\IPL\Data\matches.csv')
df2.rename(columns={'id': 'match_id'},inplace= True)
df2['date'] = pd.to_datetime(df2['date'])
df2['year'] = df2['date'].dt.year
df2['team1'] = df2['team1'].replace({'Rising Pune Supergiants': 'Rising Pune Supergiant'})
df2['team2'] = df2['team2'].replace({'Rising Pune Supergiants': 'Rising Pune Supergiant'})
df2 = df2.rename(columns={'id': 'match_id'})
df2['date'] = pd.to_datetime(df2['date'])

# Extract the year from the 'date' column
df2['year'] = df2['date'].dt.year

# Count the number of matches played by each team using unique match IDs
matches_played_by_team = pd.concat([df2.groupby('team1')['match_id'].nunique(), 
                                    df2.groupby('team2')['match_id'].nunique()]).groupby(level=0).sum()

print("Number of matches played by each team:")
matches_played_by_team = matches_played_by_team.reset_index()
matches_played_by_team = matches_played_by_team.rename(columns={'index': 'Team_name', 'match_id': 'match_played'})


#team wise wins 

team_wise_wins = df2['winner'].value_counts()

print("Team-wise winner count:")
team_wise_wins = team_wise_wins.reset_index()
team_wise_wins = team_wise_wins.rename(columns={'winner': 'Team_name', 'count': 'Number_of_times_wins'})

team_wise_wins



# create new df 

newdf = team_wise_wins.merge(matches_played_by_team,on = 'Team_name' , how='right')


# calculate winning percentage 
newdf['winning_percentage'] = (newdf['Number_of_times_wins']/newdf['match_played']) * 100
print(newdf)


#calculate number of sixes 
sixes_df = df1[df1['batsman_runs'] == 6]

# Count the number of sixes for each team
sixes_by_team = sixes_df['batting_team'].value_counts()

# Rename the columns
sixes_by_team = sixes_by_team.reset_index()
sixes_by_team = sixes_by_team.rename(columns={'count': 'Number_of_sixes', 'batting_team': 'Team_name'})

print("Number of sixes scored by each team:")
sixes_by_team

#calculate number of fours 

# Filter the dataset for rows where batsman_runs is 4
fours_by_team = df1[df1['batsman_runs'] == 4]

# Count the number of fours for each team
fours_by_team = fours_by_team['batting_team'].value_counts()

# Rename the columns
fours_by_team = fours_by_team.reset_index()
fours_by_team = fours_by_team.rename(columns={'count': 'Number_of_fours', 'batting_team': 'Team_name'})

print("Number of fours scored by each team:")
fours_by_team

#calculate total runs

total_runs_by_team = df1.groupby('batting_team')['total_runs'].sum().reset_index()

# Rename the columns
total_runs_by_team = total_runs_by_team.rename(columns={'batting_team': 'Team_name'})

print("Total runs for each team:")
(total_runs_by_team) 

merged_df = sixes_by_team.merge(newdf,on = 'Team_name' , how='right')
merged_df = fours_by_team.merge(merged_df,on='Team_name',how ='inner')
merged_df = total_runs_by_team.merge(merged_df,on = 'Team_name',how='inner')

print(merged_df)





# calculate wins per year 

# Convert 'date' column to datetime format
df2['date'] = pd.to_datetime(df2['date'])

# Extracting year from the 'date' column
df2['year'] = df2['date'].dt.year

# Grouping by year and winner, then counting the occurrences
yearly_team_wins = df2.groupby(['year', 'winner']).size().reset_index(name='wins')

print("Yearly wins by each team:")
print(yearly_team_wins)

# calculate nuber of sixes per year 

# Convert the 'date' column to datetime if it's not already in datetime format
Y = df1[['match_id','batsman_runs','batting_team']].merge(df2[['match_id','date']])

Y['date'] = pd.to_datetime(Y['date'])

# Group by 'batting_team', 'date' (year), and 'batsman_runs', then count the occurrences
Fours_per_team_per_year = Y[Y['batsman_runs'] == 4].groupby([Y['batting_team'], Y['date'].dt.year])['batsman_runs'].count().reset_index()

# Rename columns for clarity
Fours_per_team_per_year.columns = ['batting_team', 'year', 'number_of_fours']

# Display the result
print(Fours_per_team_per_year)





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

print("Yearly wins by each team with final winner indication:")
print(result)








row_1 = dbc.Row(
    [
       dbc.Col(
                    [
                        
                    ]
                    
                )
    ]
)


layout = dbc.Container(
    [
          
            
                  row_1 ,
                  dbc.Tabs([
                    
                    dbc.Tab(Tab1,label='Team'),
                    dbc.Tab(Tab2,label='Batsman')  ,
                    dbc.Tab(Tab3,label='Bowler') ,
                    

                  ])
              
          
           

    ], fluid=True, style={
                          'height':'1306px',
                          
                          
                          }
)


@callback(
    Output('year-over-runs', 'figure'),
    Output('year-over-wickets', 'figure'),
    Output('year-over-wins', 'figure'),

    [Input('Team-dropdown', 'value')]
)

def update_output(team):
    
    yearly_team_wins = df2.groupby(['year', 'winner']).size().reset_index(name='wins')

# Grouping to get the final winners
    finals_winners = df2[df2['match_type'] == 'Final'].groupby('year')['winner'].last().reset_index()

    # Merging the two DataFrames
    result = pd.merge(yearly_team_wins, finals_winners, on='year', how='left')

    # Renaming the columns
    result.rename(columns={'winner_x': 'winner', 'winner_y': 'final_winner'}, inplace=True)

    # Adding a column to indicate if a team won the final
    result['final_winner'] = result.apply(lambda row: 'Yes' if row['winner'] == row['final_winner'] else 'No', axis=1)

    print("Yearly wins by each team with final winner indication:")
    result
    result = result[result['winner']==team]
    print(result)
    
    


    df_filtered = df1[df1['batting_team'] == team]
    print('Filtered DataFrame:')
    
    df_filtered1 = df_filtered[['match_id','batting_team','total_runs']].merge(df2[['year','match_id']],on = 'match_id').groupby('year')['total_runs'].sum().reset_index()
    df_filtered2= df_filtered[['match_id','batting_team','is_wicket']].merge(df2[['year','match_id']],on = 'match_id').groupby('year')['is_wicket'].sum().reset_index()
    print(df_filtered2)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(df_filtered1) 
    x=update_plot_run(df_filtered1,team,'green')
    y = update_plot_wick(df_filtered2,team,'blue')
    z= update_bar_plot_change_color(result)
    return x,y ,z





@callback(
    Output('batsman-total-run', 'children'),
    Output('batsman-total-match', 'children'),
    Output('thirty_plus_runs', 'children'),
    Output('player-of-the-match','children'),
    Output('fifty_plus_runs','children'),
    Output('Hundred_plus_runs','children'),
    Output('Selected-batsman','children'),
    Output('Runs_per_over','figure'),
    Output('Dismissal','figure'),
    [Input('batter-dropdown', 'value')]
)
def update_df(selected_batter):
    unique_batters = df1['batter'].unique()
    batsman_dismissals = df1[df1['batter'] == selected_batter]['dismissal_kind'].value_counts()
    batsman_dismissals = batsman_dismissals.reset_index()

# Now, we will count the number of times each batter is named "player_of_match" in the original DataFrame
    player_of_match_counts = df2[df2['player_of_match'].isin(unique_batters)]['player_of_match'].value_counts()
    # if selected_batter is None:
    #     return "Please select a batter."
    
    # Get the count of player of the match awards for the selected batter
    count = player_of_match_counts.get(selected_batter, 0)
    #return f"{selected_batter} has been named Player of the Match {count} times."
    
    merged_df = df1.merge(df2[['date','match_id','year','player_of_match']],on = 'match_id',how ='inner')

    filtered_df = merged_df[merged_df['batter'] == selected_batter]

    xx = batsman_total_runs(filtered_df)
    zz =total_match(filtered_df)
    mm = thirty_plus_runs(filtered_df)
    yy = fifty_plus_runs(filtered_df)
    bb = hundered_plus_runs(filtered_df)
    cc = runs_by_over_for_batsman(filtered_df)
    dd = DismissalType(batsman_dismissals)
    
    return xx,zz,mm,count,yy,bb,f"{selected_batter}",cc,dd






@callback(
     Output('bowler-total-wickets', 'children'),
     Output('bowler-total-match', 'children'),
     #Output('Wickets 3+', 'children'),
     Output('bowler-player-of-the-match','children'),
#     Output('fifty_plus_runs','children'),
     Output('Avg Extra','children'),
     Output('Selected-bowler','children'),
#     Output('Runs_per_over','figure'),
#     Output('Dismissal','figure'),
     [Input('bowler-dropdown', 'value')]
 )
def update_df2(selected_bowler):
    merged_df = df1.merge(df2[['date','match_id','year','player_of_match']],on = 'match_id',how ='inner')
    unique_bowlers = merged_df['bowler'].unique()
    filtered_df = merged_df[merged_df['bowler'] == selected_bowler]
    #batsman_dismissals = df1[df1['batter'] == selected_batter]['dismissal_kind'].value_counts()
    #batsman_dismissals = batsman_dismissals.reset_index()
   
# Now, we will count the number of times each batter is named "player_of_match" in the original DataFrame
    player_of_match_counts = df2[df2['player_of_match'].isin(unique_bowlers)]['player_of_match'].value_counts()
    
    count = player_of_match_counts.get(selected_bowler, 0)
    
    bowler_df=bowler_stat[bowler_stat['bowler']==selected_bowler]
    x = bowler_total_wickets(bowler_df)
    y = bowler_total_match(bowler_df)
    z = round(bowler_df['extra_runs']/bowler_df['matches_played'],1)

    return x , y, count ,z,f"{selected_bowler}"

@callback(
#     Output('bowler-total-wickets', 'children'),
#     Output('bowler-total-match', 'children'),
     Output('Wickets 3+', 'children'),
     Output('Total 5 wickets','children'),
#     Output('fifty_plus_runs','children'),
#     Output('Hundred_plus_runs','children'),
#     Output('Selected-batsman','children'),
      Output('runs_concede_per_over','figure'),
      Output('wickets-per-year-over','figure'),
     [Input('bowler-dropdown', 'value')]
 )

def update_df3(selected_bowler):
    merged_df = df1.merge(df2[['date','match_id','year','player_of_match']],on = 'match_id',how ='inner')
    #unique_bowlers = merged_df['bowler'].unique()
    filtered_df = merged_df[merged_df['bowler'] == selected_bowler]
    runs_per_over = filtered_df.groupby('over')['total_runs'].sum().reset_index()
    print("????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
    print(filtered_df)

    z = three_plus_wickets(filtered_df)
    zz = five_wickets(filtered_df)
    zzz = runs_per_over_concede_by_bowler(runs_per_over)
    w = runs_and_wickets_per_over(filtered_df)
    return z.shape[0] ,zz.shape[0] , zzz,w 

    #batsman_dismissals = df1[df1['batter'] == selected_batter]['dismissal_kind'].value_counts()
    #batsman_dismissals = batsman_dismissals.reset_index()
   
# Now, we will count the number of times each batter is named "player_of_match" in the original DataFrame

    


    