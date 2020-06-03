var msg = $.ajax({type: "GET", url: "/getmethod", async: false}).responseText;
var obj = JSON.parse(msg)
videoId = obj.videoId
startTime = obj.startTime
endTime = obj.endTime

// Disable button for as long as the video takes
$( document ).ready(function() {
    timeout = (endTime - startTime) * 1000;
    document.getElementById("votebutton").disabled = true;
    setTimeout(function(){document.getElementById("votebutton").disabled = false;},timeout);
    setTimeout(function(){document.getElementById("sentiment-form").style.visibility = 'visible';},timeout);
});

function process(){

    // Declare values and find them in the for-loops
    value = null
    clarityValue = null
    agreeValue = null
    relevantValue = null
    singleSentimentValue = null

    elements = document.getElementsByName("sentiment");
    for(i = 0; i < elements.length; i++) {
        if(elements[i].checked) {
            value = i
        }
    }

    clarityElements = document.getElementsByName("clarity");
    for(i = 0; i < clarityElements.length; i++) {
        if(clarityElements[i].checked) {
            clarityValue = i
        }
    }

    agreeElements = document.getElementsByName("content");
    for(i = 0; i < agreeElements.length; i++) {
        if(agreeElements[i].checked) {
            agreeValue = i
        }
    }

    relevantElements = document.getElementsByName("relevant");
    for(i = 0; i < relevantElements.length; i++) {
        if(relevantElements[i].checked) {
            relevantValue = i
        }
    }

    singleElements = document.getElementsByName("single");
    for(i = 0; i < singleElements.length; i++) {
        if(singleElements[i].checked) {
            singleSentimentValue = i
        }
    }

    clarityText = document.getElementById("clarity-textbox").value;
    generalCommentText = document.getElementById("general-textbox").value;

    if (value == null) {
        alert("You did not choose a sentiment yet.");
    } else if (clarityValue == null) {
        alert("You did not choose whether the video was clear yet.");
    } else if (agreeValue == null) {
        alert("You did not choose whether you agreed with the video yet.");
    } else if (clarityValue == "no" && clarityText == null) {
        alert("You did not explain why the video was unclear yet.");
    } else if (relevantValue == null) {
        alert("You did not choose whether the video was relevant to the coronavirus yet.");
    } else if(singleSentimentValue == null) {
        alert("You did not choose whether it was easy to identify a single dominant sentiment yet.");
    } else {
        if (clarityValue == 0) {
        clarityValue = "yes";
    } else {
        clarityValue = "no";
    }

    if (relevantValue == 0) {
        relevantValue = "yes";
    } else {
        relevantValue = "no";
    }

    if (singleSentimentValue == 0) {
        singleSentimentValue = "yes";
    } else {
        singleSentimentValue = "no";
    }

        if (clarityText == "") {
            clarityText = "-"
        }
        if (generalCommentText == "") {
            generalCommentText = "-"
        }
        console.log(clarityText)
        clarityText = clarityText.replace(",", ";")
        generalCommentText = generalCommentText.replace(",", ";")

        $.post( "/postmethod", {
            video_data: JSON.stringify({videoid: videoId, starttime: startTime, endtime: endTime, value: value, agree:agreeValue,  clarity: clarityValue, claritytext: clarityText, relevanceValue: relevantValue, generalComment: generalCommentText, singleDominantSentiment: singleSentimentValue})
            }, function(err, req, resp){
            window.location.href = "/assessment.html";
        });
    }
}

function getVideoEmbed() {
    htmlResult = '<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/' + videoId + '?controls=0&start=' + startTime + '&end=' + endTime + ';" frameborder="0"></iframe>';
    document.getElementById("video-embed").innerHTML = htmlResult;
}

// Functions to show and hide the clarity textbox
function showTextbox(){
    document.getElementById("clarity-div").style.display = '';
}

function hideTextbox(){
    document.getElementById("clarity-div").style.display = 'none';
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

function trainingLoadAgree() {
    document.getElementById("agree-intro").style.display = 'block';
}

function trainingLoadClear() {
    document.getElementById("clear-intro").style.display = 'block';
}

function trainingDone() {
document.getElementById("next").style.display = 'block';
}

function wrongPositive() {
    alert("Remember, this is a positive example!");
}

function wrongNegative() {
    alert("Remember, this is a negative example!");
}