from nltk.tokenize import sent_tokenize
from pytube import YouTube
import re

# This file segments a video based on a sliding window
# using its captions.
#

# Helper method that converts timestamp to sec
def getSec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

# Main method
if __name__ == "__main__":

    # Add the ID of the video to be segmented here
    YOUTUBE_VIDEO_ID = "zyOQI995HWU"
    source = YouTube('https://www.youtube.com/watch?v=' + YOUTUBE_VIDEO_ID)
    en_caption = source.captions.get_by_language_code('en')
    en_caption_convert_to_srt =(en_caption.generate_srt_captions())

    
    # Save the caption to a file named Output.txt
    print(en_caption_convert_to_srt)
    text_file = open("vids/Output.txt", "w")
    text_file.write(en_caption_convert_to_srt)
    text_file.close()

    # Read fragments and corresponding text
    # and put it into a dictionary of fragnebts
    text = {"fragments": []}
    with open(r"vids/Output.txt", "r") as f:
        try:
            print(f.readline())

            while True:
                # Pick the timestamps and text from the caption
                timeString = f.readline()[:-1]
                textString = f.readline()[:-1]
                if timeString == "":
                    raise Exception("Done with file")
                
                beginTime = timeString[:-21]
                endTime = timeString[-12:-4]

                # Skip empty lines
                f.readline()
                f.readline()

                # Make into and add fragment
                fragment = {
                    'beginTime': beginTime,
                    'endTime': endTime,
                    'text': textString 
                }
                text['fragments'].append(fragment)                

        except:
            pass

    # Build sentences from fragments
    beginTime = ""
    endTime = ""
    sentence = ""

    res = {'sentences': []}

    for fragment in text['fragments']:
        if endTime != "":
            beginTime = fragment['beginTime']

        # Split based on .?!
        splitted = re.split('[\.?!]', fragment['text'])

        if len(splitted) != 1:
            endTime = fragment['endTime']
            sentence += splitted[0]
            print(beginTime + " -> " + endTime + ":  " + sentence)
            res['sentences'].append({'beginTime': beginTime, 'endTime': endTime, 'text': sentence})

            sentence = splitted[1]

        else:
            sentence += fragment['text']

    # Split: sliding window based. Size of window is 5. 

    with open(r"vids/res.csv", "w") as f:
        for i in range(len(res['sentences']) - 4):
            if i % 2 != 0: 
                beginTime = getSec(res['sentences'][i]['beginTime'])
                endTime = getSec(res['sentences'][i+4]['endTime'])
                print(YOUTUBE_VIDEO_ID + "," + str(beginTime) + "," + str(endTime))
                f.write(YOUTUBE_VIDEO_ID + "," + str(beginTime) + "," + str(endTime) + "\n")



    




            
