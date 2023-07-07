import os, shutil, sys
from tkinter import *
from tkinter import filedialog
from os import path
from FileSorterDictionary import FILE_TYPE_NAMES

UI_FONT: tuple[str, int]; GUI = ("Arial", 12), None

UnsortedDir: str; SortedDir: str = "Unsorted", "Sorted"

def GetFolder(newpath: str): #Creates Folder! Not Get
    if not path.exists(newpath): #Checks if the path exists else make the folder
        os.makedirs(newpath) #Creates Folder

def GetClassName(file: os.DirEntry) -> str:
    fileClass: str = path.basename(file).split('.')[1].lower()
    
    a: str = FILE_TYPE_NAMES.get(fileClass, fileClass.upper)

    if a.upper() == fileClass: #The File Class is equal to
        print(f"The file class name is {fileClass} doesn't exist", file=sys.stderr)
    
    return a

def FolderLoad(name: str, file: os.DirEntry) -> None:
    folderDir: str = f"{SortedDir}\\{name}" #The Folder Name
            
    if not path.exists(folderDir): #Checks if the file doesn't exist
        shutil.copytree(path.abspath(file), folderDir) #Copies Folder

def FileLoad(name: str, file: os.DirEntry) -> None:
    fileClass: str; toFolder: str = GetClassName(file), f"{SortedDir}\\{fileClass}" #The get file fullname; The Folder Name

    GetFolder(toFolder) #Creates Folder

    if not path.exists(f"{toFolder}\\{name}"): #Checks if the file doesn't exist
        shutil.copyfile(path.abspath(file), f"{toFolder}\\{name}") #Clones the file

def EveryFile(inside: os._ScandirIterator) -> None:

    for _, file in enumerate(inside):
        name: str = path.basename(file)

        if path.isfile(file): #Is File
            FileLoad(name, file)
        else: #Is Folder
            FolderLoad(name, file)
        
        print(f"File {name} has been completed")

    print("The sorting has been completed")

def startup():
    global UnsortedDir, SortedDir

    inSorted: os._ScandirIterator = os.scandir(UnsortedDir) #Gets all files/folders in a Folder 

    EveryFile(inSorted) #Iterators every child of "inSorted"

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

    GUI: UI = UI()

    GUI.root.mainloop()

CreateUI()