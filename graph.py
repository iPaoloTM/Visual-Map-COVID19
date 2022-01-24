import pandas as pd
import glob 
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

file='dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'

df = pd.read_csv(file, index_col=None, header=0)
df.reset_index(inplace=True)
print(df[:5])

datas = ['totale_positivi', 'totale_casi' , 'deceduti', 'ricoverati_con_sintomi', 'tamponi']

app.layout = html.Div([

    html.H1("Dashboards for COVID-19", style={'text-align': 'center'}),

    dcc.Dropdown(id="views",
                 options=[{"label": x, "value":x} for x in datas],
                 value="totale_casi",
                 multi=True,
                 style={'width': "40%"}
                 ),

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


    fig = px.line(df, 
             x='data', 
             y=selection,
             template='plotly_dark',
            labels= {
                "totale_positivi":"Totale Positivi",
                "data":"Data"
            },
            
            )

    return container, fig




             
if __name__ == '__main__':
    app.run_server(debug=True)
