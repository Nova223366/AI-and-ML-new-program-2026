import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to retrieve a joke."
    
def get_random_travel():
    url = "https://opentdb.com/api.php?amount=1&category=22&type=multiple"
    response = requests.get(url)
    if response.status_code == 200:
        travel_data = response.json()
        question = travel_data['results'][0]['question']
        correct_answer = travel_data['results'][0]['correct_answer']
        return f"Travel Question: {question} - Correct Answer: {correct_answer}"
    else:
        return "Failed to retrieve a travel question."
    
def get_random_cat_facts():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    if response.status_code == 200:
        cat_fact_data = response.json()
        return f"Cat Fact: {cat_fact_data['fact']}"
    else:
        return "Failed to retrieve a cat fact."
    
def get_random_weather():
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        'key': 'YOUR_API_KEY',  # Replace with your actual API key
        'q': 'London'  # You can change this to any location you want
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        location = weather_data['location']['name']
        temp_c = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']
        return f"Weather in {location}: {temp_c}°C, {condition}"
    else:
        return "Failed to retrieve weather information."
    
def main():
    print("Welcome to the Random API Data Generator!")

    while True:
        print("1.'Get random joke'\n2.'Get random travel question'\n3.'Get random cat fact'\n4.'Get random weather info'")
        user_input = input("Press 1, 2, 3, or 4, or type 'q'/quit to exit: ").strip().lower()
        if user_input == 'q' or user_input == 'quit':
            print("Thanks for using the Random API Data Generator!")
            break
        elif user_input == '1':
            joke = get_random_joke()
            print(joke)
        elif user_input == '2':
            travel_question = get_random_travel()
            print(travel_question)
        elif user_input == '3':
            cat_fact = get_random_cat_facts()
            print(cat_fact)
        elif user_input == '4':
            weather_info = get_random_weather()
            print(weather_info)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()