import os, shutil, sys
from tkinter import *
from tkinter import filedialog
from os import path

UnsortedDir = "Unsorted"
SortedDir = "Sorted"

FileTypeNames = {
    "txt": "Text",

    "js": "JavaScript",
    "json": "JavaScript",

    "b": "Brainfuck",
    "bf": "Brainfuck",

    "py": "Python",

    "png": "Pictures",
    "jepg": "Pictures",
}

def GetFolder(newpath):
    if not path.exists(newpath):
        os.makedirs(newpath)

def GetClassName(file):
    fileClass: str = path.basename(file).split('.')[1].lower()
    
    a: str = FileTypeNames.get(fileClass, fileClass)

    if a == fileClass:
        print(f"The file class name is {fileClass} doesn't exist", file=sys.stderr)
    
    return a

def EveryFile(inside):

    for index, file in enumerate(inside):
        name: str = path.basename(file)

        if path.isfile(file):
            
            fileClass: str = GetClassName(file)

            toFolder: str = f"{SortedDir}\\{fileClass}"

            GetFolder(toFolder)

            shutil.copyfile(path.abspath(file), f"{toFolder}\\{name}")
        else:
            folderDir = f"{SortedDir}\\{name}"
            
            if not path.exists(folderDir):
                shutil.copytree(path.abspath(file), folderDir)
        
        print(f"File {name} has been completed")

    print("The sorting has been completed")

def startup():
    global UnsortedDir, SortedDir

    inSorted = os.scandir(UnsortedDir)

    EveryFile(inSorted)

UI_FONT = ("Arial", 12)

class UI:

    def OnSortButtonPress(self):
        global UnsortedDir, SortedDir

        SortedDir = filedialog.askdirectory()
        self.SortData.config(text=f"Unsorted: {path.basename(UnsortedDir)}, Sorted: {path.basename(SortedDir)}")

        print(SortedDir)

    def OnUnsortButtonPress(self):
        global UnsortedDir, SortedDir

        UnsortedDir = filedialog.askdirectory()
        self.SortData.config(text=f"Unsorted: {path.basename(UnsortedDir)}, Sorted: {path.basename(SortedDir)}")

        print(UnsortedDir)

    def __init__(self):
        self.root = Tk()
        self.root.title("File Sorter")
        self.root.geometry("350x200")

        self.SortButton = Button(self.root, font=UI_FONT, height=1, text="Sorted Folder", command=self.OnSortButtonPress)
        self.SortButton.grid(column=0, row=0, padx=5, pady=10)

        self.UnsortButton = Button(self.root, font=UI_FONT, height=1, text="Unsorted Folder", command=self.OnUnsortButtonPress)
        self.UnsortButton.grid(column=0, row=1, padx=5, pady=10)

        self.SortData = Label(self.root, font=UI_FONT, height=1, text="")
        self.SortData.grid(column=0, row=2, padx=10, pady=10)

        self.button = Button(self.root, font=UI_FONT, height=1, text="Sort into Folder", command=startup)
        self.button.grid(column=0, row=3, padx=10, pady=10)

def CreateUI():
    global GUI

    GUI = UI()

    GUI.root.mainloop()

CreateUI()

#startup()