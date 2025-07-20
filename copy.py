import os
import json
import downloader as dwn

def cleanSource(pSource):
    command = ""
    runCommand(command)

def moveSource(pSource, pDestination):
    command = f"cp -v -r {pSource} {pDestination}"
    runCommand(command)

def runCommand(pCommand):
    os.system(pCommand)

def main():
    print("Starting the copying process")
    global settings
    settings = dwn.loadSettings()
    destinationDownloadFolder = settings.move.storageDownloadFolder
    sourceVideoFolder = settings.download.downloadVideoFolder 
    sourceAudioFolder = settings.download.downloadAudioFolder

    videoDest = f'{destinationDownloadFolder}'
    audioDest = f'{destinationDownloadFolder}'

    res = input("\nCopy Video Content (*y* or n): ")
    if (dwn.processBoolCheckYes(res)):
        moveSource(sourceVideoFolder, videoDest)
    
    res = input("\nCopy Audio Content (*y* or n): ")
    if (dwn.processBoolCheckYes(res)):
        moveSource(sourceAudioFolder, audioDest)

    print("\nCoping files complete!")

if __name__ == "__main__":
    print("SW FILE COPIER")
    print("Developed by SWorks Solutions Ltd")
    print("\nTo copy files from a source folder to its destinstion folder.")
    print("\nThanks for using our tool!\n")
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
    finally:
        print("Closing Application")                
