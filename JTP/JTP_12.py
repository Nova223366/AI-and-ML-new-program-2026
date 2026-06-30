import requests
import colorama
from colorama import Fore, Style

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_random_technology_fact():
    response = requests.get(url)
    #print(f"Response: {response}")  # Debugging line to check the status code
    if response.status_code == 200:
        fact_data = response.json()
        #print(f"fact_data: {fact_data}")  # Debugging line to check the response content
        print(f"{Fore.GREEN}\nDid you know? {fact_data['text']}\n{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Failed to retrieve a fact. Please try again later.{Style.RESET_ALL}")

while True:
    user_input = input("Press enter to get a random tech fact or type 'q' to quit: ")
    if user_input.lower() == 'q':
        break
    get_random_technology_fact()
