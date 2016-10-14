# -*- coding: utf-8 -*-

import os
import csv

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