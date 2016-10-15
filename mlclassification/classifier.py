# -*- coding: utf-8 -*-

from sklearn import metrics
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

        # Divide dataset into two subsets - train set and test set
        self.train_data, self.test_data, \
        self.train_target, self.test_target = train_test_split(dataset.data, dataset.target, train_size=0.5, random_state=0)

    def _knn(self, **kwargs):
        """
        k-nearest neighbors algorithm

        """

        neigh = KNeighborsClassifier(n_neighbors=3)
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
            print 'NOT ADDED'

    def _logit(self, **kwargs):
        """
        Logistic Regression

        """

        logit = LogisticRegression()
        logit.fit(self.train_data, self.train_target)

        if 'compare' in kwargs:
            print 'NOT ADDED'

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