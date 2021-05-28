
import os
import time
import shutil
def main():
    deletedFoldersCount = 0
    deletedFilesCount = 0
    path = "C:\Users\Mahesh\Documents\Vivek\Python Vivek\folderA\css"
    days = 30
    seconds = time.time()-(days*24*3600)
    if os.path.exists(path):
        for rootFolder, folders, files in os.walk(path):
            if seconds>=getFileorFolderAge(rootFolder):
                removeFolder(rootFolder)
                deletedFoldersCount += 1
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder, folder)
                    if seconds>=getFileorFolderAge(folderPath):
                        removeFolder(folderPath)
                        deletedFoldersCount += 1
                for file in files:
                    filePath = os.path.join(rootFolder, file)
                    if seconds>=getFileorFolderAge(filePath):
                        removefile(filePath)
                        deletedFilesCount += 1
def getFileorFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

def removefile(path):
    if not os.remove(path):
        print("successfuly removed file!!")
    else:
        print("unsuccessful!!")

def removeFolder(path):
    if not shutil.rmtree(path):
        print("successfuly removed folder!!")
    
    else:
        print("unsuccessful!!")
# if __name__ == '__main__':
    # main()