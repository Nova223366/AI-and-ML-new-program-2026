import random
from colorama import Fore, Style, init

# initialize colorama
init(autoreset=True)

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*"

def generate_password():
    length = random.randint(8, 16)
    return ''.join(random.choice(chars) for _ in range(length))

# generate password
password = generate_password()

# print with colors
print(Fore.CYAN + "🔐 Generated Password:")
print(Fore.GREEN + Style.BRIGHT + password)