videoId = "zyOQI995HWU"


class Assessment:
  def __init__(self, videoId, startTime, endTime, sentimentValue, agreementValue, clarityValue, clarityExplanation, relevanceValue, generalComment, singleSentimentValue):
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


if __name__ == "__main__":
    # Initialize data and datastructure
    data = open("assessment-" + videoId + ".csv", "r")
    data.readline()
    allAssessments = set()

    # Read all assessments and add to set
    for line in data:
        line = line.split(",")
        startTime = line[1]
        endTime = line[2]
        sentimentValue = line[3]
        agreementValue = line[4]
        clarityValue = line[5]
        clarityExplanation = line[6]
        relevanceValue = line[7]
        generalComment = line[8]
        singleSentimentValue = line[9]
        assessment = Assessment(videoId, startTime, endTime, sentimentValue, agreementValue, clarityValue, clarityExplanation, relevanceValue, generalComment, singleSentimentValue)
        allAssessments.add(assessment)


