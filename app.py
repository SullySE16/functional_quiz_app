import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample quiz questions and answers (you can replace these with your own questions)
# Sample quiz questions and answers (you can replace these with your own questions)
questions = [
    {
        'question': 'What is the capital of France?',
        'image': 'question1.jpg',  # Image file for question 1
        'choices': ['New York', 'London', 'Paris', 'Tokyo'],
        'correct_choice': 'Paris'
    },
    {
        'question': 'What is 2 + 2?',
        'image': 'question2.jpg',  # Image file for question 2
        'choices': ['3', '4', '5', '6'],
        'correct_choice': '4'
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'image': 'question3.jpg',  # Image file for question 3
        'choices': ['Mars', 'Saturn', 'Jupiter', 'Neptune'],
        'correct_choice': 'Jupiter'
    }
]



# Global variable to keep track of the current question index
current_question_index = 0
correct_answer_tally = 0

@app.route('/', methods=['GET', 'POST'])
def quiz():
    global current_question_index
    global correct_answer_tally
    
    finish = False

    

    while finish == False:

        if request.method == 'POST':
            # Get the user's answer from the form
            user_answer = request.form.get('choice')

            # Check if the user's answer is correct
            correct_answer = questions[current_question_index]['correct_choice']

            is_correct = user_answer == correct_answer

            if is_correct:
                correct_answer_tally+=1

            # Move to the next question
            current_question_index += 1

            if current_question_index < len(questions):
                return render_template('quiz.html', question=shuffle_choices(questions[current_question_index]), is_correct=is_correct)
            else:
                finish=True
                return render_template('results.html', is_correct=is_correct, score_tally=correct_answer_tally)

        return render_template('quiz.html', question=shuffle_choices(questions[current_question_index]), is_correct=None)

def shuffle_choices(question):
    # Randomly shuffle the choices for a given question
    shuffled_choices = question['choices'][:]
    random.shuffle(shuffled_choices)
    question['choices'] = shuffled_choices
    return question

@app.route('/restart')
def restart_quiz():
    global current_question_index
    global correct_answer_tally
    current_question_index = 0
    correct_answer_tally = 0
    return redirect(url_for('quiz'))

if __name__ == '__main__':
    app.run(debug=True)
