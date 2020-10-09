import json
from flask import Flask, request, jsonify
from flask.views import MethodView
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

# import Hien model
# Define param
# call model with text, param
param = {
    "embedding" : "character",
    "model": "lstm",
    "activate": "H",
    "loss": "A"
}


from sentiment_analysis import SentimentAnalysis as sa

     

def change_model_param(new_param):
    global param
    print(param)
    param = new_param
    print(param)


@app.route('/setter', methods=['POST'])
def setter():
    if request.method == "POST":
        try:
            change_model_param(request.get_json())
        except:
            return 'error'
    return 'ok'

#
def sentiment_analysis(sentence):
    global param

    print(sentence)

    # param_map = {'lstm': 'lstm', 'LSTM': 'lstm', 'Word': 'word', 'Character': 'character', 'character': 'character'}

    paramX = {'model' : 'cnn',
            'textprocessor' : 'character',
            'activation' : 'linear',
            'loss' : 'crossEntropy'}
    
    out = sa(paramX, sentence)
    #{'Positive': 0, 'Negative': 1, 'Normal': 2}
    label = ""
    if out == 0:
        label = "Positive"
    if out == 1:
        label = "Negative"
    if out == 2:
        label = "Normal"


    response = {
        'text': sentence,
        'label': label,
        'param': paramX
    }


    print(response)
    return jsonify(response)
app.add_url_rule('/sean/<string:sentence>', 'sentiment_analysis', sentiment_analysis)
#
 
#
def index():
    return "ok"
app.add_url_rule('/', 'index', index)
#

app.run(host='localhost', port=80, debug=True) 