import os
import downloader as dwn

def processFolder(pFolder):
    print(f'Processing {pFolder} folder')

    toProcess = False
    listOfDir  = os.listdir(pFolder)

    for item in listOfDir:
        content = os.listdir(f"{pFolder}/{item}")

        for cItem in content:
            if cItem.startswith("."):
                toProcess = True
                print(f'Folder to rename: {cItem}')

                removedDotName = cItem[1:]
                updatedName = f'Dot{removedDotName}'
                
                cItemPath = f'{os.getcwd()}{pFolder[1:]}/{item}/{cItem}'
                cItemPathNew = f'{os.getcwd()}{pFolder[1:]}/{item}/{updatedName}'
                print(f'Old Path: {cItemPath}')
                print(f'New Path: {cItemPathNew}')

                os.rename(cItemPath,cItemPathNew)
                
    if toProcess == False:
        print(f'Nothing to process for {pFolder} folder.')

def main():
    print("Starting the renaming process")
    global settings
    settings = dwn.loadSettings()
    sourceVideoFolder = settings.download.downloadVideoFolder
    sourceAudioFolder = settings.download.downloadAudioFolder      

    processFolder(sourceVideoFolder)
    processFolder(sourceAudioFolder)
    
if __name__ == "__main__":
    main()
