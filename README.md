# Python Testing for Data Science and Stochastic Code

This repo is a companion to the PyData DC 2018 presentation "Do Your Homework! Writing tests for Data Science and Stochastic Code" by David Waterman.

## Quickstart
**Clone the repo, create a new virtual environment, and then:**
 
1. Install the package requirements:
`pip install -r requirements.txt`

1. Install the package in editable mode:
`pip install -e .`

1. Run the tests:
`pytest`

1. Open the generated test report `tests/test-logs/testreport.html` in your browser of choice.

## Resources

#### Pytest Documentation
https://docs.pytest.org
 
#### Good integration practices
https://docs.pytest.org/en/latest/goodpractices.html
 
#### Data Science Testing Tutorial
https://github.com/ericmjl/data-testing-tutorial
 
#### Test Driven Development for Data Science (article)
http://engineering.pivotal.io/post/test-driven-development-for-data-science/

#### Test-Driven Machine Learning
https://www.oreilly.com/library/view/thoughtful-machine-learning/9781449374075/ch01.html

Chapter 1 of _Thoughtful Machine Learning_ by Matthew Kirk

#### Code Complete
https://www.oreilly.com/library/view/code-complete-second/0735619670/

At the presentation a question was asked about whether time spent testing is a good investment. I didn't have any references to support my affirmative response offhand, but the first thing that came to mind after was the book "Code Complete" by Steve McConnell. It is an excellent book overall that I would recommend to anyone looking to improve their software development process, and Chapter 22 in particular addresses testing. Going back through the book I was unable to find hard numbers on the cost savings provided by testing, but I did find some interesting and relevant data, such as that if a software defect is introduced during code construction, it is 10-25 times most costly to fix it after release than it is to find it and fix it during the construction phase.

#### Ynchausti, R. (2001). Integrating Unit Testing Into A Software Development Team’s Process

http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.19.5798

Another reference that provides some data on the value of testing. The conclusion: "Members of the target development team
can expect to spend up to 100% more time implementing
unit tests in conjunction with the production code being
written. Improvements of up to 267% fewer defects can
be achieved through the test-during-coding processes." 
