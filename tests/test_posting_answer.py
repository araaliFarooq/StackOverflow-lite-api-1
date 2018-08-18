import unittest
from run import app
from flask import jsonify, json
from app.models import Answer
from app import views


class Test_Posting_Answer(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_posting_answer(self):
        """ Test for posting an answer """
        response = self.app.post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(dict(question="This is my question 1"),))

        response2 = self.app.post("/api/v1/questions/1/answer",
            content_type='application/json',
            data=json.dumps(dict(answer="This is my answer 1"),))

        reply = json.loads(response2.data)
        self.assertEquals(reply["message"], "Answer successfully posted to question")
        self.assertEquals(response2.status_code, 201)

    def test_posting_answer_with_improper_question_id(self):
        """ Test for posting an answer with improperquestion_id"""
        response = self.app.post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(dict(question="This is my question 1"),))

        response2 = self.app.post("/api/v1/questions/a/answer",
            content_type='application/json',
            data=json.dumps(dict(answer="This is my answer 1"),))

        reply = json.loads(response2.data)
        self.assertEquals(reply["message"], "Id should be an interger")
        self.assertEquals(response2.status_code, 400)


    def test_posting_answer_with_wrong_question_id(self):
        """ Test for posting an empty answer post"""
        response = self.app.post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(dict(question="This is my question 1"),))

        response2 = self.app.post("/api/v1/questions/1/answer",
            content_type='application/json',
            data=json.dumps(dict(answer="  "),))

        reply = json.loads(response2.data)
        self.assertEquals(reply["message"], "No input was given")
        self.assertEquals(response2.status_code, 400)

        response2 = self.app.post("/api/v1/questions/1/answer",
            content_type='application/json',
            data=json.dumps(dict(answer="This is"),))

        reply = json.loads(response2.data)
        self.assertEquals(reply["message"], "Input has to be at least 10 characters long")
        self.assertEquals(response2.status_code, 400)    
        
                             