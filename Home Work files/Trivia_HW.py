import requests
import colorama
from colorama import Fore, Style
colorama.init()
url = "https://opentdb.com/api.php?amount=5&category=9&difficulty=easy"

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
        
        user_answer = input(f"Enter your answer (1-{len(options)}): ")

        if user_answer not in [str(k) for k in range(1, len(options) + 1)]:
            print(f"{Fore.YELLOW}Invalid input. Please enter a number corresponding to the options.\n{Style.RESET_ALL}")

        elif options[int(user_answer) - 1] == question_data['correct_answer']:
            print(f"{Fore.GREEN}\nCorrect!\n{Style.RESET_ALL}")
            score += 1
        else:
            print(f"{Fore.RED}Wrong! The correct answer was: {question_data['correct_answer']}\n{Style.RESET_ALL}")
    print(f"Your final score is: {score}/{len(trivia_data['results'])}")
else:
    print("Failed to retrieve trivia questions. Please try again later.")
