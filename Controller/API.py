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
    "embedding" : "ha",
    "model": "Haa",
    "activate": "H",
    "loss": "A"
}

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
    response = {
        'text': sentence,
        'label': 'Negative',
        'param': param
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