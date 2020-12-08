# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd

# Imports from this application
from app import app

#Load pipeline
pipeline = load('assets/pipeline4.joblib')
print('Pipeline Loaded!')
print(type(pipeline))



# def predict(neighborhood, property_type, instant_bookable, room_type, bedrooms, bathrooms, accommodates, review_scores_value, cancellation_policy, host_is_superhost, self_check_in, free_parking_on_premises, patio_or_balcony,
#         internet, beach_essentials, garden_or_backyard, washer, air_conditioning, heating, 
#         laptop_friendly_workspace, kitchen, referigerator, hair_dryer, iron, indoor_fireplace,
#         free_street_parking, microwave, hot_water, cabel_tv, breakfast, essentials, coffee_maker, dishes_and_silverware, 
#         dishwasher, stove, oven, private_entrance, gym, pool, cleaning_fee, security_deposit, host_acceptance_rate, minimum_nights, host_response_time, host_response_rate):
#     print('Navroz says predict function has been called')
#     df = pd.DataFrame(
#         columns=['neighborhood', 'property_type', 'instant_bookable', 'room_type', 'bedrooms', 'bathrooms', 'accommodates', 'review_scores_value', 'cancellation_policy', 'host_is_superhost', 'self_check_in', 'free_parking_on_premises', 'patio_or_balcony',
#         'internet', 'beach_essentials', 'garden_or_backyard', 'washer', 'air_conditioning', 'heating', 
#         'laptop_friendly_workspace', 'kitchen', 'referigerator', 'hair_dryer', 'iron', 'indoor_fireplace',
#         'free_street_parking', 'microwave', 'hot_water', 'cabel_tv', 'breakfast', 'essentials', 'coffee_maker', 'dishes_and_silverware', 
#         'dishwasher', 'stove', 'oven', 'private_entrance', 'gym','pool','cleaning_fee', 'security_deposit', 'host_acceptance_rate', 'minimum_nights', 'host_response_time', 'host_response_rate'], 
#         data=[[neighborhood, property_type, instant_bookable, room_type, bedrooms, bathrooms, accommodates, review_scores_value, cancellation_policy, host_is_superhost, self_check_in, free_parking_on_premises, patio_or_balcony,
#         internet, beach_essentials, garden_or_backyard, washer, air_conditioning, heating, 
#         laptop_friendly_workspace, kitchen, referigerator, hair_dryer, iron, indoor_fireplace,
#         free_street_parking, microwave, hot_water, cabel_tv, breakfast, essentials, coffee_maker, dishes_and_silverware, 
#         dishwasher, stove, oven, private_entrance, gym, pool, cleaning_fee, security_deposit, host_acceptance_rate, minimum_nights, host_response_time, host_response_rate]]
#     )
#     y_pred = pipeline.predict(df)[0]
#     return f'${y_pred:.0f}'

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 

        dcc.Markdown('#### Neighborhood'), 
        dcc.Dropdown(
            id='neighborhood', 
            options = [

                {'label': 'Beverly Hills', 'value': 'Beverly Hills'},
                {'label': 'Hollywood', 'value': 'Hollywood'}, 
                {'label': 'Downtown Los Angeles', 'value': 'Downtown'}, 
                {'label': 'Santa Monica', 'value': 'Santa Monica'}, 
                {'label': 'Venice', 'value': 'Venice'}, 
                {'label': 'Long Beach', 'value': 'Long Beach'},
                {'label': 'West Hollywood', 'value': 'West Hollywood'},
                {'label': 'East Hollywood', 'value': 'East Hollywood'},
                {'label': 'Mid-Wilshire', 'value': 'Mid-Wilshire'},
                {'label': 'Silver Lake', 'value': 'Silver Lake'},
                {'label': 'Glendale', 'value': 'Glendale'},
                {'label': 'Hollywood Hills West', 'value': 'Hollywood Hills West'},
                {'label': 'Koreatown', 'value': 'Koreatown'},
                {'label': 'Rowland Heights', 'value': 'Rowland Heights'},
                {'label': 'Westwood', 'value': 'Westwood'},
                {'label': 'Other', 'value': 'Other'}

            ], 
            value = 'Downtown', 
            className='mb-5', 
        ),
        #########
        dcc.Markdown('#### Property Type'), 
        dcc.Dropdown(
            id='property_type', 
            options = [

                {'label': 'Condominium', 'value': 'Condominium'},
                {'label': 'Apartment', 'value': 'Apartment'}, 
                {'label': 'House', 'value': 'House'}, 
                {'label': 'Guesthouse', 'value': 'Guesthouse'}, 
                {'label': 'Bungalow', 'value': 'Bungalow'}, 
                {'label': 'Loft', 'value': 'Loft'},
                {'label': 'Guest suite', 'value': 'Guest suite'},
                {'label': 'Townhouse', 'value': 'Townhouse'},
                {'label': 'Hostel', 'value': 'Hostel'},
                {'label': 'Boutique hotel', 'value': 'Boutique hotel'},
                {'label': 'Villa', 'value': 'Villa'},
                {'label': 'Cottage', 'value': 'Cottage'},
                {'label': 'Camper/RV', 'value': 'Camper/RV'},
                {'label': 'Aparthotel', 'value': 'Aparthotel'},
                {'label': 'Serviced apartment', 'value': 'Serviced apartment'},
                {'label': 'Other', 'value': 'Other'}

            ], 
            value = 'Apartment', 
            className='mb-5', 
        ),
         
         dcc.Markdown('#### Instant Booking'), 
            dcc.Dropdown(
            id='instant_bookable', 
            options = [

                {'label': 'YES', 'value': 'YES'},
                {'label': 'NO', 'value': 'NO'}

            ], 
            value = 'NO', 
            className='mb-5', 
        ),
        
        dcc.Markdown('#### Room Type'), 
        dcc.Dropdown(
            id='room_type', 
            options = [

                {'label': 'Entire home/apt', 'value': 'Entire home/apt'},
                {'label': 'Private room', 'value': 'Private room'}, 
                {'label': 'Hotel room', 'value': 'Hotel room'}, 
                {'label': 'Shared room', 'value': 'Shared room'}

            ], 
            value = 'Entire home/apt', 
            className='mb-5', 
        ),
        
        dcc.Markdown('#### Bedrooms'), 
        dcc.Dropdown(
            id='bedrooms', 
            options = [

                # {'label': 'Studio', 'value': 'Studio'},
                {'label': '1', 'value': '1'}, 
                {'label': '2', 'value': '2'}, 
                {'label': '3', 'value': '3'}, 
                {'label': '4', 'value': '4'}, 
                {'label': '5+', 'value': '5+'}

            ], 
            value = '1', 
            className='mb-5', 
        ),
        
         dcc.Markdown('#### Bathrooms'), 
        dcc.Dropdown(
            id='bathrooms', 
            options = [

                {'label': '1', 'value': '1'},
                {'label': '2', 'value': '2'}, 
                {'label': '3', 'value': '3'}, 
                {'label': '4+', 'value': '4+'}

            ], 
            value = '1', 
            className='mb-5', 
        ),
        
        dcc.Markdown('#### Accommodates'), 
        dcc.Dropdown(
            id='accommodates', 
            options = [

                {'label': '1-2', 'value': '1-2'},
                {'label': '2-4', 'value': '2-4'}, 
                {'label': '4-6', 'value': '4-6'}, 
                {'label': '6-8', 'value': '6-8'}, 
                {'label': '8+', 'value': '8+'}

            ], 
            value = '1-2', 
            className='mb-5'
        ),
        
        dcc.Markdown('#### Rating 1-10'), 
        dcc.Dropdown(
            id='review_scores_value', 
            options = [

                {'label': '0-5', 'value': '0-5'},
                {'label': '5-6', 'value': '5-6'}, 
                {'label': '6-7', 'value': '6-7'}, 
                {'label': '7-8', 'value': '7-8'}, 
                {'label': '8-9', 'value': '8-9'},
                {'label': '9+', 'value': '9+'}

            ], 
            value = '8-9',
            className='mb-5', 
            multi=False
        ),
        
        dcc.Markdown('#### Cancelation Policy'), 
        dcc.Dropdown(
            id='cancellation_policy', 
            options = [

                {'label': 'Strict', 'value': 'strict_14_with_grace_period'},
                {'label': 'Flexible', 'value': 'flexible'}, 
                {'label': 'Moderate', 'value': 'moderate'}
                
            ], 
            value = 'strict_14_with_grace_period', 
            className='mb-5' 
        )
    
    ],
    md=4,
)

