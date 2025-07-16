import os
import json

from dataclasses import dataclass, asdict, field

SETTINGS_FILENAME = "appSettings.json"
SETTINGS_FOLDER_NAME = "settings"
CURR_DIR = os.getcwd()

def runCommand():
    commandBase = "python ./yt-dlp --update"
    commandToRun = f'{commandBase}'
    os.system(commandToRun)    


def main():

    res = input("Start Update y or *n*:")
    if (res == "y"):
        runCommand()

if __name__ == "__main__":
    print("\nThanks for using SWorks YT Downloader")
    print("This is to update to the latest version of the yt-dlp downloader")
    print("Happy updating\n")
    try:
        main() 
    except Exception as error:
        print(f"error: {error}")
    except NameError as error:
        print(f"Name Error: {error}")
    finally:
        print("\nCompleted")                       
        print("Closing Application")        
