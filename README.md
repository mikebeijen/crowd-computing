# CS4145 Crowd Computing
## Group 1 - Agreeable Group Name

## How to Run Locally
For this to run, you will need flask, `pip install flask`

Make sure you have the csv file containing the videoID's, create a folder in the root called `data/` and add the `res.csv` file to this folder.

Afterwards run `flask run`, and the results will be in the results folder.

## How to run on Google Compute Engine
1. Update the files you've updated by removing the old ones and uploading the new ones
2. run `sudo python3 app.py`
3. Visit http://34.90.159.99/

## Building the video
When you've gathered enough data, you can run `create-summary.py`, which will generate a video of a minimal specified length. Make sure to have the `ffmpeg.exe` in the `create-summary` folder to make sure the command work. Your video will be available at `create-summary/output.mp4`.