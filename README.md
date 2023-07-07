# File-Sorter
The Python File Explorer is used to easily sort files from one folder of unsorted content to an another folder.

## How Does It Work?
It uses: 
* os 
* Tkinter (Making the UI)
* shuttil (Adding and Cloning files)

To achieve the sorting system, as well as if it exists it uses a Fullname or else just use the extension name (Free to update the list)

## Other

To open, open **FileSorter.py** not **FileSorterDictionary.py**. To add more default names add to **FileSorterDictionary.py**, formated as ```"BaseName": "FullName"``` in to the *FileTypeNames* Dictionary.

### Addition
#### Negatives
* Won't override files
#### Positives
* Can files to folder that had already been sorted
* Can Change Sorted & Unsorted Folders