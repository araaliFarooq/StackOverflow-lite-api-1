from flask import jsonify
import re

class FieldValidation:

    def validate_entered_id(self,id):
        try:
           _id = int(id)
        except ValueError:
            return jsonify({"message": "Id should be an interger"}), 400

    def validate_input(self, input):

        if not input:
            return jsonify({"message": "No input was given"}), 400
        if len(input) < 10:
            return jsonify({"message": "Input has to be at least 10 characters long"}), 400    

    def validate_type(self, input):
        if re.match("^[1-9]\d*(\.\d+)?$", input) != None:
            return True
        return False
