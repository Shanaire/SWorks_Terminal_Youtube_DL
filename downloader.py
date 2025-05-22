import os
import json

from dataclasses import dataclass, asdict, field

SETTINGS_FILENAME = "appSettings.json"
SETTINGS_FOLDER_NAME = "settings"
CURR_DIR = os.getcwd()

@dataclass
class SettingsMove():
    storageDownloadFolder:str = ""

@dataclass
class SettingsDownload():
    downloadVideoFolder:str = ""
    downloadAudioFolder:str = ""

@dataclass
class SettingsMain():
    download:SettingsDownload = field(default_factory = SettingsDownload)
    move:SettingsMove = field(default_factory=SettingsMove)

def checkGlobalFolders(func):
    settingsFolderPath = f'{CURR_DIR}/{SETTINGS_FOLDER_NAME}'
    settingsFilePath = f'{settingsFolderPath}/{SETTINGS_FILENAME}'
    if (os.path.exists(settingsFolderPath)== False):
        print("Create settings folder")
        os.mkdir(settingsFolderPath)
    if (os.path.exists(settingsFilePath) == False):
        print("Create settings file")
        settingsData = SettingsMain()
        with open(settingsFilePath,"w") as file:
            json.dump(asdict(settingsData), file)
    return func

@checkGlobalFolders
def loadSettings()-> SettingsMain:
    settingsFilePath = f"{CURR_DIR}/{SETTINGS_FOLDER_NAME}/{SETTINGS_FILENAME}"
    with open(settingsFilePath, "r") as file:
        data = json.load(file)
        sDownload = SettingsDownload(**data["download"])
        sMove = SettingsMove(**data["move"])
    return SettingsMain(sDownload,sMove)  

def runCommandVideo(pUrl, pOutCommand):
    global settings
    downloadFolder = settings.download.downloadVideoFolder
    videoQualCommand = "-f 'mp4[height<=1080]+bestaudio'"
    pCommand = f"{videoQualCommand} {pOutCommand} {pUrl}"
    runCommand(pCommand, downloadFolder)

def runCommandAudio(pUrl, pOutCommand):
    global settings
    downloadFolder = settings.download.downloadAudioFolder
    audioExtCommand = "-x --audio-format mp3"
    audioQualCommand = "--audio-quality 0"
    pCommand = f"{pOutCommand} {audioExtCommand} {audioQualCommand} {pUrl}"
    runCommand(pCommand, downloadFolder)

def runCommand(pCommand, pDownloadFolder):
    commandBase = "python ./yt-dlp"
    saveCommand = f"-P {pDownloadFolder}"
    commandToRun = f'{commandBase} {saveCommand} {pCommand}'
    os.system(commandToRun)    

def isPlaylistCheck(pUrl):
    if ('playlist' in pUrl):
        print("\nThis link is for a playlist.")
        res = input("Do you want to download the videos in the Playlist (y or *n*): ")
        return processBoolCheck(res)
    else:
        return "noplaylist"

def isAudioCheck()-> bool:
    res = input("\nDo you want to download audio (y or *n*): ")
    return processBoolCheck(res)
    
def processBoolCheck(pResult)-> bool:
    if (pResult.lower() == "y"):
        return True
    elif (pResult.lower() == "n"):
        return False
    else:
        return False         
    
def ProcessPlaylist(pUrl):
    outCommand = "-o '%(uploader)s/%(playlist)s/%(title)s.%(ext)s'"
    if (isAudioCheck()):
        runCommandAudio(pUrl, outCommand)
    else:
        runCommandVideo(pUrl, outCommand)

def ProcessVideo(pUrl):
    outCommand = "-o '%(uploader)s/%(title)s.%(ext)s'"  
    runCommandVideo(pUrl, outCommand) 

def ProcessAudio(pUrl):
    outCommand = "-o '%(uploader)s/%(title)s.%(ext)s'"
    runCommandAudio(pUrl, outCommand)    

def main():
    global settings
    settings = loadSettings()

    url = input("Enter url: ")

    if (len(url) == 0):
        print("URL string empty, Please add a URL")
        return main()

    res = isPlaylistCheck(url)
    
    if (res == True):
        ProcessPlaylist(url)
    elif (res == 'noplaylist'):
        if (isAudioCheck()):
            ProcessAudio(url)
        else:
            ProcessVideo(url)

    res = input("\nWould you like to download another (y or *n*):")
    if (processBoolCheck(res)):
        main()


if __name__ == "__main__":
    print("\nThanks for using SWorks YT Downloader")
    print("The asterisk(*) highlights the default response")
    print("Happy downloading\n")
    try:
        main() 
    except Exception as error:
        print(f"error: {error}")
    except NameError as error:
        print(f"Name Error: {error}")
    finally:
        print("\nCompleted")                       
        print("Closing Application")        
