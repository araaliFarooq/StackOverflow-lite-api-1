from app import app
from flask import request, jsonify, json
from app.models import Answer, Question

all_questions = []


@app.route("/api/v1/questions", methods=["POST"])
# posting a single question
def post_question():
    data = request.get_json()
    question = data.get("question")
    qstn_id = len(all_questions) + 1

    new_question = Question(qstn_id , question)
    all_questions.append(new_question)
    return jsonify({"message":"New question successfully posted"}), 201
