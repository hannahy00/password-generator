########  imports  ##########
from flask import Flask, jsonify, request, render_template
# from generator import password_generator_main
# from generator import test
import json
from generator import *

app = Flask(__name__)

# fake data:
def generateJSONList():
    answer_one = "pear"
    answer_two = "Red Sox"
    answer_three = "car"
    password_length = 12
    have_symbols = True
    have_numbers = True
    have_lowercase = False
    have_uppercase = True
    have_ambiguous_characters = False
    passwordList = {'passwords': []}

    for i in range(10):
        generated_password = password_generator_main(answer_one, answer_two, answer_three, password_length,
                                                        have_symbols, have_numbers, have_lowercase, have_uppercase,
                                                        have_ambiguous_characters)
        print(f"Your password on iteration {i} is: {generated_password}")
        # generated_password = "PEAR^2CAR07^"
        passwordList['passwords'].append({'id': i, 'password': generated_password})

    return json.dumps(passwordList, indent=4)

# def password_serializer(password):
#     return {
#         'id': password.id,
#         'password': password.content
#     }


# Passwords API Route
@app.route('/passwords')
def passwords():
    return generateJSONList()
    # return {"passwords": ["Password1", "Password2", "Password3"]}

# @app.route('/test', methods=['GET', 'POST'])
# def testfn():
#     # GET request
#     if request.method == 'GET':
#         message = {'greeting':'Hello from Flask!'}
#         return jsonify(message)  # serialize and use JSON headers
#     # POST request
#     if request.method == 'POST':
#         print(request.get_json())  # parse as JSON
#         return 'Sucesss', 200

if __name__ == "__main__":
    app.run(debug=True)