# -*- coding: utf-8 -*-

import os
from mlclassification.dataset import Dataset

# Dataset
dataset = None

def board():
    """
    Simple menu

    """

    print '---------------------------------------------------------'
    print '| Graded Assignment Project / Nazaraly Nadirbek / END03 |'
    print '---------------------------------------------------------'

    if dataset is None:
        print 'Dataset has not been loaded, please, select one :'
        choose_file()

def choose_file():
    """
    Select dataset and load it

    """

    for index, value in enumerate(os.listdir(os.path.abspath('data'))):
        if value.endswith('.csv'):
            print '{0}. {1}'.format(index + 1, value)

    filename = raw_input('Filename (with extension) : ')
    dataset = Dataset({'name' : filename})

def main():
    """
    Start point

    """

    # Show menu
    board()

main()