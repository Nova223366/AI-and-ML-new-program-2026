import random
from colorama import Fore, Style, init

init(autoreset=True)

chars = input("Enter your password for strength checking: ")

if chars.isalpha() and chars.isdigit() and chars.isupper() and chars.islower():
    print(Fore.GREEN + "Your password is strong!")
else:
    print(Fore.RED + "Your password is weak!")
