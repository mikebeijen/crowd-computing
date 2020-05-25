videoId = "mii6NydPiqI"
startTime = getRandomInt(0, 100)
endTime = startTime + 10

function process(){
    valueSentiment = null
    valueOpinion = null
    valueClear = null

    elements = document.getElementsByName("sentiment")
    for(i = 0; i < elements.length; i++) {
        if(elements[i].checked) {
            valueSentiment = elements[i].value
        }
    }

    elements = document.getElementsByName("opinion")
    for(i = 0; i < elements.length; i++) {
        if(elements[i].checked) {
            valueOpinion = elements[i].value
        }
    }

    elements = document.getElementsByName("clear")
    for(i = 0; i < elements.length; i++) {
        if(elements[i].checked) {
            valueClear = elements[i].value
        }
    }


    if (valueSentiment== null | valueClear==null | valueOpinion==null) {
        alert("You did answer all the questions.");
    } else {
        alert("You've chosen sentiment: " + valueSentiment + "\n\nVideo id: " + videoId + "\nStart time: " + startTime + "\nEnd time: " + endTime);
        $.post( "/postmethod", {
            video_data: JSON.stringify({choice: valueSentiment, videoid: videoId, starttime: startTime, endtime: endTime})
            }, function(err, req, resp){
            window.location.href = "/";
        });
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