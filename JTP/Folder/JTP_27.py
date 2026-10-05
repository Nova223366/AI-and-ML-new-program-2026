from groq_02 import generate_response, list_models

def main():

    print("===================================")
    print("       GROQ AI DEBUG PROGRAM")
    print("===================================")

    # Show available models
    print("\nChecking Groq models...")
    list_models()

    print("Type 'exit' to quit.")
    print()

    while True:

        try:

            prompt = input("You: ")

            if prompt.lower().strip() == "exit":
                print("Goodbye!")
                break

            if not prompt.strip():
                print("Please enter a message.")
                continue

            print("\n[DEBUG] Sending request...\n")

            response = generate_response(prompt)

            print("\nAI:", response)
            print()

        except KeyboardInterrupt:

            print("\nProgram stopped.")
            break

        except Exception as e:

            print("\n========== UNEXPECTED ERROR ==========")
            print(
                f"Type: {type(e).__name__}"
            )
            print(
                f"Message: {e}"
            )
            print("======================================\n")

if __name__ == "__main__":
    main()
