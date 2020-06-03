from flask import Flask, render_template, json, request, jsonify
import json, csv, random, os

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
    with open("assessment-" + jsdata["videoid"] + ".csv", mode="a+", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        if os.stat("assessment-" + jsdata["videoid"] + ".csv").st_size == 0:
            csvwriter.writerow(["Video id, Start time, End time, Sentiment value, Agreement value, Clarity value, Clarity explanation, Relevance value, General comment, Single dominant sentiment value"])

        csvwriter.writerow([jsdata["videoid"], int(jsdata["starttime"]), int(jsdata["endtime"]), jsdata["value"], jsdata["agree"], jsdata["clarity"], jsdata["claritytext"], jsdata["relevanceValue"], jsdata["generalComment"], jsdata["singleDominantSentiment"]])
        csvfile.close()

    return "", 200


@app.route('/getmethod', methods= ['GET'])
def get_javascript_data():
    videoId, startTime, endTime = get_video_split()
    return jsonify(videoId=videoId, startTime=startTime, endTime=endTime)


def get_video_split():
    all_video_splits = open("data/res.csv", "r")
    all_video_info = dict()
    video_assessment_amounts = dict()

    for video_split in all_video_splits:
        video_split = video_split.split(",")
        video_id = video_split[0]
        video_start_time = video_split[1]
        video_end_time = video_split[2]

        all_video_info[video_start_time] = (video_id, video_end_time)
        video_assessment_amounts[video_start_time] = 0

    try:
        all_video_assessments = open("assessment-" + video_id + ".csv", "r")
        all_video_assessments.readline()
    except FileNotFoundError:
        random_start_time = random.choice(list(video_assessment_amounts.keys()))
        video_id, video_end_time = all_video_info[random_start_time]
        return video_id, random_start_time, video_end_time

    for assessment in all_video_assessments:
        assessment_split = assessment.split(",")
        start_time = assessment_split[1]
        video_assessment_amounts[start_time] += 1

    minimally_graded_split = min(video_assessment_amounts, key=video_assessment_amounts.get)
    video_id, video_end_time = all_video_info[minimally_graded_split]
    return video_id, minimally_graded_split, video_end_time


if __name__ == '__main__':
    app.run()
