import os
import json
import downloader as dwn

def cleanSource(pSource):
    command = f"rm {pSource}/* -r -v"
    runCommand(command)

def runCommand(pCommand):
    os.system(pCommand)

def main():
    print("Starting the cleaning process")
    global settings
    settings = dwn.loadSettings()
    sourceVideoFolder = settings.download.downloadVideoFolder 
    sourceAudioFolder = settings.download.downloadAudioFolder

    res = input("\nClean Video Folder (*y* or n): ")
    if (dwn.processBoolCheckYes(res)):
        cleanSource(sourceVideoFolder)


    res = input("\nClean Audio Folder (*y* or n): ")
    if (dwn.processBoolCheckYes(res)):  
        cleanSource(sourceAudioFolder)

    print("\nClean Completed!")

if __name__ == "__main__":
    print("SW FOLDER CLEANER")
    print("Developed by SWorks Solutions Ltd")
    print("\nCleans the audio and video folders by\ndeleting all files in the selected folders.")
    print("\nThanks for using our tool!\n")
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
    finally:
        print("Closing Application")                
