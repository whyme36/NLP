import dash
import dash_core_components as dcc
import dash_html_components as html
from preparator_text_and_classifier import preprocessing_text, get_classifier, get_TFIDF

# start
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
text_address_change = 'Register number : Company name, address. Firma geändert, nun: Neue Firma: new company name. Sitz verlegt, nun: Neuer Sitz: Witten. Geändert, nun: Geschäftsanschrift: new address'
# head
app.layout = html.Div([
    html.H4("I use dash to represent classification methods"),
    html.Div([
        "Input text: ",
        dcc.Textarea(id='input_text',
                     value=text_address_change,
                     style={"width": '60%',
                            "height": '80%'})
    ]),
    html.Br(),
    html.Div([
        "Clarification model: ",
        dcc.Dropdown(id='input_model',
                     style={"width": '40%'},
                     value='LogisticRegression',
                     options=[{'label': 'Logistic Regression', 'value': 'LogisticRegression'},
                              {'label': 'Naive Bayes', 'value': 'MultinomialNB'},
                              {'label': 'SVM', 'value': 'SVC'},
                              {'label': 'Random Forest', 'value': 'RandomForestClassifier'},
                              {'label': 'XGBoost', 'value': 'XGBClassifier'}])
    ]),
    html.Br(),
    html.H4(id = 'class_output'),
    html.Div(' by Kacper Glazer', style={'textAlign': 'right'})

])


# callbacks
@app.callback(
    dash.dependencies.Output(component_id = 'class_output', component_property='children'),
    [dash.dependencies.Input(component_id = 'input_text', component_property='value'),
     dash.dependencies.Input(component_id = 'input_model', component_property='value')]
)
def update_output_div_table(text, model):
    model_print = {'LogisticRegression': 'Logistic Regression',
                   'MultinomialNB': 'Naive Bayes',
                   'SVC': 'SVM',
                   'RandomForestClassifier': 'Random Forest',
                   'XGBClassifier': 'XGBoost'}
    text_preprocessed = preprocessing_text(text, 'german')
    model_class = get_classifier(model)
    TFIDF = get_TFIDF()
    text_TFIDF = TFIDF.transform([text_preprocessed])
    prediction = model_class.predict(text_TFIDF)[0]
    if int(prediction) == 0:
        return f'No change of address detected by the model {model_print[model]}'
    else:
        return f'Change of address was detected by the model {model_print[model]}'


if __name__ == '__main__':
    app.run_server(debug=True)
