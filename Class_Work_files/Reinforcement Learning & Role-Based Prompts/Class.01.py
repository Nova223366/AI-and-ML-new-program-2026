from Groq import generate_response

def reinforcement_learning_activity():
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ===\n")
    prompt = input("Enter a prompt for the AI model (e.g., 'Describe the lion'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return
    
    initial_response = generate_response(prompt)
    print("\nInitial Response from AI Model:")

    try:
        rating = int(input("Rate the respones from 1 (bad) to 5 (good): ").strip())
        if rating < 1 or rating > 5:
            print("Invalid rating. Using 3.")
            rating = 3
    except ValueError:
        print("Invalid input. Using 3.")
        rating = 3

    feedback = input("Provide feedback for improvement: ").strip()
    improved_response = f"{initial_response} (Feedback: {feedback})"
    print(f"\nImproved Response from AI Model:\n{improved_response}")

    print("\nReflection:")
    print("1. How did the model's respones improve with feedback?")
    print("2. How does reinforcement learning help AI to improve its performance over time?")

def role_based_prompt_activity():
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")
    category = input("Enter a category (e.g., science, history, math): ").strip()
    item = input(f"Enter a specific {category} topic (e.g., 'photosynthesis' for science): ").strip()

    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return

    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed, technical manner."

    teacher_response = generate_response(teacher_prompt, temperature = 0.3, max_tokens = 1024)
    expert_response = generate_response(expert_prompt, temperature=0.3, max_tokens=1024)

    print(f"\n--- Teacher's Prespective ---\n{teacher_re}")