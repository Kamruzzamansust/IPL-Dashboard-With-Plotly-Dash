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
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



batsman_stat = pd.read_csv(r"D:\All_data_science_project\DASH\IPL\Data\batsman_stat.csv")
bowler_stat = pd.read_csv(r'D:\All_data_science_project\DASH\IPL\experiments\bowler_stat.csv')

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









def bowler_total_wickets(filtered_df):
     
     return filtered_df['wickets'].values

def bowler_total_match(filtered_df):
     return filtered_df['matches_played'].values

def three_plus_wickets(filtered_df):
    # Group by match_id and bowler, then sum the is_wicket column
    wickets_per_match = filtered_df.groupby(['match_id', 'bowler'])['is_wicket'].sum().reset_index()
    
    # Filter the groups where wickets are 3 or more
    matches_with_3_or_more_wickets = wickets_per_match[wickets_per_match['is_wicket'] >= 3]
    
    return matches_with_3_or_more_wickets
def five_wickets(filtered_df):
    # Group by match_id and bowler, then sum the is_wicket column
    wickets_per_match = filtered_df.groupby(['match_id', 'bowler'])['is_wicket'].sum().reset_index()
    
    # Filter the groups where wickets are 3 or more
    matches_with_5_or_more_wickets = wickets_per_match[wickets_per_match['is_wicket'] >= 5]
    
    return matches_with_5_or_more_wickets

def runs_per_over_concede_by_bowler(filtered_df):
    # fig = px.bar(filtered_df, x='over', y='total_runs', 
    #             title='Total Runs Conceded per Over',
    #             labels={'over': 'Over', 'total_runs': 'Total Runs'})

    # # Show the plot
    # return fig
  fig = px.bar(filtered_df, x='over', y='total_runs',
               title='Runs concede per Over')
  fig.update_layout(yaxis_title='Number of Runs', xaxis_title='Over', margin=dict(l=0, r=0, t=30, b=0))
  return fig

def runs_and_wickets_per_over(filtered_df):
    # Aggregate total runs and wickets per over
    runs_and_wickets_per_over = filtered_df.groupby(['over', 'bowler']).agg({'total_runs': 'sum', 'is_wicket': 'sum'}).reset_index()
    
    # Create a bar plot
    fig = px.bar(runs_and_wickets_per_over, x='over', y='is_wicket', 
                 labels={'over': 'Over', 'is_wicket': 'Wickets'}, 
                 title='Wickets Taken per Over')
    
    # Update layout
    fig.update_layout(yaxis_title='Number of Wickets', xaxis_title='Over', margin=dict(l=0, r=0, t=30, b=0))
    
    return fig

























df2 = pd.read_csv('D:\All_data_science_project\DASH\IPL\Data\matches.csv')
df2['date'] = pd.to_datetime(df2['date'])
df2['year'] = df2['date'].dt.year
df2




def card1(headername,df):
    
    x =       dbc.Card(
                [
                        dbc.CardHeader(headername,style = {"textAlign": "center"}),
                    dbc.CardBody(
            [


                        html.H1(df['match_id'].nunique(),style = {"textAlign": "center","fontSize": "606px"})                                                      
        ]
                ),
                                                                
                ],
                style={"width": "rem",'backgroundColor':'lightgray','height':'130px'},
            )
    return x 
#.....................................................................................................................................



# Assuming df is your DataFrame containing the IPL data
# Replace 'df' with the actual name of your DataFrame if it's different

