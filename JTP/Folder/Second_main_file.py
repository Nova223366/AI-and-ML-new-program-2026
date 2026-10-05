from groq_02 import generate_response as k 

def main():
    print("If you want to do task type 'task'")
    while True:
        user_input = input("You: ")

        if user_input == "task":
            School_tasks()
        elif user_input.lower().strip() == "command":
            utility()
        else:
            response = k(user_input)
            print(f"\nAI: {response}\n")


def School_tasks():
    import time
    animation = [".", "..", "...","...."]
    for i in range(len(animation)):
        print(f"\rLoading{animation[i]}", end="")
        time.sleep(1.0)
    print("\n========School task mode activated==========\n")
    while True:
        sec_input =input("Enter your school task: ")
        if sec_input.lower().strip() == "exit":
            main()
            print("Back to casual talk")
            break
        prompt = school_prompt_for_AI_model(sec_input)
        response = k(prompt)
        print(f"\nAI: {response}\n")       

def school_prompt_for_AI_model(school_task):
    role = "Act as a High School Educator to explain the following school task in simple terms."
    constraints = "Constraints: Clear bullet points, 1 simple real-world analogy"
    task = f"Task: {school_task}"
    prompt = f"{role}\n{constraints}\n{task}"
    return prompt


def utility():
    import webbrowser
    command = input("Enter a utility command (e.g., 'open chrome', 'open chatgpt', 'open youtube', 'open google', 'open gmail'): ")
    print(command)
    command = command.lower().strip()

    if command == "open chrome":
        webbrowser.open("https://www.google.com")

    elif command == "open chatgpt":
        webbrowser.open("https://chatgpt.com")

    elif command == "open youtube":
        webbrowser.open("https://youtube.com")

    elif command == "open google":
        webbrowser.open("https://google.com")

    elif command == "open gmail":
        webbrowser.open("https://mail.google.com")

    else:
        print("I don't know that utility command.")


main()