from Question import Question 

question_prompts = [
    "what is 2 + 2 \n a) 4\n b) 6\n c) 2\n\n",
    "What colour is a banana?\n a) Green\n b) Yellow\n c) Orange\n\n",
    
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " right")

run_quiz(questions)
