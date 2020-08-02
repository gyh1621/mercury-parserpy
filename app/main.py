# coding: utf-8

import json
from urllib.parse import unquote
from flask import Flask, request, render_template, url_for
app = Flask(__name__)

from mercury_parser.client import MercuryParser

parser = MercuryParser()


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/parse', methods=['GET'])
def parse():
    url = unquote(request.args.get('url'))
    style = request.args.get('style')
    result = parser.parse_article(url).json()
    if style == 'dark':
        css = url_for('static', filename='dark.css')
    else:
        css = url_for('static', filename='bright.css')
    return render_template('article.html',
                           title=result.get('title', 'No Title'),
                           content_title=result.get('title', 'No Title'),
                           content=result.get('content', str(result)),
                           css=css
                           )

