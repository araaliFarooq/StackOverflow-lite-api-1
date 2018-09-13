# StackOverflow-lite-api-1
[![Build Status](https://travis-ci.org/araaliFarooq/StackOverflow-lite-api-1.svg?branch=master)](https://travis-ci.org/araaliFarooq/StackOverflow-lite-api-1)
[![Coverage Status](https://coveralls.io/repos/github/araaliFarooq/StackOverflow-lite-api-1/badge.svg?branch=master)](https://coveralls.io/github/araaliFarooq/StackOverflow-lite-api-1?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/304f736722854a9fba99e3bd660c03ca)](https://www.codacy.com/app/araaliFarooq/StackOverflow-lite-api-1?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=araaliFarooq/StackOverflow-lite-api-1&amp;utm_campaign=Badge_Grade)



## About
This is an API for a Q&A application that allows users, register on the application to be able post questions to which other users can post answers to or answer questions other users have posted.

## Features
- Get all questions posted on the application
- Get a particuler question posted on the application
- Post a question on the application.
- Post an answer to a particular question.

## Other features
- View all answers posted on the application


## Tools Used
[Flask](http://flask.pocoo.org/) - web microframework for Python
## Requirements
Python 2.7.x - 3.x.x+
## Run (Use) on your local machine
First clone the repository
```sh
   $ git clone https://github.com/araaliFarooq/StackOverflow-lite-api-1
   ```
   Head over to the cloned directory, create a virtual environment, use pip to install the requirements, then run the app
   ```
    $ cd StackOverflow-lite-api-1
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python run.py
```

#### Endpoints to create, read user questions and answers
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/v1/questions | False | Post a question
GET | /api/v1/questions | True | Fetch all questions on the application
GET | /api/v1/questions/<question_id> | True | Fetch a single question
GET | /api/v1/questions/<question_id>/answer | False | Post an answer to a question
GET | /api/v1/answers | True | View all answers

## Authors
[Araali Sseruwu Farooq](https://github.com/araalifarooq)
