from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import intro, calculator

server = app.server

style = {'maxWidth': '960px', 'margin': 'auto'}

app.layout = html.Div([
    dcc.Markdown('# Coronary Disease Calculator'),
    dcc.Tabs(id='tabs', value='tab-intro', children=[
        dcc.Tab(label='Intro', value='tab-intro'),
        dcc.Tab(label='Calculator', value='tab-calculator')
    ]),
    html.Div(id='tabs-content')
], style=style)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-intro': return intro.layout
    elif tab == 'tab-calculator': return calculator.layout

if __name__ == '__main__':
    app.run_server(debug=True)