column2 = dbc.Col(
    [   
        dcc.Markdown('#', className='mb-5'),
        
        dcc.Markdown('#### Superhost'), 
            dcc.Dropdown(
            id='host_is_superhost', 
            options = [

                {'label': 'YES', 'value': 'YES'},
                {'label': 'NO', 'value': 'NO'}

            ], 
            value = 'YES', 
            className='mb-5'
        ),
    
        dcc.Markdown('#### Cleaning Fee'), 
        dcc.Dropdown(
            id='cleaning_fee', 
            options = [

                {'label': 'Upto 50', 'value': '0-50'}, 
                {'label': '50-100', 'value': '50-100'},
                {'label': '100-150', 'value': '100-150'},
                {'label': '150+', 'value': '150+'}
                
            ], 
            value = '0-50',
            className='mb-5', 
            multi=False,
            disabled=False
        ),
        
        dcc.Markdown('#### Security Deposit'), 
        dcc.Dropdown(
            id='security_deposit', 
            options = [

                {'label': 'Upto 100 ', 'value': '0-100'}, 
                {'label': '100-200', 'value': '100-200'},
                {'label': '200-300', 'value': '200-300'},
                {'label': '300-400', 'value': '300-400'}, 
                {'label': '400+', 'value': '400+'}
                
            ], 
            value = '0-100',
            className='mb-5', 
            multi=False,
            disabled=False
        ),
        
        dcc.Markdown('#### Host Acceptance Rate'), 
        dcc.Dropdown(
            id='host_acceptance_rate', 
            options = [

                {'label': '0-20', 'value': '0-20'},
                {'label': '20-40', 'value': '20-40'}, 
                {'label': '40-60', 'value': '40-60'},
                {'label': '60-80', 'value': '60-80'},
                {'label': '80-94', 'value': '80-94'}, 
                {'label': '94+', 'value': '94+'}
                
            ], 
            value = '94+', 
            className='mb-5', 
            disabled=False
        ),
        
        dcc.Markdown('#### Minimum Nights'), 
        dcc.Dropdown(
            id='minimum_nights', 
            options = [

                {'label': '1', 'value': '1'},
                {'label': '2', 'value': '2'}, 
                {'label': '7', 'value': '7'}, 
                {'label': '30', 'value': '30'},
                {'label': '30+', 'value':'30+'}

            ], 
            value = '1', 
            className='mb-5',
            multi=False,
            disabled=False 
        ),
        
        dcc.Markdown('##### Set to Default for a better customer experience', className='mb-5'),

        dcc.Markdown('#### Host Response Time'), 
        dcc.Dropdown(
            id='host_response_time', 
            options = [

                {'label': 'within an hour', 'value': 'within an hour'},
                {'label': 'within a few hours', 'value': 'within a few hours'}, 
                {'label': 'within a day', 'value': 'within a day'},
                {'label': 'a few days or more', 'value': 'a few days or more'}
                
            ], 
            value = 'within an hour',
            className='mb-5', 
            multi=False,
            disabled=True
        ),
        
        dcc.Markdown('#### Host Response Rate'), 
        dcc.Dropdown(
            id='host_response_rate', 
            options = [

                {'label': '100%', 'value': '100'}
        
            ], 
            value = '100', 
            className='mb-5', 
            disabled=True
        )
    ],
    md=4,
)

