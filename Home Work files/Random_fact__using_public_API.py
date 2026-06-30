import requests
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


def General_facts():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    response = requests.get(url)

    if response.status_code == 200:
        General_data = response.json()
        print(f"\n{Fore.GREEN}Here's your fact: {General_data['text']}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.YELLOW}Failed to retrieve data{Style.RESET_ALL}")


def Technology_facts():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    response = requests.get(url)

    if response.status_code == 200:
        Tech_data = response.json()
        print(f"\n{Fore.GREEN}Tech fact: {Tech_data['text']}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.YELLOW}Failed to retrieve data{Style.RESET_ALL}")


def History_facts():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    response = requests.get(url)

    if response.status_code == 200:
        History_data = response.json()
        print(f"\n{Fore.RED}History fact: {History_data['text']}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.YELLOW}Failed to retrieve data{Style.RESET_ALL}")


def Science_facts():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    response = requests.get(url)

    if response.status_code == 200:
        Science_data = response.json()
        print(f"\n{Fore.CYAN}Science fact: {Science_data['text']}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.YELLOW}Failed to retrieve data{Style.RESET_ALL}")


print("""
=============================
        FACT GENERATOR
=============================

G - General Facts
T - Technology Facts
H - History Facts
S - Science Facts
Q - Quit
""")

user_input = input("Want to start? Type 'Yes' or 'No': ")

if user_input.capitalize() == "Yes":

    while True:

        user_choice = input(
            "\nEnter first letter (G/T/H/S) or Q to Quit: "
        )

        if user_choice.upper() == "G":
            General_facts()

        elif user_choice.upper() == "T":
            Technology_facts()

        elif user_choice.upper() == "H":
            History_facts()

        elif user_choice.upper() == "S":
            Science_facts()

        elif user_choice.upper() == "Q":
            print(f"{Fore.YELLOW}Thanks for using Fact Generator! 👋")
            break

        else:
            print(f"{Fore.RED}Enter valid input.{Style.RESET_ALL}")

else:
    print("Have a good day and also I don't have that much time. Bye 👍")