# Combine unique teams from 'team1' and 'team2' columns for each year
def update_barplot(df,height=None, width=None,margin=None):

    unique_teams_per_year = df.groupby('year')[['team1', 'team2']].agg({'team1': 'unique', 'team2': 'unique'})

    # Count the number of unique teams for each year
    unique_teams_per_year['unique_teams_count'] = unique_teams_per_year.apply(lambda row: len(set(row['team1']) | set(row['team2'])), axis=1)

    # Display the result
    unique_teams_per_year['unique_teams_count'].reset_index()

    # Create the bar plot
    fig = px.bar(unique_teams_per_year.reset_index(), x='year', y='unique_teams_count' 
                 
                )
    fig.update_layout(xaxis=dict(title=None), yaxis=dict(title=None),paper_bgcolor="lightgray",plot_bgcolor='lightgray')
    
    if height:
        fig.update_layout(height=height)
    if width:
        fig.update_layout(width=width)
    if margin:
        fig.update_layout(margin=margin)
    return fig 








def card2(headername,df):
    
    x =       dbc.Card(
                [
                        dbc.CardHeader(headername,style = {"textAlign": "center"}),
                    dbc.CardBody(
            [
                                                                                    
                        dbc.Row([
                            
                            dbc.Col([ 
                                html.H3(df['team1'].nunique(),style = {"textAlign": "center","fontSize": "100px"}),
                                
                                

                                ]),
                                dbc.Col([



                                    dcc.Graph(id='unique-teams-bar',figure = update_barplot(df2,170,600,dict(l=20, r=20, t=20, b=20)),style = {"height":'170px'}),
                                ])

                            
                            
                            ])                                                      
        ]
                ),
                                                                
                ],
                style={"width": "rem",'backgroundColor':'lightgray','height':'230px'},
            )
    return x 

#.....................................................................................................................................







def success(df):
    finals = df[df['match_type'] == "Final"]

    # Create a Series with team names as index and number of wins as values
    wins_by_team = (
        finals.groupby('winner')['winner']
        .count()
        .reset_index(name='Wins')
    )

    # Sort by wins (optional)
    wins_by_team = wins_by_team.sort_values(by='Wins', ascending=False)

    # Print the result (optional)
    wins_by_team

    return html.Div([
        html.H6("IPL Final Wins by Team"),
        
        dash_table.DataTable(
            id='final-wins',
            columns=[{'name': col, 'id': col} for col in wins_by_team.columns],
            data=wins_by_team.to_dict('records')
        )
    ])





# image_urls = [
#     r"D:\All_data_science_project\DASH\IPL\assets\img1.jpg",
#     r"D:\All_data_science_project\DASH\IPL\assets\img2.jpeg",
#     r"D:\All_data_science_project\DASH\IPL\assets\img3.jpg"
# ]

# def generate_carousel_items(image_urls):
#     items = []
#     for url in image_urls:
#         items.append(
#             dbc.CarouselItem(
#                 children=[
#                     html.Img(src=url, className="img-fluid")
#                 ]
#             )
#         )
#     print(items)

# generate_carousel_items(image_urls)


def update_plot_run(df,team,line_color):
    
    # # Filter the data
    #     # Filter the data
    # df_filtered = df[df['batting_team'] == team]
    # print('Filtered DataFrame:')
    # print(df_filtered)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['year'], y=df['total_runs'], mode='lines+markers', name='Total Runs',line=dict(color=line_color)))
    
    fig.update_layout(title=f'Total Runs scored by {team} each year', xaxis_title='Year', yaxis_title='Total Runs')
    return fig

def update_plot_wick(df,team,line_color):
    
    # # Filter the data
    #     # Filter the data
    # df_filtered = df[df['batting_team'] == team]
    # print('Filtered DataFrame:')
    # print(df_filtered)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['year'], y=df['is_wicket'], mode='lines+markers', name='is_wicket',line=dict(color=line_color)))
    
    fig.update_layout(title=f'Total Wickets collected by {team} each year', xaxis_title='Year', yaxis_title='Total Wickets')
    return fig




def update_bar_plot_change_color(df):
    # Assuming your DataFrame is named 'yearly_wins'
# Assuming the final winner for each year is stored in the 'final_winner' column

