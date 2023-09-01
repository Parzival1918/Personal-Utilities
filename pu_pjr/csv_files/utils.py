#General csv utilities

#Imports
import pandas as pd
from pathlib import Path

#Functions
def read_csv(path: Path) -> pd.DataFrame:
    """Reads csv file and returns a pandas dataframe"""
    df = pd.read_csv(path)
    return df

def write_csv(df: pd.DataFrame, path: Path) -> None:
    """Writes a pandas dataframe to a csv file"""
    df.to_csv(path, index=False)
    return None

def extract_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Extracts columns from a pandas dataframe"""
    df = df[columns]
    return df

def drop_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Drops columns from a pandas dataframe"""
    df = df.drop(columns=columns)
    return df

def replace_values(df: pd.DataFrame, column: str, old_value: str, new_value: str) -> pd.DataFrame:
    """Replaces values in a pandas dataframe"""
    df[column] = df[column].replace(old_value, new_value)
    return df

def replace_nan_values(df: pd.DataFrame, column: str, new_value: str) -> pd.DataFrame:
    """Replaces nan values in a pandas dataframe"""
    df[column] = df[column].fillna(new_value)
    return df

def replace_nan_values_with_mean(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Replaces nan values in a pandas dataframe with the mean of the column"""
    df[column] = df[column].fillna(df[column].mean())
    return df

def replace_nan_values_with_median(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Replaces nan values in a pandas dataframe with the median of the column"""
    df[column] = df[column].fillna(df[column].median())
    return df

def replace_nan_values_with_mode(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Replaces nan values in a pandas dataframe with the mode of the column"""
    df[column] = df[column].fillna(df[column].mode()[0])
    return df

#Return rows of df that contain a certain value in a column
def return_rows_with_value(df: pd.DataFrame, column: str, value: str) -> pd.DataFrame:
    """Returns rows of a pandas dataframe that contain a certain value in a column"""
    df = df[df[column] == value]
    return df

