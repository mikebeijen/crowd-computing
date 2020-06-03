videoId = "zyOQI995HWU"

if __name__ == "__main__":
    data = open("assessment-" + videoId + ".csv", "r")
    data.readline()

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
