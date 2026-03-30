import re, random
from colorama import Fore, init

init(autoreset=True)

destination = {
    "beaches":["bali", "Maldives", "Phuket"],
    "mountains":["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities":["Tokyo", "paris", "New york"]
}

jokes = [
    "Why don't programmers like nature? It has too many bugs.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why do Java developers wear glasses? Because they don't see sharp."
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destination:
        suggestions = random.choice(destination[preference])
        print(Fore.GREEN + f"travelBot: how about {suggestions}?")
        print(Fore.CYAN + "travelbot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! {suggestions} is a great choice!")
        elif answer == "no":
            print(Fore.GREEN + "TravelBot: No worries! Let's try something else.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I didn't understand that. Let's try again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I can only recommend beaches, mountains, or cities.")
        

    Show_help()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Here are some packing tips:")
    print(Fore.GREEN + "- Pack light and versatile clothing.")
    print(Fore.GREEN + "- Don't forget your chargers and adapters.")
    print(Fore.GREEN + "- Bring a reusable water bottle.")
    print(Fore.GREEN + "- Pack a first aid kit.")
    Show_help()

def tell_joke():
    joke = random.choice(jokes)
    print(Fore.CYAN + f"TravelBot: Here's a joke for you: {joke}")
    Show_help()

def 



    while True:
        user_input = input(Fore.YELLOW + f"{name}:")
        user_input = normalize_input(user_input)
       
        if "recommend" in user_input:
            recommend()

        elif "pack" in user_input:
            packing_tips()

        elif "joke" in user_input:
            tell_joke()

        elif "help" in user_input:
            Show_help()

        elif "exit" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")


if __name__ == "__main__":
    chat()