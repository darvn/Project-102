import os

import shutil

source = "C:/Users/mingm/Downloads"
destination = "C:/Users/mingm/Desktop/Coding/Python/document_files"

listOfFiles = os.listdir(source)
#print(listOfFiles)

for i in listOfFiles:
    name, extension = os.path.splitext(i)
    #print(extension)
    if extension == "":
        continue
    if extension in [".png", ".jpg", ".gif", ".jpeg", ".jfif"]:
        path1 = source + "/" + i
        path2 = destination + "/" + "image_files"
        path3 = destination + "/" + "image_files" + "/" + i 

        if os.path.exists(path2):
            print("Moving..." + i + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving..." + i + "...")
            shutil.move(path1 , path3)