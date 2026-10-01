from groq import generate_respones as a

def get_essay_details():
    print("\n=== AI Writing Assistant ===\n")
    topic = input("What is the topic of your essay? ").strip()
    essay_type = input("What type of essay are you writing? ").strip()
    lengths = ["300 words", "900 words", "1200 words", "2000 words"]
    print("Select essay word count: ")
    for i, l in enumerate(lengths, 1):
        print(f"{i}. {l}")
    try:
        idx = int(input("> ").strip())
        length = lengths[idx - 1] if 1 <= idx <= len(lengths) else "300 words"
    except ValueError:
        length = "300 words"
    target_audience = input("Who is the target audience for your essay? ").strip()
    return {"topics": topic, "essay_type": essay_type, "length": length, "target_audience": target_audience}

def generate_essay_content(details):
    try:
        temp = float(input("Enter temperature (0.0-1.0, default 0.7): ").strip())
    except ValueError:
        print("Invalid input. Using default temperature of 0.7.")
        temp = 0.7
    intro_p = f"Write an introduction for an essay on the topic '{details['topics']}' of type '{details['essay_type']}' with a length of '{details['length']}' for the target audience '{details['target_audience']}'."
    intro = a(intro_p, temperature=temp)
    print(intro)

    print("\nWould you like the body written as full draft or step by step?")
    print("1. Full draft\n2. Step by step")
    choice = input("> ").strip()
    if choice == "1" or choice == "Full draft":
        body_p = f"Write the body of the essay on the topic '{details['topics']}' of type '{details['essay_type']}' with a length of '{details['length']}' for the target audience '{details['target_audience']}'."
        body = a(body_p, temperature=temp)
        print(body)
    elif choice == "2" or choice == "Step by step":
        print("\nGenerating body step by step...")
        for i in range(1, 4):
            step_p = f"Write part {i} of the body of the essay on the topic '{details['topics']}' of type '{details['essay_type']}' with a length of '{details['length']}' for the target audience '{details['target_audience']}'."
            step = a(step_p, temperature=temp)
            print(f"\n--- Part {i} ---\n{step}")
    conclusion_p = f"Write a conclusion for the essay on the topic '{details['topics']}' of type '{details['essay_type']}' with a length of '{details['length']}' for the target audience '{details['target_audience']}'."
    
        