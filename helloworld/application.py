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
    print("language")
    return json.jsonify(googletrans.LANGUAGES)


@application.route("/translator", methods=['POST'])
def translator():
    if request.method == 'POST':
        print("---------translator---------")
        translators = Translator()
        get_data = request.get_json()
        origin = get_data['origin_word']
        dest = get_data['trans_language']
        result = translators.translate(origin, dest=dest)
        print(get_data)
        print(origin)
        print(dest)
        print(result)
        return json.jsonify(
            origin_launguage=result.src,  # src = 원본 언어
            trans_language=result.dest,  # dest = 타겟 언어
            origin_word=result.origin,  # origin = 번역할 글자
            trans_word=result.text,  # text = 번역된 글자
        )


if __name__ == '__main__':
    flaskrun(application)
