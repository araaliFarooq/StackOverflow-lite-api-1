import unittest
from run import app
from flask import jsonify, json
from app.models import Question
from app import views

class Test_Viewing_Questions(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_fetching_available_questions(self):
        '''Test to fetch all questions'''
        response = self.app.post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(dict(question="This is my question 1"),))
            
        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/questions",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"],"Successfully viewed Questions")
        self.assertEquals(response2.status_code, 200)



    def test_get_single_question(self):
        '''Test to fetch single question'''
        response = self.app.post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(dict(question="This is my question 1"),))
        response = self.app.post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(dict(question="This is my question 2"),))
            
        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/questions/2",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        
        self.assertEquals(response2.status_code, 200)


    def test_get_single_question_with_improper_id(self):
        '''Test to fetch single question with improper id'''
        response = self.app.post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(dict(question="This is my question 1"),))
        response = self.app.post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(dict(question="This is my question 2"),))
            
        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/questions/q",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"],"Id should be an interger")
        self.assertEquals(response2.status_code, 400)    

    


