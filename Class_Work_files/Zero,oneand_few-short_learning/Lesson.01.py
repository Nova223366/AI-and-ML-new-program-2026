from groq import generate_response

def run_activity():
    print("Zero, One, and Few-Shot Learning Activity")

    category = input("Enter the category (e.g., 'animals', 'fruits', 'vehicles'): ").strip()

    item = input(f"Enter a specific {category} to classify: ").strip()

    if not category or not item:
        print("Category and item cannot be empty. Please try again.")
        return

    zero_shot = f"Is {item} a {category}? Answer with 'yes' or 'no'."

    print("\nZero-Shot Learning:")
    print(f"Prompt: {generate_response(zero_shot, temperature=0.3, max_tokens=1024)}")

    one_shot = f"""Example:
catehgory: fruit
item: apple
Answer: Yes, apple is a fruit.

Now you try:
catehgory: {category}
item: {item}
Answer:"""

    print("\nOne-Shot Learning:")
    print(f"Prompt: {generate_response(one_shot, temperature=0.3, max_tokens=1024)}")

    few_shot = f"""Examples:
category: fruit
item: apple
Answer: Yes, apple is a fruit.

Now you try:
category: {category}
item: {item}
Answer:"""

    print("\nFew-Shot Learning:")
    print(f"Prompt: {generate_response(few_shot, temperature=0.3, max_tokens=1024)}")

    creative_prompt = f""" Write a one-sentence story about the given word.
    
Example 1: Word: moon
story: The moon shone brightly over the quiet village, casting silver shadows on the cobblestone streets.
Example 2: Word: river
story: The river flowed gently through the valley, reflecting the sunlight on its surface.

word: {item}
story:"""

    print("\nCreative Prompt:")
    print(f"Prompt: {generate_response(creative_prompt, temperature=0.7, max_tokens=1024)}")

if __name__ == "__main__":
    run_activity()