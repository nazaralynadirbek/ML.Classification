# -*- coding: utf-8 -*-

import os
import warnings

from mlclassification.dataset import Dataset
from mlclassification.classifier import Classifier

# Dataset
dataset = None

# Classifier
classifier = None

def board():
    """
    Simple menu

    """
    global classifier

    # Check if dataset is loaded
    if dataset is None:
        load_dataset()

        # Classifier
        classifier = Classifier(dataset)

    while True:

        # Print parent menu
        print '1. Compare accuracies'
        print '2. Show the scatter plot'
        print '3. Output'

        usr_raw = raw_input('Select : ')

        if usr_raw == '1':

            # Print sub menu
            print '1. k-nearest neighbors'
            print '2. Decision tree'
            print '3. Naive Bayes'
            print '4. Linear Regression'
            print '5. Logistic Regression'
            print '6. All'

            # Create array
            usr_choice = raw_input('Select : ')
            usr_choice = [int(x) for x in usr_choice.split(',')]

            classifier.compare(usr_choice)
        elif usr_raw == '2':

            # Display scatter plot
            classifier.scatter()

        elif usr_raw == '3':

            # Write data into file
            # Filename

            usr_choice = raw_input('Filename : ')
            dataset.write(usr_choice)
        else:
            break

def load_dataset():
    """
    Select dataset and load it

    """
    global dataset

    for index, value in enumerate(os.listdir(os.path.abspath('data'))):
        if value.endswith('.csv'):
            print '{0}. {1}'.format(index + 1, value)

    # Dataset
    dataset = Dataset({'name': raw_input('Filename (with extension) : ')})

def main():
    """
    Start point

    """

    # Ignore some warnings
    warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

    # Show menu
    board()

main()