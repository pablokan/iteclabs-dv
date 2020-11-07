import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

import pymysql
db = pymysql.connect("localhost", "root", "root", "tecnoredDB" )
cur = db.cursor()
cur.execute("SELECT FOS, TAC, fech FROM charDige")
datos = cur.fetchall()

external_stylesheets = ['bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame.from_records(datos)

app.layout = html.Div([
        html.Div([
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['FOS', 'TAC']],
                value='FOS',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

    ]),
   
    dcc.Graph(id='bar-chart'),

])

""" 
@app.callback(Output('bar-chart', 'figure'),
    [Input('radio-items', 'value')])
def make_pie_chart(value):
    trace = go.Pie(
        #define pie chart
    )
    layout = #define layout
    figure = go.Figure(data=[trace], layout=layout)
    retrun figure
 """
if __name__ == '__main__':
    app.run_server(debug=True)
