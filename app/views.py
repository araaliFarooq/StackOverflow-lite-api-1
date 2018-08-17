from app import app
from flask import request , jsonify, json
from app.models import Answer, Question

all_questions = []
all_answers = []


@app.route("/api/v1/questions", methods=["POST"])
# posting a single question
def post_question():
    data = request.get_json()
    question = data.get("question")
    qstn_id = len(all_questions) + 1

    new_question = Question(qstn_id , question)
    all_questions.append(new_question)
    return jsonify({"message":"New question successfully posted"}), 201


@app.route("/api/v1/questions", methods=["GET"])
# fetching all questions
def get_all_questions():
    if len(all_questions) > 0:
        return jsonify({
            "message":"Successfully viewed Questions",
            "Available questions":[     
                question.__dict__ for question in all_questions
            ]
        }),200
    return jsonify({"message":"No Question has been posted yet"}), 404


@app.route("/api/v1/questions/<question_id>", methods=["GET"])
# get a specific question
def get_a_question(question_id):
    for question in range(len(all_questions)):
        if ((all_questions[question]["qstn_id"]) == int(question_id)):
            return jsonify({
            "message":"Successfully viewed Question",
            "Question":[     
                all_questions[question]["question"]
            ]
    }),200
    return jsonify({
        "message":"No such question is available",
    }),400
