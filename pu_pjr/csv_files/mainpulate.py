#Functions to manipulate csv data

#Imports
import pandas as pd
from pathlib import Path

from . import utils

#Functions
#Calculate the average, median, mode and standar deviation of a column
def calculate_stats(df: pd.DataFrame, column: str) -> tuple:
    """Calculates the average, median, and mode of a column"""
    average = df[column].mean()
    median = df[column].median()
    mode = df[column].mode()[0]
    std = df[column].std()
    return (average, median, mode, std)

#Calculate the average, median, and mode of all columns
def calculate_all_stats(df: pd.DataFrame) -> dict:
    """Calculates the average, median, and mode of all columns"""
    stats = {}
    for column in df.columns:
        stats[column] = calculate_stats(df, column)
    return stats


