#Deal with dlpoly files

#Imports
# import pandas as pd
from pathlib import Path

from ..csv_files import utils as csv_utils
from ..csv_files import mainpulate as csv_manipulator

#Functions
#Check that the CONFIG file is correct
def check_config_file(path: Path) -> dict:
    """Check that the CONFIG file from a DLPOLY4 project is set up correctly"""
    pass

#Check that the FIELD file is correct
def check_field_file(path: Path | None = None) -> dict:
    """Check that the FIELD file from a DLPOLY4 project is set up correctly"""
    #Check that the path is valid
    if path is None:
        #If no path is given, use the current directory
        path = Path.cwd()

    print(path)

    #Read the FIELD file
    with open(path, "r") as f:
        lines = f.readlines()

    #Check that the FIELD file is not empty
    if len(lines) == 0:
        raise Exception("The FIELD file is empty")
    
    #Check that lines are at max 200 characters long and count comment lines
    comment_lines = 0
    for i,line in enumerate(lines):
        #Remove trailing newline characters
        line = line.rstrip("\n")
        lines[i] = line
        if len(line) == 0:
            continue

        if len(line) > 200:
            raise Exception(f"The FIELD file contains lines longer than 200 characters, line {i}")
        
        if line[0] == "#":
            comment_lines += 1
            lines[i] = ""
        else:
            #Check that words do not exceed 40 characters
            words = line.split()
            for word in words:
                if len(word) > 40:
                    raise Exception(f"The FIELD file contains words longer than 40 characters, line {i}: {word}")
                
    #FIELD file is separated in general info, molecular descriptions and non-bonded parameters sections in that order
    #Check for general info section
    #Contains mandatory: title, units
    #Contains optional: multipolar order


    print(lines)
