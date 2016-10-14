# -*- coding: utf-8 -*-

import os
from mlclassification.dataset import Dataset

# Dataset
dataset = None

def board():
    """
    Simple menu

    """

    if dataset is None:
        load_dataset()

def load_dataset():
    """
    Select dataset and load it

    """
    global dataset

    for index, value in enumerate(os.listdir(os.path.abspath('data'))):
        if value.endswith('.csv'):
            print '{0}. {1}'.format(index + 1, value)

    dataset = Dataset({'name' : raw_input('Filename (with extension) : ')})

def main():
    """
    Start point

    """

    # Show menu
    board()

main()