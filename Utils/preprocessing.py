import os
import pandas as pd


def get_file_names(folder_path):
    """This function obtain a list of all files inside a specific folder

    Args:
        folder_path (string): path where your desired folder is located

    Returns:
        list: list of files inside directory
    """    

    # Obtain files inside directory
    file_names = os.listdir(os.path.join(folder_path))
    print('File names: ', file_names)
    print('Number of files: ', len(file_names))
    
    
    return file_names
