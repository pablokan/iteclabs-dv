import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

import pymysql
db = pymysql.connect("localhost", "root", "root", "tecnoredDB" )
cur = db.cursor()
cur.execute("SELECT FOS, TAC, fech FROM charDige")
datos = cur.fetchall()

external_stylesheets = ['bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame.from_records(datos, columns=["FOS", "TAC", "fech"])
print(df)

fig = px.bar(df, x=2, y=0, barmode="group", opacity=0.5)
#fig = px.line(df, x=2, y=0)

app.layout = html.Div(children=[html.H1(children='Digestor Primario 1'),
    html.Div(children='''Análisis'''),
    dcc.Graph(id='digestor-graph', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)