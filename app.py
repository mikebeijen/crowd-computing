from flask import Flask, render_template, make_response, json
from flask import redirect, request, jsonify, url_for
import json, csv, os
from random import randint

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
    jsdata = json.loads(jsdata)
    with open("results/assessment-" + jsdata["videoid"] + ".csv", mode="a+", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([jsdata["videoid"], jsdata["starttime"], jsdata["endtime"], jsdata["value"], jsdata["clarity"], jsdata["agree"]])
        csvfile.close()

    return "", 200


@app.route('/getmethod', methods= ['GET'])
def get_javascript_data():
    videos = list()
    with open('data/res.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, ['videoId', 'startTime', 'endTime'])
        for row in reader:
            videos.append(row)

    random = randint(0, len(videos) - 1)
    return jsonify(videoId=videos[random]['videoId'], startTime=videos[random]['startTime'], endTime=videos[random]['endTime'])


if __name__ == '__main__':
    app.run()