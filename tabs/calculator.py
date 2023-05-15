style = {'padding': '1.5em'}

app.layout = html.Div([
    dcc.Markdown("""
        ### Predict
        Use the controls below to update your predicted diagnosis of coronary disease, based on chest pain, vessel calcification and stress test performance.
        Scores range from 0-4 and denote the degree of coronary occlusion, with 0 indicating no occlusion and 4 corresponding to the worst.
    """),

    html.Div(id='prediction-content', style={'fontWeight': 'bold'}),


    html.Div([
        dcc.Markdown('###### Chest Pain'),
        dcc.Slider(
            id='chest_pain',
            min=1,
            max=4,
            step=1,
            value=3,
            marks={n: str(n) for n in range(1, 4, 1)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Vessel Calcification'),
        dcc.Slider(
            id='vessel_calcification',
            min=0,
            max=3,
            step=1,
            value=2,
            marks={n: str(n) for n in range(0, 3, 1)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Stress Test'),
        dcc.Slider(
            id='stress_test',
            min=3,
            max=7,
            step=1,
            value=3,
            marks={n: str(n) for n in range(3, 7, 1)}
        ),
    ], style=style),


])


@app.callback(
    Output('prediction-content', 'children'),
    [Input('chest_pain', 'value'),
     Input('vessel_calcification', 'value'),
     Input('stress_test', 'value')])

def predict(chest_pain, vessel_calcification, stress_test):

 
    df3 = pd.DataFrame(
        columns=['Chest Pain', 'Vessel Calcification', 'Stress Test'],
        data=[[chest_pain, vessel_calcification, stress_test]]
    )

    rfc_pipeline = joblib.load('rfc_pipeline.joblib')
    y_pred_log = rfc_pipeline.predict(df3)
    y_pred = y_pred_log[0]
    results = f'The predicted diagnosis is {y_pred:,.0f}.'

    return results