column3 = dbc.Col(
    [
        html.H2('Nightly Rate', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
        
    ]
)

layout = dbc.Row([column1, column2, column3])

@app.callback(
    Output('prediction-content', 'children'),

    [Input('neighborhood', 'value'), 
    Input('property_type', 'value'),
    Input('instant_bookable', 'value'), 
    Input('room_type', 'value'),
    Input('bedrooms', 'value'), 
    Input('bathrooms', 'value'),
    Input('accommodates', 'value'), 
    Input('review_scores_value', 'value'),
    Input('cancellation_policy', 'value'), 
    Input('host_is_superhost', 'value'),
    # Input('self_check_in', 'value'), 
    # Input('free_parking_on_premises', 'value'),
    # Input('patio_or_balcony', 'value'), 
    # Input('internet', 'value'),
    # Input('beach_essentials', 'value'), 
    # Input('garden_or_backyard', 'value'),
    # Input('washer', 'value'), 
    # Input('air_conditioning', 'value'),
    # Input('heating', 'value'), 
    # Input('laptop_friendly_workspace', 'value'),
    # Input('kitchen', 'value'), 
    # Input('referigerator', 'value'),
    # Input('hair_dryer', 'value'), 
    # Input('iron', 'value'),
    # Input('indoor_fireplace', 'value'), 
    # Input('free_street_parking', 'value'),
    # Input('microwave', 'value'), 
    # Input('hot_water', 'value'),
    # Input('cabel_tv', 'value'), 
    # Input('breakfast', 'value'),
    # Input('essentials', 'value'), 
    # Input('coffee_maker', 'value'),
    # Input('dishes_and_silverware', 'value'), 
    # Input('dishwasher', 'value'),
    # Input('stove', 'value'), 
    # Input('oven', 'value'),
    # Input('private_entrance', 'value'), 
    # Input('gym', 'value'),
    # Input('pool', 'value'),
    Input('cleaning_fee', 'value'),
    Input('security_deposit', 'value'), 
    Input('host_acceptance_rate', 'value'),
    Input('minimum_nights', 'value'), 
    Input('host_response_time', 'value'),
    Input('host_response_rate', 'value')]
)
def predict(neighborhood, property_type, instant_bookable, room_type, bedrooms, bathrooms, accommodates, review_scores_value, cancellation_policy, host_is_superhost, cleaning_fee, security_deposit, host_acceptance_rate, minimum_nights, host_response_time, host_response_rate):
    print('Navroz says predict function has been called')
    df = pd.DataFrame(
        columns=['neighborhood', 'property_type', 'instant_bookable', 'room_type', 'bedrooms', 'bathrooms', 'accommodates', 'review_scores_value', 'cancellation_policy', 'host_is_superhost','cleaning_fee', 'security_deposit', 'host_acceptance_rate', 'minimum_nights', 'host_response_time', 'host_response_rate'], 
        data=[[neighborhood, property_type, instant_bookable, room_type, bedrooms, bathrooms, accommodates, review_scores_value, cancellation_policy, host_is_superhost, cleaning_fee, security_deposit, host_acceptance_rate, minimum_nights, host_response_time, host_response_rate]]
    )
    y_pred = pipeline.predict(df)[0]
    return y_pred
