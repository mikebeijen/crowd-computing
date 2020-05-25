videoId = "mii6NydPiqI"
startTime = getRandomInt(0, 100)
endTime = startTime + 10

function process(){
    // Declare values and find them in the for-loops
    value = null
    clarityValue = null
    agreeValue = null

    elements = document.getElementsByName("sentiment");
    for(i = 0; i < elements.length; i++) {
        if(elements[i].checked) {
            value = elements[i].value
        }
    }

    clarityElements = document.getElementsByName("clarity");
    for(i = 0; i < clarityElements.length; i++) {
        if(clarityElements[i].checked) {
            clarityValue = clarityElements[i].value
        }
    }

    agreeElements = document.getElementsByName("content");
    for(i = 0; i < agreeElements.length; i++) {
        if(agreeElements[i].checked) {
            agreeValue = agreeElements[i].value
        }
    }

    // Alert if any of the values are null, submit values otherwise
    if (value == null) {
        alert("You did not choose a sentiment yet.");
    } else if (clarityValue == null) {
        alert("You did not choose whether the video was clear yet.");
    } else if (agreeValue == null) {
        alert("You did not choose whether you agreed with the video yet.");
    } else {
        alert("Sentiment: " + value + "\nClear: " + clarityValue + "\nAgree:" + agreeValue + "\n\nVideo id: " + videoId + "\nStart time: " + startTime + "\nEnd time: " + endTime);
        location.reload();
    }
}

function getVideoEmbed() {
    htmlResult = '<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/' + videoId + '?controls=0&start=' + startTime + '&end=' + endTime + ';" frameborder="0"></iframe>';
    document.getElementById("video-embed").innerHTML = htmlResult;
}

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function start() {
    window.location.replace("positive.html");
}

function posNext() {
    window.location.replace("negative.html");
}

function negNext() {
    window.location.replace("assessment.html");
}