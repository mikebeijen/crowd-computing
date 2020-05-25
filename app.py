from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for

import os

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")

@app.route('/', methods=['GET'])
def index():
    title = 'Create the input'
    return render_template('layouts/index.html',
                           title=title)

@app.route('/postmethod', methods = ['POST'])
def post_javascript_data():
    jsdata = request.form['video_data']
    print(jsdata)
    return jsdata


if __name__ == '__main__':
    app.run()