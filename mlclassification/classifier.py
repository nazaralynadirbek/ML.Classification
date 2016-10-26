# -*- coding: utf-8 -*-

import math
import numpy

from sklearn import metrics
from matplotlib import pyplot
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

class Classifier:
    """
    Main class for all classifiers

    """

    def __init__(self, dataset):
        """
        Initialize variables

        :param dataset: object
        """

        # Train size
        self.train_size = 0.3

        # Rotated dataset
        self.dataset = dataset
        self.rotated = dataset.rotate()

        # Divide dataset into two subsets - train set and test set
        self.train_data, self.test_data, \
        self.train_target, self.test_target = train_test_split(self.dataset.data, self.dataset.target, train_size=self.train_size, random_state=0)

    def _knn(self, **kwargs):
        """
        k-nearest neighbors algorithm

        """

        neigh = KNeighborsClassifier(n_neighbors=5)
        neigh.fit(self.train_data, self.train_target)

        if 'compare' in kwargs:
            print 'KNN ACCURACY :', metrics.accuracy_score(self.test_target, neigh.predict(self.test_data))

    def _dt(self, **kwargs):
        """
        Decision tree

        """

        dt = DecisionTreeClassifier()
        dt.fit(self.train_data, self.train_target)

        if 'compare' in kwargs:
            print 'DT ACCURACY :', metrics.accuracy_score(self.test_target, dt.predict(self.test_data))

    def _nv(self, **kwargs):
        """
        Naïve-base

        """

        nv = GaussianNB()
        nv.fit(self.train_data, self.train_target)

        if 'compare' in kwargs:
            print 'NV ACCURACY :', metrics.accuracy_score(self.test_target, nv.predict(self.test_data))

    def _lrm(self, **kwargs):
        """
        Linear Regression

        """

        reg = LinearRegression()
        reg.fit(self.train_data, self.train_target)

        if 'compare' in kwargs:
            print 'LRM ACCURACY :'
            print '------ %-R^2 :', 'NOT ADDED'
            print '------ RMSE  :', math.sqrt(metrics.mean_squared_error(self.test_target, reg.predict(self.test_data)))
            print '------ MSE   :', metrics.mean_squared_error(self.test_target, reg.predict(self.test_data))

    def _logit(self, **kwargs):
        """
        Logistic Regression

        """

        logit = LogisticRegression()
        logit.fit(self.train_data, self.train_target)

        if 'compare' in kwargs:
            print 'LOGIT ACCURACY :'
            print '------ %-R^2 :', 'NOT ADDED'
            print '------ RMSE  :', math.sqrt(metrics.mean_squared_error(self.test_target, logit.predict(self.test_data)))
            print '------ MSE   :', metrics.mean_squared_error(self.test_target, logit.predict(self.test_data))

    def compare(self, usr_choice=[4]):
        """
        Compare accuracies of selected algorithms

        :param usr_choice: array
        """

        # k-nearest
        if 1 in usr_choice:
            self._knn(compare=True)

        # Decision tree
        if 2 in usr_choice:
            self._dt(compare=True)

        # Naive Bayes
        if 3 in usr_choice:
            self._nv(compare=True)

        # Linear Regression
        if 4 in usr_choice:
            self._lrm(compare=True)

        # Logistic Regression
        if 5 in usr_choice:
            self._logit(compare=True)

        # All
        if 6 in usr_choice:
            self._knn(compare=True)
            self._dt(compare=True)
            self._nv(compare=True)
            self._lrm(compare=True)
            self._logit(compare=True)

    def _bfit_line(self, x, y):
        """
        Best fit line

        :return: float, float
        """

        xbar = sum(x) / len(x)
        ybar = sum(y) / len(y)

        numr = sum([xi*yi for xi, yi in zip(x, y)]) - len(x) * xbar * ybar
        denr = sum([xi**2 for xi in x]) - len(x) * xbar**2

        return (ybar - (numr/denr) * xbar), (numr / denr)

    def scatter(self):
        """
        Show scatter plot

        """

        print 'Drawing...'

        for i in range(len(self.rotated)):
            for j in range(i + 1, len(self.rotated)):

                # Calculate correlation
                corrcoef = numpy.corrcoef(self.rotated[i], self.rotated[j])[0, 1]

                if corrcoef >= 0.5:
                    pyplot.scatter(self.rotated[i], self.rotated[j], s=30, color='r')

                    # Best fit line
                    a, b = self._bfit_line(self.rotated[i], self.rotated[j])
                    yfit = [a + b * xi for xi in self.rotated[i]]
                    pyplot.plot(self.rotated[i], yfit, 'g')
                    pyplot.show()