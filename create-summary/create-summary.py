import operator, os, pytube, shutil

videoId = "zyOQI995HWU"
summaryLengthSeconds = 100
positive = True


# Saves a part of the video to a seperate file
def crop(start: str, end: str, input: str, output: str):
    command = "ffmpeg -y -i " + input + " -ss  " + start + " -to " + end + " -c copy " + output
    os.system(command)


# Download the YouTube video if it is not downloaded yet
def downloadVideo():
    if not os.path.exists("full-video-" + videoId):
        yt = pytube.YouTube('https://www.youtube.com/watch?v=' + videoId)
        video = yt.streams.first()
        video.download("full-video-" + videoId, filename=videoId)


class Assessment:
  def __init__(self, videoId: str, startTime: int, endTime: int, sentimentValue: int, agreementValue: int, clarityValue: str, clarityExplanation: str, relevanceValue: str, generalComment: str, singleSentimentValue: str):
    self.videoId = videoId
    self.startTime = startTime
    self.endTime = endTime
    self.sentimentValue = sentimentValue
    self.agreementValue = agreementValue
    self.clarityValue = clarityValue
    self.clarityExplanation = clarityExplanation
    self.relevanceValue = relevanceValue
    self.generalComment = generalComment
    self.singleSentimentValue = singleSentimentValue


class Split:
    def __init__(self, startTime: int, endTime: int, totalSentimentScore: int, totalAmountOfAssessments: int):
        self.startTime = startTime
        self.endTime = endTime
        self.length = self.endTime - self.startTime
        self.totalSentimentScore = totalSentimentScore
        self.totalAmountOfAssessments = totalAmountOfAssessments
        self.averageSentimentScore = 0

    def addSentiment(self, sentiment: int):
        self.totalSentimentScore += sentiment
        self.totalAmountOfAssessments += 1
        self.averageSentimentScore = self.totalSentimentScore/self.totalAmountOfAssessments

    def __repr__(self):
        return "(Start time: " + str(self.startTime) + ", End time: " + str(self.endTime) + ", Split length: " + str(self.length) + ", Total sentiment score: " + str(self.totalSentimentScore) + ", Total amount of assessments: " + str(self.totalAmountOfAssessments) + ", Average sentiment score: " + str(self.averageSentimentScore) + ")\n"


if __name__ == "__main__":
    # Initialize data and datastructure
    downloadVideo()
    data = open("../assessment-" + videoId + ".csv", "r")
    data.readline()
    allAssessments = set()
    allSplits = dict()
    resultingSplits = list()

    # Read all assessments and add to set
    for line in data:
        line = line.split(",")
        startTime = int(line[1])
        endTime = int(line[2])
        sentimentValue = int(line[3])
        agreementValue = int(line[4])
        clarityValue = line[5]
        clarityExplanation = line[6]
        relevanceValue = line[7]
        generalComment = line[8]
        singleSentimentValue = line[9]
        assessment = Assessment(videoId, startTime, endTime, sentimentValue, agreementValue, clarityValue, clarityExplanation, relevanceValue, generalComment, singleSentimentValue)
        allAssessments.add(assessment)

    # Build split objects in dictionary
    for assessment in allAssessments:
        startTime = assessment.startTime
        if startTime not in allSplits:
            split = Split(startTime, assessment.endTime, 0, 0)
            allSplits[startTime] = split
        allSplits[startTime].addSentiment(assessment.sentimentValue)

    # Cast splits to list and sort on decreasing average sentiment
    allSplits = list(allSplits.values())
    allSplits.sort(key=operator.attrgetter('averageSentimentScore'), reverse=not positive)

    # Get as many splits as needed to fill the minimal summary length
    while summaryLengthSeconds > 0:
        split = allSplits.pop()
        resultingSplits.append(split)
        summaryLengthSeconds -= split.length

    # Sort resulting splits by start time
    resultingSplits.sort(key=operator.attrgetter('startTime'))

    # Create video splits
    counter = 1
    mergeList = open("mergelist-" + videoId + ".txt", "w+")
    os.system("mkdir video-splits-" + videoId)
    for split in resultingSplits:
        input = os.getcwd() + "\\full-video-" + videoId + "\\" + videoId + ".mp4"
        output = os.getcwd() + "\\video-splits-" + videoId + "\\" + str(counter) + ".mp4"
        crop(str(split.startTime), str(split.endTime), input, output)
        counter += 1
        mergeList.write("file '" + output + "'\n")

    # Concatenate video splits
    os.system("ffmpeg -f concat -safe 0 -i mergelist-" + videoId + ".txt -c copy output.mp4")

    # Remove leftover files
    mergeList.close()
    os.remove("mergelist-" + videoId + ".txt")
    shutil.rmtree("video-splits-" + videoId)
    shutil.rmtree("full-video-" + videoId)
