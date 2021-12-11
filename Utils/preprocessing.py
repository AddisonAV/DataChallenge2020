import os
import pandas as pd
import numpy as np


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

def fix_invalid_rows(dataset):
    """
    This function fix invalid rows in a dataset
    """

    return dataset.fillna(dataset.mean())


def get_pressure_drop(X):
    UP_Pessure = np.array(X['Upstream_Pressure(psi)'])
    D_Pressure = np.array(X['Downstream_Pressure(psi)'])
    return UP_Pessure-D_Pressure



def get_labels(X):
    pressure = get_pressure_drop(X)
    pressure_threshold_index = np.where(pressure > 20)[0][0]

    pressure_threshold_index
    times = X['Time(s)']
    threshold_time = times[pressure_threshold_index]

    labels = [round(threshold_time - i, 1) if (threshold_time - i) > 0 else 0 for i in times]
    return labels


def prepare_dataset(X):

    pressure = get_pressure_drop(X)
    X = X.drop(['Flow_Rate(ml/m)', 'Upstream_Pressure(psi)','Downstream_Pressure(psi)'], axis=1)
    X['pressure_drop'] = pressure
    return X