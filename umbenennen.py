import os
from pathlib import Path

def renamePicturenumbers():
    """
    Renames picture numbers in the current directory.
    
    This function renames picture files with the extension '.tif' in the current directory.
    The new filename format is '<prefix>_<index>.tif', where <prefix> is the first block of the original filename
    and <index> is the index of the file in the directory content.
    """
    directorycontent = os.listdir()
    for file in directorycontent:
        if file.endswith(".tif"):
            f = Path(file)
            name, extension = f.stem, f.suffix
            nameblocks = f.stem.split("_")
            newFilename = f"{nameblocks[0]}_{str(directorycontent.index(file))}{extension}"
            f.rename(newFilename)

if __name__ == "__main__":
    os.chdir(os.getcwd()+"/aufnahmen")
    renamePicturenumbers()
    os.chdir(os.getcwd()+"/Plain")
    renamePicturenumbers()