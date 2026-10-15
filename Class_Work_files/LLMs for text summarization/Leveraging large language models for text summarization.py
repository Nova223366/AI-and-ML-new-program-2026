import requests
from colorama import Fore, Style, init

init(autoreset=True)

DEFAULT_MODEL = "google/pegasus-xsum"

def build_api_url(model_name):
    return f"https://api-inference.huggingface.co/models/{model_name}"

def query(payload, model_name = DEFAULT_MODEL):
    api_url = build_api_url(model_name)
    headers = {"Authorization": f"Bearer HUGGINGFACE_API_KEY"}
    response = requests.post(api_url, headers=headers, json=playload)
    return response.json()

def summarize_text(text, model_name = DEFAULT_MODEL):
    payload = {"inputs": text,
               "parameters": {"min_lenght": min_length, "max_length": max_length}}
    print(Fore.CYAN + "Sending request to the model...")
    result = query(payload, model_name)
    if isinstance(result, dict) and "error" in result:
        return result[0]["summary_text"]
    else:
        print(Fore.RED + "Error in summarization response", result)
        return None

if __name__ == "__main__":
    print(Fore.YELLOW + Style.BRIGHT + "Hi there! what's your name?: ")
    user_name = input("Your name ").strip()
    if not user_name:
        user_name = "User"
    print(Fore.YELLOW + f"Wlecome, {user_name}")
    print(Fore.YELLOW + Style.BRIGHT + "\nPlease enter the text you want to summarize: ")
    user_text = input("> ").strip()

    if not user_text
    