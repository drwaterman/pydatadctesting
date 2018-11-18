#!/usr/bin/env bash
if [ ! -d tests/test-logs ]
then
    mkdir tests/test-logs
fi

pytest --html=tests/test-logs/testreport.html --self-contained-html \
--cov=experiment --cov-report term-missing -r aPp tests