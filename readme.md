# SWorks Solutions LTD Youtube Downloader
## Introduction
This allows you to download individual or a playlist of videos from youtube.
You can also download just tue audio if that is what you require.

## Prerequisite
- You will need to have python running on your machine.
- Any recent version will be ok.
- You need to download or have ffmpeg on your machine.

## Usage
#### Download Youtube Video
- Open a terminal, either cmd prompt or powershell or similar
- Use the **python download.py** command to launch the download process. 
- Paste a url from youtube of the video or playlist you want to download.
- You can then specify if you want to download the video or audio.
- Then let the download complete.
- The video or audio will be downloaded in its respected folder along with organising by channel name in the audio or video folder.

#### Move Downloaded Content
- In the settings folder you can specify a folder to move the files to.
- Use the **python move.py** command to move all downloaded videos and audio to tye users specified folder.

#### Clean Up Downloaded Content
- Use the **python clean.py** command to start the clean up process.
- This deletes all files from the downloaded video and audio folders 

## Settings Folder
In the settings folder, you have the appSettings.json file which is used for settingup the video and audio download folder, along with the move folder when we move the downloaded files.
The download and audio folder will be downloaded automatically if it doesn't already exists.


