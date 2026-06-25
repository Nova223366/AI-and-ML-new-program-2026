import requests

url = "https://opentdb.com/api.php?amount=3&category=9&difficulty=easy"

response = requests.get(url)

if response.status_code == 200:
    trivia_data = response.json()
    score = 0

    for i, question_data in enumerate(trivia_data["results"]):
        print(f"Question {i + 1}: {question_data['question']}")
        options = question_data['incorrect_answers'] + [question_data['correct_answer']]
        options = sorted(options)

        for j, option in enumerate(options):
            print(f"{j + 1}. {option}")
        
        user_answer = input("Your answer (enter the option number(1/2/3/4)): ")

        if options[int(user_answer) - 1] == question_data['correct_answer']:
            print("Correct!\n")
            score += 1

        else:
            print(f"Wrong! The correct answer was: {question_data['correct_answer']}\n")
        print("\n")
    print(f"Your final score is: {score}/{len(trivia_data['results'])}")
else:
    print("Failed to retrieve trivia questions. Please try again later.")
