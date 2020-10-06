import json
from flask import Flask, request, jsonify
from flask.views import MethodView
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

# import Hien model
# Define param
# call model with text, param


def change_model_param(param):
    print(param)


@app.route('/setter', methods=['POST'])
def setter():
    if request.method == "POST":
        try:
            change_model_param(request.get_json())
        except:
            return 'error'
    return 'oka'


def sentiment_analysis(sentence):
    response = {
        'text': sentence,
        'label': 'Negative'
    }
    return jsonify(response)
app.add_url_rule('/sean/<string:sentence>', 'sentiment_analysis', sentiment_analysis)

 
def index():
    return "ok"
app.add_url_rule('/', 'index', index)


app.run(host='localhost', port=80, debug=True) 