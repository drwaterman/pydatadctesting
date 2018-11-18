from datetime import datetime
from pydatadctesting import experiment
import os
import pandas as pd
import pytest
from scipy.stats import normaltest


@pytest.fixture
def sales_records():
    file_path = os.path.join(os.path.dirname(__file__), 'test-data/100_sales_records.csv')
    return pd.read_csv(file_path)


def test_get_time_str():
    assert experiment.get_time_str() == datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")


def test_increment():
    assert experiment.increment(5) == 6
    assert experiment.increment(-5) == -4
    assert experiment.increment(-2.5) == -1.5
    assert experiment.increment(987654321987654321) == 987654321987654322
    with pytest.raises(TypeError):
        experiment.increment('a')
    with pytest.raises(TypeError):
        experiment.increment(None)


def test_average(sales_records):
    assert experiment.average([1, 2, 3, 4, 5]) == 3
    assert experiment.average([.1, .2, .3, .4, .5]) == .3

    assert experiment.average(sales_records['Total Profit'].tolist()) == \
        pytest.approx(441681.9839999)

    with pytest.raises(ZeroDivisionError):
        experiment.average([])
    with pytest.raises(TypeError):
        experiment.average(1)
    with pytest.raises(TypeError):
        experiment.average(None)
    with pytest.raises(TypeError):
        experiment.average(['a', 'b', 'c'])
    with pytest.raises(TypeError):
        experiment.average(['1', '2', 'c'])


def test_generate_random_normal_dist():
    dist = experiment.generate_random_normal_dist()
    is_norm = normaltest(dist)
    pvalue = is_norm[1]
    assert pvalue > 0.01


@pytest.mark.xfail(reason="Model's current benchmark is 0.93")
def test_classify_posts_pipeline():
    grid_search = experiment.classify_posts_pipeline()
    assert grid_search.best_score_ > 0.95
