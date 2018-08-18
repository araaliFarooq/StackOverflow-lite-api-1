import unittest
from run import app
from flask import jsonify, json
from app.models import Question
from app import views


class Test_Questions(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_adding_question(self):
        """ Test for posting question successfully """
        response = self.app.post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(dict(question="This is my question 1"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "New question successfully posted")
        self.assertEquals(response.status_code, 201)

    def test_adding_question_with_empty_post(self):
        """ Test for empty post validation """
        
        response = self.app.post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(dict(question=" "),)) 

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "No input was given")
        self.assertEquals(response.status_code, 400)

    def test_adding_question_with_short_post(self):
        """ Test for short post validation """
        
        response = self.app.post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(dict(question="This is"),)) 

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Input has to be at least 10 characters long")
        self.assertEquals(response.status_code, 400)                        