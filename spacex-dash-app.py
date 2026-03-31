# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(id='site-dropdown',
                                        options=[
                                            {'label': 'All Sites', 'value': 'ALL'},
                                            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
                                        ],
                                        value='ALL',
                                        placeholder="Select a Launch Site",
                                        searchable=True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(
                                    id='payload-slider',
                                    min=0,  # slider starting point in kg
                                    max=10000,  # slider ending point in kg
                                    step=1000,  # interval step in kg
                                    marks={0: '0', 1000: '1000', 2000: '2000', 3000: '3000', 4000: '4000',
                                        5000: '5000', 6000: '6000', 7000: '7000', 8000: '8000', 9000: '9000',
                                        10000: '10000'},
                                    value=[min_payload, max_payload]  # default range selected
                                ),
                                html.Br(),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # Use all data to show total success launches by site
        fig = px.pie(
            spacex_df, 
            names='Launch Site', 
            values='class',  # 'class' is 1 for success, 0 for failure
            title='Total Successful Launches by Site'
        )
    else:
        # Filter data for the selected launch site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        # Count successes and failures
        success_counts = filtered_df['class'].value_counts().reset_index()
        success_counts.columns = ['class', 'count']
        # Map 0/1 to meaningful labels
        success_counts['class'] = success_counts['class'].map({1: 'Success', 0: 'Failure'})
        # Create pie chart for the selected site
        fig = px.pie(
            success_counts, 
            names='class', 
            values='count',
            title=f"Total Launch Outcomes for site {entered_site}"
        )
    return fig
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown', component_property='value'),
        Input(component_id='payload-slider', component_property='value')
    ]
)
def get_scatter_plot(entered_site, payload_range):
    low, high = payload_range  # unpack slider range
    # Filter by payload range first
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]
    
    if entered_site == 'ALL':
        # Scatter for all sites
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            hover_data=['Launch Site'],
            title='Correlation between Payload and Success for All Sites'
        )
    else:
        # Scatter for specific site
        site_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(
            site_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            hover_data=['Launch Site'],
            title=f'Correlation between Payload and Success for site {entered_site}'
        )
    return fig

# Run the app
if __name__ == '__main__':
    app.run()
