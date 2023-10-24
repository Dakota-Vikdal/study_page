from flask import Flask, render_template, request
from questions_options import python_questions

app = Flask(__name__)



@app.route("/")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name, questions=python_questions)


@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    answers = request.form # This will contain the selected answers
    
    return render_template('result.html', answers=answers)