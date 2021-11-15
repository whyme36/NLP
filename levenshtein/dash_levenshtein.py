import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output,State
from levenshtein import levenshteinDistanceDP

#start
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#head
app.layout = html.Div([
    html.H4("I use dash to represent levenshtein's method"),
    html.Div([
        "Input horizontal: ",
        dcc.Input(id='my-input1',
        value='fast',
        type='text')
    ]),
    html.Br(),
    html.Div([
        "Input vertical: ",
        dcc.Input(id='my-input2',
        value='cats',
        type='text')
    ]),
    html.Br(),
    html.H4(id='distance_output'),
    html.Div(id='table_output'),
    html.Div(' by Kacper Glazer', style={ 'textAlign': 'right'})

])

#callbacks
@app.callback(
    dash.dependencies.Output(component_id='table_output',component_property= 'children'),
    [dash.dependencies.Input(component_id='my-input1', component_property='value'),
    dash.dependencies.Input(component_id='my-input2', component_property='value')]
)
def update_output_div_table(token_1,token_2):
    # if len(token_1) > 2 and len(token_2) > 2:
        array_of_array,_ = levenshteinDistanceDP(token_1, token_2)
    # stworzenie nagłówka
        token_1=[x for x in token_1]
        token_1.insert(0,"")
    # stworzenie pierwszej kolumny
        token_2 = [x for x in token_2]
        fig = go.Figure(data=[go.Table(header=dict(values=token_1),
                                       cells=dict(values=[token_2]+[array[1:] for array in array_of_array][1:]))])
        return html.Div(
            dcc.Graph(
                figure=fig
            ))
@app.callback(
    dash.dependencies.Output(component_id='distance_output',component_property= 'children'),
    [dash.dependencies.Input(component_id='my-input1', component_property='value'),
    dash.dependencies.Input(component_id='my-input2', component_property='value')]
)
def update_output_div_table(token_1,token_2):
    _,distance = levenshteinDistanceDP(token_1, token_2)
    return f"Levenshtein's distance is: {int(distance)}"

if __name__ == '__main__':
    app.run_server(debug=True)