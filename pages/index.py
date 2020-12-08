# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Planning a trip to Los Angeles?!

            How much would you want to spend on Airbnb for a night?

            This app could help you predict the nightly rates for renting out an Airbnb, catered to your custom needs.  

            Is it a family vacation, where your family would like to rent out a house close to Disney, or is it a couple's getaway, and you are looking for an apartment close to the beach in Santa Monica?

            """
        ),
        dcc.Link(dbc.Button('Click to Predict', color='primary'), href='/predictions')
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        html.Img(src='assets/word.png', className='.img-fluid'),
    ]
)

layout = dbc.Row([column1, column2])