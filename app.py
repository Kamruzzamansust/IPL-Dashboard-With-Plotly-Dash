import dash
from dash import dcc
from dash import html
from dash import html, dcc,Input,Output,State, callback

import dash_bootstrap_components as dbc
import requests
from pathlib import Path
import sys
import pandas as pd
#import pages.page2 as pp
#from dash_bootstrap_templates import load_figure_template

# Add the parent directory of the current module to the Python path

current_path = Path(__file__).resolve().parent
parent_path = current_path.parent
sys.path.append(str(parent_path))

#load_figure_template('DARKLY')
background_image_url = r'D:\All_data_science_project\DASH\IPL\assets\img1.jpg'  

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1.0"}],
    suppress_callback_exceptions=True  # Add this line to suppress callback exceptions
)



row_1 = dbc.Row(
    [
        dbc.Col(
            [
                #html.H2("Ipl DashBoard Analysis",style ={'text-align':'center'}),
                dbc.Nav(
    [
        dbc.NavLink("Home", href="/", active="exact"),
        dbc.NavLink("Analytics", href="/Analytics", active="exact"),  # Add more links as needed
        #dbc.NavLink("About", href="/about", active="exact"),
    ],
    vertical=False,
    #className="sidebar",  # Optional class for styling
    # style={
    #     "position": "fixed",
    #     "width": "200px",
    #     "height": "100vh",  # Adjust height if needed
    #     "left": 0,
    #     "background-color": 'yellow',  # Adjust background color
    #     "padding": "20px",
    # },
)
                
            ],style = {'height':'80px','backgroundColor':'lightblue'}
        )
    ]
)

row_2 = dbc.Row(
    [
#         dbc.Col(
#             [
# #                 dbc.Nav(
# #     [
# #         dbc.NavLink("Home", href="/", active="exact"),
# #         dbc.NavLink("Analytics", href="/Analytics", active="exact"),  # Add more links as needed
# #         #dbc.NavLink("About", href="/about", active="exact"),
# #     ],
# #     vertical=False,
# #     #className="sidebar",  # Optional class for styling
# #     # style={
# #     #     "position": "fixed",
# #     #     "width": "200px",
# #     #     "height": "100vh",  # Adjust height if needed
# #     #     "left": 0,
# #     #     "background-color": 'yellow',  # Adjust background color
# #     #     "padding": "20px",
# #     # },
# # )
#             ],width = 1 ,style = {'backgroundColor':'#FAF9F6'
#                                      }
#         ),
        dbc.Col(
            [
                dash.page_container
            ],style = {'height':'1400px','backgroundColor':'white'
                                     }
        )
    ]
)


# sidebar_layout = dbc.Nav(
#     [
#         dbc.NavLink("Home", href="/", active="exact"),
#         dbc.NavLink("Analytics", href="/Analytics", active="exact"),  # Add more links as needed
#         #dbc.NavLink("About", href="/about", active="exact"),
#     ],
#     vertical=True,
#     className="sidebar",  # Optional class for styling
#     style={
#         "position": "fixed",
#         "width": "200px",
#         "height": "100vh",  # Adjust height if needed
#         "left": 0,
#         "background-color": "#f8f9fa",  # Adjust background color
#         "padding": "20px",
#     },
# )










app.layout = html.Div(
    [
        dbc.Container(  # Content container
            [
                row_1,
                row_2
            ],
            fluid=True,
            style={
                'border': '1px solid #4eb1ce',
                'height': '2205px'
            }
        ),
        html.Div(  className='background-image',
            style={
                'position': 'absolute',
                'top': 0,
                'left': 0,
                'width': '100%',
                'height': '100%',
                'backgroundImage': f'url({background_image_url})',
                'backgroundSize': 'contain',  # Adjust size as needed (cover, contain, etc.)
                'backgroundRepeat': 'no-repeat',  # Or 'repeat' for tiling
                'backgroundPosition': 'center',  # Adjust position as needed (center, top, etc.)
                'zIndex': -1  # Ensure background is behind content
            }
        )
    ]
)



if __name__ == "__main__":
    app.run_server(debug=True)