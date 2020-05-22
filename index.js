videoId = "mii6NydPiqI"
startTime = getRandomInt(0, 100)
endTime = startTime + 10

function process(){
    value = null

    elements = document.getElementsByName("sentiment")
    for(i = 0; i < elements.length; i++) {
        if(elements[i].checked) {
            value = elements[i].value
        }
    }

    if (value == null) {
        alert("You did not choose a sentiment yet.");
    } else {
        alert("You've chosen: " + value + "\n\nVideo id: " + videoId + "\nStart time: " + startTime + "\nEnd time: " + endTime);
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