import collections
from datetime import datetime
import numpy as np
import numbers
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline


def get_time_str():
    now = datetime.now()
    time_str = datetime.strftime(now, "%Y-%m-%d %H:%M")
    return time_str


def increment(num):
    if not isinstance(num, numbers.Number):
        raise TypeError("Not a number")
    return num + 1


def average(number_iter):
    if not isinstance(number_iter, collections.Iterable):
        raise TypeError("number_list must be an iterable")
    if not all(isinstance(d, numbers.Number) for d in number_iter):
        raise TypeError("All elements must be numeric")
    return sum(number_iter)/float(len(number_iter))


def generate_random_normal_dist(mu=100, sigma=25, n=1000):
    return np.random.normal(mu, sigma, n)


def classify_posts_pipeline():
    categories = ['alt.atheism', 'talk.religion.misc',]
    data = fetch_20newsgroups(subset='train', categories=categories)
    pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier()),
    ])
    parameters = {
        'vect__max_df': (0.5, 0.75, 1.0),
        'vect__ngram_range': ((1, 1), (1, 2)),  # unigrams or bigrams
        'clf__alpha': (0.00001, 0.000001),
        'clf__penalty': ('l2', 'elasticnet'),
    }
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1)
    grid_search.fit(data.data, data.target)
    print("Best score: %0.3f" % grid_search.best_score_)
    print("Best parameters set:")
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))
    return grid_search


if __name__ == "__main__":
    print("The current date time time is:", get_time_str())
    print("If you increment 5 you get", increment(5))
    print("The average of 3 and 10 is", average([3, 10]))
    print("A random number drawn from N(100, 25) is", generate_random_normal_dist()[0])
    print("Running classify posts pipeline...")
    classify_posts_pipeline()

