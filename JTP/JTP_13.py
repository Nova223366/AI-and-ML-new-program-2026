import requests
import colorama
from colorama import Fore, Style
import json
import os

colorama.init(autoreset=True)

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def save_fact(fact):
    filename = "facts.json"

    # Load existing facts if the file exists
    if os.path.exists(filename):
        with open(filename, "r") as file:
            facts = json.load(file)
    else:
        facts = []

    # Add the new fact
    facts.append(fact)

    # Save the updated list
    with open(filename, "w") as file:
        json.dump(facts, file, indent=4)

def get_random_fact():
    response = requests.get(url)

    if response.status_code == 200:
        fact_data = response.json()

        print(f"{Fore.GREEN}\nDid you know? {fact_data['text']}\n")

        # Save the fact
        save_fact({
            "id": fact_data["id"],
            "text": fact_data["text"],
            "source": fact_data["source"]
        })

    else:
        print(f"{Fore.RED}Failed to retrieve a fact.")

while True:
    user_input = input("Press Enter to get a random fact or type 'q' to quit: ")

    if user_input.lower() == "q":
        break

    get_random_fact()