import unittest
from run import app
from flask import jsonify, json
from app.models import Question
from app import views

class Test_Viewing_Answers(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_fetching_available_answers(self):
        '''Test to fetch all questions'''
        response = self.app.post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(dict(question="This is my question 1"),))

        response2 = self.app.post("/api/v1/questions/1/answer",
            content_type='application/json',
            data=json.dumps(dict(answer="This is my answer 1"),))    
            
        reply = json.loads(response2.data.decode())
        response3 = self.app.get("/api/v1/answers",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response3.data.decode())
        self.assertEquals(reply2["message"],"Successfully viewed Answers")
        self.assertEquals(response3.status_code, 200)
