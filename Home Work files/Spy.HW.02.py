import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

conversation_history = []
stats = {"Positive": 0, "Neutral": 0, "Negative": 0}

def get_sentiment_details(text):
    polarity = TextBlob(text).sentiment.polarity
    
    if polarity > 0.25:
        return polarity, "Positive", Fore.GREEN, "HAPPY"
    elif polarity < -0.25:
        return polarity, "Negative", Fore.RED, "SAD"
    else:
        return polarity, "Neutral", Fore.YELLOW, "NEUTRAL"

def show_stats():
    print(f"\n{Fore.CYAN}--- Session Statistics ---")
    for sentiment, count in stats.items():
        print(f"{sentiment}: {count}")
    print(f"--------------------------{Style.RESET_ALL}")

print(f"{Fore.CYAN}Welcome to Sentiment Spy!{Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip() or "Mystery Agent"

print(f"\nHello, Agent {user_name}. Type 'Start' to see counts, or 'exit' to quit.")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        continue

    if user_input.lower() == "exit":
        show_stats()
        print(f"{Fore.BLUE}Farewell, Agent {user_name}!{Style.RESET_ALL}")
        break
    
    elif user_input.lower() == "stats":
        show_stats()
        continue

    elif user_input.lower() == "reset":
        conversation_history.clear()
        for key in stats: 
            stats[key] = 0
        print(f"{Fore.CYAN}History and stats cleared.{Style.RESET_ALL}")
        continue

    polarity, s_type, color, emoji = get_sentiment_details(user_input)
    
    conversation_history.append((user_input, polarity, s_type))
    stats[s_type] += 1
    
    print(f"{color}{emoji} {s_type} detected! (Polarity: {polarity:.2f}){Style.RESET_ALL}")
