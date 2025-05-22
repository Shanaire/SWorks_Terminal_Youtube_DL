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

    res = input("Clean up video (y or *n*): ")
    if (dwn.processBoolCheck(res)):
        cleanSource(sourceVideoFolder)


    res = input("Clean up audio (y or *n*): ")
    if (dwn.processBoolCheck(res)):
        print("Clean Audio")    
        cleanSource(sourceAudioFolder)

    print("\nCompleted!")

if __name__ == "__main__":
    print("File mover developed by SWorks Solutions Ltd")
    print("Thanks for using our tool!\n")
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
    finally:
        print("Closing Application")                
