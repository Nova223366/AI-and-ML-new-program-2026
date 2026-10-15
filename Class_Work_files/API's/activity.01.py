import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to retrieve a joke."
    
def main():
    print("Welcome to the Random Joke Generator!")

    while True:
        user_input = input("Press enter to get a new joke, or type 'q'/quit to exit: ").strip().lower()
        if user_input == 'q' or user_input == 'quit':
            print("Thanks for using the Random Joke Generator!")
            break
        else:
            joke = get_random_joke()
            print(joke)

if __name__ == "__main__":
    main()