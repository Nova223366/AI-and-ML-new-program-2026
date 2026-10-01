from groq_02 import generate_response as k

def casual_talk():
    print("\n=== Casual Talk with AI ===\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            for i in range(3, 0, -1):
                print(f"Exiting in {i}...")
            print("Exited from casual talk.")
            break
        response = k(user_input, temperature=0.5, max_tokens=150)

casual_talk()