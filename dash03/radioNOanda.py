# ejemplo boludo con Radio Buttons - NO anda
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
dcc.RadioItems(
    id='radio-items',
    options = [
        {'label': 'One', 'value': 'first'},
        {'label': 'Two', 'value': 'second'},
        {'label': 'Three', 'value': 'third'},

        ],
    value = "",
    labelStyle={'display': 'inline-block'}
    ), 

dcc.Graph(id='pie-chart')
])


@app.callback(Output('pie-chart', 'figure'),
    [Input('radio-items', 'value')])
def render_charts(value):
    labels1 = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    values1 = [4500,2500,1053,500]

    labels2 = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    values2 = [4500,2500,1053,500]

    labels3 = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    values3 = [4500,2500,1053,500]

    charts = [
        go.Pie(labels=labels1, values=values1),
        go.Pie(labels=labels2, values=values2),
        go.Pie(labels=labels3, values=values3)
               ]
    
    if value == 'first':
        return {
            'data':charts[0],
            'layout' : go.Layout()
            }
    elif value == 'second': 
         return {
            'data':charts[1],
            'layout' : go.Layout()
            }
    else: 
        return {
            'data':charts[2],
            'layout' : go.Layout()
            }

if __name__ == '__main__':
    app.run_server(debug=True, port=8056)