# Create a list of colors for the bars
            
            colors = ['#33FFFF' if is_final_winner == 'Yes' else 'light blue' for is_final_winner in df['final_winner']]

            # Create the bar plot
            fig = go.Figure(data=[go.Bar(
                x=df['year'],
                y=df['wins'],
                marker_color=colors,  # Assign colors to the bars
            )])

            # Update the layout
            fig.update_layout(title='Yearly wins by each team with final winner indication',
                            xaxis_title='Year',
                            yaxis_title='Wins count')

            # Show the plot
            return fig










df4 = pd.read_csv('D:\All_data_science_project\DASH\IPL\Data\Geocoding.csv')
df3 =pd.read_csv('D:\All_data_science_project\DASH\IPL\Data\stadium.csv')
#print(df3)
df4.rename(columns={'Address': 'Stadium'},inplace=True)
df=df3.merge(df4,on = 'Stadium',how = 'inner')



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


def mapbox():
    
    x = px.scatter_mapbox(df,lat = 'Latitude', lon = 'Longitude' ,hover_name='Stadium', mapbox_style = 'open-street-map',size="Matches Conducted",color = 'Matches Conducted',
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=45, zoom=4)
    x.update_layout(margin=dict(l=0, r=0, t=0, b=0))

    return x





df2['team1'] = df2['team1'].replace({'Rising Pune Supergiants': 'Rising Pune Supergiant'})
df2['team2'] = df2['team2'].replace({'Rising Pune Supergiants': 'Rising Pune Supergiant'})

# Count the number of matches played by each team using unique match IDs
matches_played_by_team = pd.concat([df2.groupby('team1')['id'].nunique(), 
                                    df2.groupby('team2')['id'].nunique()]).groupby(level=0).sum()

#print("Number of matches played by each team:")
matches_played_by_team = matches_played_by_team.reset_index()
matches_played_by_team = matches_played_by_team.rename(columns={'index': 'Team_name', 'id': 'match_played'})
mm = matches_played_by_team['match_played'].sum()





df2['venue'] = df2['venue'].str.split(',').str[0].str.strip()

# Recalculate highest runs per stadium
highest_runs_per_stadium = df2.groupby('venue')['target_runs'].max()

#print(highest_runs_per_stadium.reset_index())













#total_runs_each_year = df2.groupby(['year'])['total_runs'].sum().reset_index()
def total_ipl_run():
    df2.rename(columns = {'id':'match_id'}, inplace = True)
   
    xx = df1[['match_id','batting_team','total_runs']].merge(df2[['match_id','date']],on = 'match_id',how = 'inner')
    xx['date'] = pd.to_datetime(xx['date'])

    # Extract year from the date column
    xx['year'] = xx['date'].dt.year
   
    fig = px.bar(xx.groupby(['year'])['total_runs'].sum().reset_index(), x='year', y='total_runs', 
                labels={'year': 'Year', 'total_runs': 'Total Runs'},
                title='Total Runs Each Year')
    fig.update_layout(margin=dict(l=0, r=0, t=90, b=0))
    # Show the plot
    return fig
#dict(l=20, r=20, t=20, b=20)




df3['Stadium'] = df3['Stadium'].str.replace(r',.*', '', regex=True)
df3['Stadium'] = df3['Stadium'].str.replace(r'\(.*\)', '', regex=True)
df3['Stadium'] = df3['Stadium'].str.strip()

# Aggregate matches conducted for each stadium
matches_per_stadium = df3.groupby('Stadium')['Matches Conducted'].sum().reset_index()
df3['Stadium'] = df3['Stadium'].str.replace('M.Chinnaswamy Stadium', 'M Chinnaswamy Stadium')

#print(matches_per_stadium)









def total_ipl_wickets():
    df2.rename(columns = {'id':'match_id'}, inplace = True)
    x = df1[['match_id','is_wicket']].merge(df2[['match_id','date']],on = 'match_id',how = 'inner')
    x['date'] = pd.to_datetime(x['date'])

