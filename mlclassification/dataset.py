# -*- coding: utf-8 -*-

import os
import csv
import numpy

from sklearn import preprocessing

class Dataset:
    """
    Main class of dataset

    """

    def __init__(self, arguments):
        """
        Initialize variables

        :param arguments: dictionary
        """

        self.data = []
        self.target = []

        self._parse(arguments)
        self._categorization()

    def _categorization(self):
        """
        Convert values into categories like 'no' > 0, 'yes' > 1

        """

        le = preprocessing.LabelEncoder()

        for j in range(len(self.data[0])):
            if type(self.data[0][j]) == str:
                le.fit(self._column(j))

                # Transform each value
                # Worst way
                for i in range(len(self.data)):
                    self.data[i][j] = le.transform([self.data[i][j]])

    def _column(self, idx):
        """
        Get column

        :param idx: int
        :return: array
        """

        arr = []

        for i in range(len(self.data)):
            if self.data[i][idx] not in arr:
                arr.append(self.data[i][idx])

        return arr

    def _parse(self, arguments):
        """
        Parse csv file

        :param arguments: dictionary
        """

        # Get name
        self.name = arguments['name']

        # Open file and start parsing
        path = os.path.abspath('data/{0}'.format(self.name))

        with open(path) as csvfile:
            reader = csv.reader(csvfile, quotechar='"', delimiter=';', quoting=csv.QUOTE_ALL, skipinitialspace=True)

            for row in reader:
                arr = []
                for i in range(len(row)):
                    if i == len(row) - 1:

                        # no is equivalent to 0
                        # yes is equivalent to 1
                        if row[i] == 'no':
                            self.target.append(0)
                        else:
                            self.target.append(1)
                    else:
                        if row[i] == 'no':
                            row[i] = 0
                        elif row[i] == 'yes':
                            row[i] = 1
                        else:

                            # convert to float if possible
                            try:
                                row[i] = float(row[i])
                            except ValueError:
                                pass

                        arr.append(row[i])

                self.data.append(arr)