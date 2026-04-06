from colorama import Fore, Style, init

init(autoreset=True)

chars = input("Enter your password for strength checking: ")

if chars.isalpha() and chars.isdigit() and chars.isupper() and chars.islower():
    print(f"{Fore.GREEN}Your password is strong!{Style.RESET_ALL}")

elif chars.isdigit() and chars.isupper():
    print(f"{Fore.YELLOW} your password need some lowercase letters and some special characters!{Style.RESET_ALL}")

else:
    print(f"{Fore.RED}Your password is weak!{Style.RESET_ALL}")

