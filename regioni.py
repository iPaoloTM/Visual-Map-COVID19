import pandas as pd
import glob 
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import requests

app = Dash(__name__)

file='dati-regioni/dpc-covid19-ita-regioni.csv'

df = pd.read_csv(file, index_col=None, header=0)
df.reset_index(inplace=True)
print(df[:5])

datas = ['totale_positivi', 'totale_casi' , 'deceduti', 'ricoverati_con_sintomi', 'tamponi']
regions = ['Piemonte', 'Trentino-Alto Adige', 'Lombardia', 'Puglia', 'Basilicata', 
           'Friuli Venezia Giulia', 'Liguria', "Valle d'Aosta", 'Emilia-Romagna',
           'Molise', 'Lazio', 'Veneto', 'Sardegna', 'Sicilia', 'Abruzzo',
           'Calabria', 'Toscana', 'Umbria', 'Campania', 'Marche']

repo_url = 'https://gist.githubusercontent.com/datajournalism-it/48e29e7c87dca7eb1d29/raw/2636aeef92ba0770a073424853f37690064eb0ea/regioni.geojson'
italy_regions_geo = requests.get(repo_url).json()

app.layout = html.Div([

    html.H1("Dashboards for COVID-19", style={'text-align': 'center'}),

    html.Div(
            dcc.RadioItems(id='views',
                options=[{'label':'Positivi','value':'totale_positivi'},{'label':'Casi','value':'totale_casi'},{'label':'Tamponi','value':'tamponi'},{'label':'Decessi','value':'deceduti'}],
                value='totale_positivi',
                style={'width': '490px'}
             ), style={'display': 'inline-block','width': '500px'}),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_graph', figure={})

])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_graph', component_property='figure')],
    [Input(component_id='views', component_property='value')]
)
def update_graph(selection):
    print(selection)

    container = "Selection: {}".format(selection)


    fig = px.choropleth(
                    data_frame=df, 
                    geojson=italy_regions_geo, 
                    locations='denominazione_regione', # name of dataframe column
                    featureidkey='properties.NOME_REG',  # path to field in GeoJSON feature object with which to match the values passed in to locations
                    color=selection,
                    color_continuous_scale="sunsetdark",
                    scope="europe",
                    
                   )
    fig.update_geos(showcountries=False, showcoastlines=False, showland=False) # fitbounds="locations")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return container, fig




             
if __name__ == '__main__':
    app.run_server(debug=True)
