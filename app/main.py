# coding: utf-8

import json
from urllib.parse import unquote
from flask import Flask, request, render_template
app = Flask(__name__)

from mercury_parser.client import MercuryParser

parser = MercuryParser()


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/parse', methods=['GET'])
def parse():
    url = unquote(request.args.get('url'))
    result = parser.parse_article(url).json()
    return render_template('article.html',
                           title=result['title'],
                           content_title=result['title'],
                           content=result["content"])

