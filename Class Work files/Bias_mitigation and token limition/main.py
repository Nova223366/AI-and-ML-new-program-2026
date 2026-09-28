from groq import generate_response

def bias_mitigation_activity():
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")
    prompt = input("Enter a prompt to explore nias (eg, 'Describe the ideal doctor'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return
    initial_response = generate_response(prompt, temperature=0.3, max_token=1024)
    print(f"\nInitial AI respones: {initial_response}")

    modified_prompt = input("Modify the prompt to make it more neutral (eg, 'Describe the qualities of a doctor'): ").strip()

    if modified_prompt:
        modified_prompt = generate_response(modified_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nModified AI response (Neutral): {modified_prompt}")
    else:
        print("No modified promt entered. Skipping neutral response.")

def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")
    long_prompt = input("Enter a long prompt (more than 300 words, eg, a detailed story or description): ").strip()

    if long_prompt:
        long_respones = generate_response(long_prompt, temperature=0.3, max_token=1024)
        preview = ()