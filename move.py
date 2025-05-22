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
    print("Starting the moving process")
    global settings
    settings = dwn.loadSettings()
    destinationDownloadFolder = settings.move.storageDownloadFolder
    sourceVideoFolder = settings.download.downloadVideoFolder 
    sourceAudioFolder = settings.download.downloadAudioFolder

    videoDest = f'{destinationDownloadFolder}'
    audioDest = f'{destinationDownloadFolder}'

    moveSource(sourceVideoFolder, videoDest)
    moveSource(sourceAudioFolder, audioDest)

    print("\nMoving files complete!")

if __name__ == "__main__":
    print("File mover developed by SWorks Solutions Ltd")
    print("Thanks for using our tool!\n")
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
    finally:
        print("Closing Application")                
