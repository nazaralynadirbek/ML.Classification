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
        self._normalization()

    def _categorization(self):
        """
        Convert values into categories like 'no' > 0, 'yes' > 1

        """

        print 'Categorization...'

        le = preprocessing.LabelEncoder()

        for j in range(len(self.data[0])):
            if type(self.data[0][j]) == str:
                le.fit(self._column(j, unique=True))

                # Transform each value
                # Worst way
                for i in range(len(self.data)):
                    self.data[i][j] = float(le.transform([self.data[i][j]]))

    def _normalization(self):
        """
        Scales all numeric values in the range of [0,1]

        """

        print 'Normalization...'

        for j in range(len(self.data[0])):

            # Get column and find max and min of this column
            column = self._column(j)
            maxv = max(column)
            minv = min(column)

            for i in range(len(self.data)):
                self.data[i][j] = (self.data[i][j] - minv) / (maxv - minv)

    def _column(self, idx, unique=False):
        """
        Get column

        :param idx: int
        :return: array
        """

        arr = []

        if unique:
            for i in range(len(self.data)):
                if self.data[i][idx] not in arr:
                    arr.append(self.data[i][idx])
        else:
            for i in range(len(self.data)):
                arr.append(self.data[i][idx])

        return arr

    def rotate(self):
        """
        Rotate array

        :return: array
        """

        arr = []

        for j in range(len(self.data[0])):

            # Get column
            column = self._column(j)

            # Append to result
            arr.append(column)

        # Append target array
        arr.append(self.target)

        return arr

    def _parse(self, arguments):
        """
        Parse csv file

        :param arguments: dictionary
        """

        print 'Loading...'

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

    def write(self, filename):
        """
        Create file and write data into it

        :param filename: string
        """

        with open(os.path.abspath('output/{0}'.format(filename)), 'wb') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)