#!flask/bin/python
import json
from flask import Flask, Response, json, request
from helloworld.flaskrun import flaskrun
import googletrans
from googletrans import Translator

application = Flask(__name__)


@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World hihi'}), mimetype='application/json', status=200)


@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)


@application.route("/language")
def language():
    return googletrans.LANGUAGES


if __name__ == '__main__':
    flaskrun(application)
