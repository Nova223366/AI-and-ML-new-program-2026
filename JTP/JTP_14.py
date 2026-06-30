import requests
import os
import json
import colorama
from colorama import Fore, Style
colorama.init(autoreset = True)

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def saving_user_data(fact):
    file_name = "User_data.json"

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(fact)

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def get_random_facts():
    respones = requests.get(url)
    if respones.status_code == 200:
        fact_data = respones.json()
        print(f"{Fore.GREEN}Hers your random fact; {fact_data['text']}{Style.RESET_ALL}")

        saving_user_data({
            "id": fact_data["id"],
            "text": fact_data["text"],
            "source": fact_data["source"]
        })
    else:
        print(f"{Fore.RED}Cant reitrive random fact{Style.RESET_ALL}")


get_random_facts()    