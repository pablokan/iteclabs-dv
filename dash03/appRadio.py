import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

external_stylesheets = ['bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Apples", "Oranges"],
    "Amount": [2, 1, 4, 2],
    "City": ["SF", "SF", "Montreal", "Montreal"]
})


app.layout = html.Div(children=[
    html.H1(children='Children grande', style={'textAlign': 'center'}),
    html.H4(children='children chico', style={'textAlign': 'center'}),
    html.Div(dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['FOS', 'TAC']],
                value='FOS',
                labelStyle={'display': 'inline-block', 'textAlign': 'center'}
            )),
    dcc.Graph(id='example-graph')
])


@app.callback(
        Output('example-graph', 'figure'),
        [Input('xaxis-type', 'value')])
    
def update_figure(xaxis):
    print(df)
    #filtered_df = df[df.Amount == 2] # dos manzanas y dos naranjas
    filtered_df = df

    fig = px.bar(filtered_df, x="Fruit", y="Amount", color="City", barmode="group", opacity=0.3)
    
    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
