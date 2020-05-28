var msg = $.ajax({type: "GET", url: "/getmethod", async: false}).responseText;
var obj = JSON.parse(msg)
videoId = obj.videoId
startTime = obj.startTime
endTime = obj.endTime

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

    clarityText = document.getElementById("clarity-textbox").value;

    alert(clarityValue);
    alert(clarityText);

    if (value == null) {
        alert("You did not choose a sentiment yet.");
    } else if (clarityValue == null) {
        alert("You did not choose whether the video was clear yet.");
    } else if (agreeValue == null) {
        alert("You did not choose whether you agreed with the video yet.");
    } else if (clarityValue != null && clarityText == null) {
        alert("You did not explain why the video was unclear yet.");
    } else {
        $.post( "/postmethod", {
            video_data: JSON.stringify({videoid: videoId, starttime: startTime, endtime: endTime, value: value, agree:agreeValue,  clarity: clarityValue, clarityText: clarityText})
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

