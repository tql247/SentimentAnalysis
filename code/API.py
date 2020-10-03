import json
from flask import Flask, request, jsonify
from flask.views import MethodView

app = Flask(__name__)
 
def index():
    return "ok"
app.add_url_rule('/', 'index', index)


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
    return jsonify(sentence)
app.add_url_rule('/sean/<string:sentence>', 'sentiment_analysis', sentiment_analysis)


app.run(host='localhost', port=80, debug=True) 