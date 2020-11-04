import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame({
    "Fechas": ["2020-11-01", "2020-11-02", "2020-11-03", "2020-11-01", "2020-11-02", "2020-11-03", "2020-11-01", "2020-11-02", "2020-11-03"],
    "Cantidades": [3567, 1387, 4102, 1902, 7165, 2091, 1555, 1555, 4555],
    "Datos": ["FOS", "FOS", "FOS", "TAC", "TAC", "TAC", "FOS/TAC", "FOS/TAC", "FOS/TAC"]
})

fig = px.bar(df, x="Fechas", y="Cantidades", color="Datos", barmode="group", opacity=0.5)

app.layout = html.Div(children=[
    html.H1(children='Digestor Primario 1'),

    html.Div(children='''   
        Análisis
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