# Extract year from the date column
    x['year'] = x['date'].dt.year

    # Filter rows where is_wicket is 1
    wickets_df = x[x['is_wicket'] == 1]

    # Group by year and count the wickets
    total_wickets_per_year = wickets_df.groupby('year')['is_wicket'].count().reset_index()
    fig = px.line(total_wickets_per_year, x='year', y='is_wicket', 
                  labels={'year': 'Year', 'is_wicket': 'Total Wickets'},
                  title='Total Wickets Each Year',
                  #template='plotly_dark',  # Use dark theme for better contrast
                  line_shape='linear',    # Smooth spline line
                  #line_dash='is_wicket',       # Dashed line
                  markers=True,           # Show markers at data points
                  color_discrete_sequence=['green'],
                  
                  )  # Custom color for the line
    
    # Update layout
    fig.update_layout(margin=dict(l=0, r=0, t=40, b=0),
                      plot_bgcolor="light gray")
    return fig








def calculate_total_runs_per_year(x):

 batsman_name = [m['batter'] == x]

# Group by 'year' and sum the 'batsman_runs'
 batsman_runs_per_year = batsman_name.groupby('year')['batsman_runs'].sum().reset_index()
 return batsman_runs_per_year





def update_table(search_value):
    if not search_value:
        return df1.to_dict('records')
    # Perform fuzzy matching
    matches = process.extract(search_value, df1['batter'], limit=len(df1))
    matched_names = [match[0] for match in matches if match[1] > 50]  # Adjust the threshold as needed
    filtered_df = df1[df1['batter'].isin(matched_names)]
    print(f'printing the shape of --- {filtered_df.shape}')

    return filtered_df











def batsman_total_runs(filtered_df):

    
    selected_batsman_runs = filtered_df['batsman_runs'].sum()
    return selected_batsman_runs

def total_match(filtered_df):
    return filtered_df.groupby('match_id').count().reset_index().shape[0]

def thirty_plus_runs(filtered_df):
    x = filtered_df.groupby('match_id')['batsman_runs'].sum()
    matches_with_30_or_more = x[x >= 30].count()
    return matches_with_30_or_more

def fifty_plus_runs(filtered_df):
    x = filtered_df.groupby('match_id')['batsman_runs'].sum()
    matches_with_50_or_more = x[(x >= 50) & (x <= 99)].count()
    return matches_with_50_or_more


def hundered_plus_runs(filtered_df):
    x = filtered_df.groupby('match_id')['batsman_runs'].sum()
    matches_with_100_or_more = x[x >= 100].count()
    return matches_with_100_or_more





def runs_by_over_for_batsman(filtered_df):
    # Filtering the DataFrame for the specified batsman
    
    
    # Grouping the filtered DataFrame by 'over' and summing 'batsman_runs' for each group
    runs_per_over = filtered_df.groupby('over')['total_runs'].sum().reset_index()
    
    #Create a bar plot
    fig = px.bar(runs_per_over, x='over', y='total_runs', 
                 labels={'over': 'Over', 'total_runs': 'Total Runs'}, 
                 title='Runs per Over')
    
    # Update layout
    fig.update_layout(yaxis_title='Total Runs', xaxis_title='Over', margin=dict(l=0, r=0, t=30, b=0))
    
    return fig




def DismissalType(filtered_df):

    fig = px.bar(filtered_df, x='dismissal_kind', y='count', labels={'dismissal_kind': 'dismissal kind', 'count': 'count'}, title='Dismissal type')
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    
    return fig
#     print(batsman_dismissals)
# DismissalType('BB McCullum')

# Example usage:
# batsman_name = "SC Ganguly"
# batsman_runs_by_over = runs_by_over_for_batsman(batsman_name, df1)
# batsman_runs_by_over


# def player_of_the_match_count(df):

#     unique_batters = df['batter'].unique()

#     # Now, we will count the number of times each batter is named "player_of_match" in the original DataFrame
#     player_of_match_counts = df[df2['player_of_match'].isin(unique_batters)]['player_of_match'].value_counts()

#     # Display the result
#     print(player_of_match_counts)



    