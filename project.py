#python project quiz application
questions = [
    {
        "question": "Who developed python programming?",
        "options": ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which type of Programming does Python support?",
        "options": ["object oriented programming", "structured programming", "functional programming", "all of the mentioned"],
        "answer": "all of the mentioned"
    },
    {
        "question": "Is Python case sensitive when dealing with identifiers?",
        "options": ["no", "yes", "machine dependent", "none of the mentioned"],
        "answer": "yes"
    },
    {
        "question": "Which of the following is the correct extension of the Python file?",
        "options": [".python", ".pl", ".py", ".p"],
        "answer": ".py"
    },
    {
        "question": "Is Python code compiled or interpreted?",
        "options": ["Python code is both compiled and interpreted", "Python code is neither compiled nor interpreted", "Python code is only compiled", "Python code is only interpreted"],
        "answer": "Python code is both compiled and interpreted"
    },  
    {
        "question": "Which keyword is used for function in Python language?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "All keywords in Python are in",
        "options": ["capitalized", "lower case", "upper case", "none of the mentioned"],
        "answer": "none of the mentioned"
    },   
    {
        "question": "Which of the following is used to define a block of code in Python language?",
        "options": ["indentation", "key", "brackets", "all of the mentioned"],
        "answer": "indentation"
    },  
    {
        "question": "Which of the following character is used to give single-line comments in Python?",
        "options": ["//", "#", "!", "/*"],
        "answer": "#"
    },  
    {
        "question": "Select all correct ways to copy a dictionary in Python",
        "options": ["dict2 = dict1.copy()", "dict2 = dict(dict1)", "dict2 = dict1", "all of the above"],
        "answer": "dict2 = dict1.copy()"
    }   
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)

        user_answer = input("Enter your choice: ").strip().capitalize()
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    
    print(f"You scored {score}/{len(questions)}")

run_quiz(questions)
#end
