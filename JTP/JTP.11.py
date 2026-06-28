import requests
import colorama
from colorama import Fore, Style
import time
colorama.init()

user_name = input(f"Enter your name: {Fore.BLUE}")
print(Style.RESET_ALL, end="")

while True:
    user_input = input(f"{Fore.GREEN}Want to know cat facts? (yes/no): {Style.RESET_ALL}")

    if user_input.lower() == "yes":
        response = requests.get("https://catfact.ninja/fact")
        if response.status_code == 200:
            cat_fact = response.json()["fact"]
            loading_animation = ["", ".", "..", "...", "...."]
            for i in range(5):
                print(f"\r{Fore.YELLOW}Loading cat fact{loading_animation[i]}{Style.RESET_ALL}", end="\r", flush=True)
                time.sleep(0.5)
            print(" " * 30, end="\r")
            print(f"\n{Fore.CYAN}Here's a cat fact for you, {user_name}: {cat_fact}{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}Sorry, Cats where sleeping right now, so we cant know about them.{Style.RESET_ALL}")
    else:
        print(f"{Fore.CYAN}You know a cat can help you to free from streess and anxiety{Style.RESET_ALL}")
        break

