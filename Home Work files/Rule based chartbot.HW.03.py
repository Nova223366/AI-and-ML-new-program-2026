import re
import random
import datetime
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? It has too many bugs.",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!",
    "Why do Java developers wear glasses? Because they don't see sharp."
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def save_history(name, user_input):
    with open("chat_history.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {name}: {user_input}\n")

def get_weather():
    city = input(Fore.YELLOW + "Which city's weather? ")
    conditions = ["Sunny", "Rainy", "Cloudy", "Snowy"]
    temp = random.randint(-5, 35)
    print(Fore.GREEN + f"TravelBot: It's currently {random.choice(conditions)} in {city} with a temperature of {temp}°C.")

def get_time():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(Fore.GREEN + f"TravelBot: The local time is {now}.")

def get_news():
    headlines = [
        "New travel corridor opens in Asia.",
        "Flight prices expected to drop this summer.",
        "Top 10 hidden gems in Europe revealed.",
        "Space tourism reaches new milestone."
    ]
    print(Fore.GREEN + f"TravelBot: Latest news: {random.choice(headlines)}")

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = normalize_input(input(Fore.YELLOW + "You: "))

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if "yes" in answer:
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        else:
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that category.")

def packing_tips():
    location = input(Fore.YELLOW + "Where to? ")
    days = input(Fore.YELLOW + "How many days? ")
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.\n- Bring chargers/adapters.\n- Check the weather forecast.")

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def show_help():
    print(Fore.GREEN + "\nCommands:")
    print("- 'recommend' for travel spots")
    print("- 'pack' for packing tips")
    print("- 'joke' for a laugh")
    print("- 'weather' for local forecast")
    print("- 'time' for current time")
    print("- 'news' for travel updates")
    print("- 'exit' to quit\n")

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ") or "Traveler"
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    
    show_help()

    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"{name}: "))
        save_history(name, user_input)

        if re.search(r"recommend|suggest", user_input):
            recommend()
        elif re.search(r"pack", user_input):
            packing_tips()
        elif re.search(r"joke|funny", user_input):
            tell_joke()
        elif "weather" in user_input:
            get_weather()
        elif "time" in user_input:
            get_time()
        elif "news" in user_input:
            get_news()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == "__main__":
    chat()
