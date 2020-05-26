from flask import Flask, render_template, make_response, json
from flask import redirect, request, jsonify, url_for
import json, csv, os
import pandas as pd

import os

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")

@app.route('/', methods=['GET'])
def index():
    title = 'Create the input'
    return render_template('layouts/index.html',
                           title=title)

@app.route('/positive.html', methods=['GET'])
def positivePage():
    title = 'Create the input'
    return render_template('layouts/positive.html',
                           title=title)

@app.route('/negative.html', methods=['GET'])
def negativePage():
    title = 'Create the input'
    return render_template('layouts/negative.html',
                           title=title)

@app.route('/assessment.html', methods=['GET'])
def assessmentPage():
    title = 'Create the input'
    return render_template('layouts/assessment.html',
                           title=title)

@app.route('/postmethod', methods = ['POST'])
def post_javascript_data():
    jsdata = request.form['video_data']
    print(jsdata)
    jsdata = json.loads(jsdata)
    with open("assessment-" + jsdata["videoid"] + ".csv") as csvfile:
        csvwriter = csv.writer(csvfile, delimeter=',', quotechar="", quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([jsdata["videoid"], jsdata["starttime"], jsdata["endtime"], jsdata["value"], jsdata["clarity"], jsdata["agree"]])
        csvfile.close()

@app.route('/getmethod', methods= ['GET'])
def get_javascript_data():
    df = pd.read_csv('data/res.csv')
    print(df)

    return jsonify(videoId="mii6NydPiqI", startTime=10, endTime=20)


if __name__ == '__main__':
    app.run()