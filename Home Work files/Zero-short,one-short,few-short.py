def build_zero_shot(task, text):
    prompt = f"Task: {task}\nText: {text}\nResult:"
    analysis = "Zero-Shot Learning:\n- Provides 0 examples.\n- Relies entirely on pre-trained knowledge.\n- Best for simple, standard tasks.\n- Lowest token usage."
    return prompt, analysis

def build_one_shot(task, example_input, example_output, text):
    prompt = f"Task: {task}\n\nExample:\nInput: {example_input}\nOutput: {example_output}\n\nInput: {text}\nOutput:"
    analysis = "One-Shot Learning:\n- Provides 1 example.\n- Sets target formatting and tone expectations.\n- Helps reduce ambiguity.\n- Moderate token usage."
    return prompt, analysis

def build_few_shot(task, examples_list, text):
    prompt = f"Task: {task}\n\nExamples:\n"
    for i, ex in enumerate(examples_list, 1):
        prompt += f"Example {i}:\nInput: {ex[0]}\nOutput: {ex[1]}\n\n"
    prompt += f"Input: {text}\nOutput:"
    analysis = "Few-Shot Learning:\n- Provides multiple (2+) examples.\n- Teaches intricate patterns, edge cases, and strict output structures.\n- Delivers highest accuracy for complex tasks.\n- Higher token usage."
    return prompt, analysis

def save_log(shot_type, task, built_prompt, analysis):
    file = open("shot_learning_log.txt", "a")
    file.write("===================================\n")
    file.write("PROMPTING STYLE: " + shot_type + "\n")
    file.write("TASK: " + task + "\n\n")
    file.write("GENERATED PROMPT:\n" + built_prompt + "\n\n")
    file.write("AI LEARNING ANALYSIS:\n" + analysis + "\n")
    file.write("===================================\n\n")
    file.close()

def view_logs():
    try:
        file = open("shot_learning_log.txt", "r")
        content = file.read()
        file.close()
        if content.strip() == "":
            print("\nNo saved experiment logs found.")
        else:
            print("\n--- SAVED PROMPT EXPERIMENTS ---")
            print(content)
    except FileNotFoundError:
        print("\nNo log file found. Run an experiment first!")

def main():
    while True:
        print("\n==============================================")
        print("  AI LEARNING STYLES LAB (SHOT PROMPTING)")
        print("==============================================")
        print("1. Zero-Shot Prompting (No Examples)")
        print("2. One-Shot Prompting (1 Example)")
        print("3. Few-Shot Prompting (Multiple Examples)")
        print("4. View Experiment Logs")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            task = input("\nEnter task (e.g., Sentiment Analysis, Topic Categorization): ")
            text = input("Enter target text to process: ")
            built_prompt, analysis = build_zero_shot(task, text)
            shot_type = "Zero-Shot"
            
        elif choice == '2':
            task = input("\nEnter task (e.g., Sentiment Analysis, Topic Categorization): ")
            ex_in = input("Enter sample input example: ")
            ex_out = input("Enter sample output example: ")
            text = input("Enter target text to process: ")
            built_prompt, analysis = build_one_shot(task, ex_in, ex_out, text)
            shot_type = "One-Shot"
            
        elif choice == '3':
            task = input("\nEnter task (e.g., Sentiment Analysis, Topic Categorization): ")
            count = int(input("How many examples do you want to provide? "))
            examples = []
            for i in range(count):
                print(f"\n--- Example {i+1} ---")
                ex_in = input("Sample Input: ")
                ex_out = input("Sample Output: ")
                examples.append((ex_in, ex_out))
            text = input("\nEnter target text to process: ")
            built_prompt, analysis = build_few_shot(task, examples, text)
            shot_type = "Few-Shot"
            
        elif choice == '4':
            view_logs()
            continue
            
        elif choice == '5':
            print("\nExiting AI Learning Styles Lab. Good luck with your project!")
            break
            
        else:
            print("Invalid choice! Please select 1-5.")
            continue
            
        print("\n" + "="*45)
        print(f"GENERATED {shot_type.upper()} PROMPT:")
        print("="*45)
        print(built_prompt)
        print("="*45)
        print("BEHAVIOR & ACCURACY ANALYSIS:")
        print(analysis)
        print("="*45)
        
        save_opt = input("\nSave experiment log to file? (y/n): ")
        if save_opt.lower() == 'y':
            save_log(shot_type, task, built_prompt, analysis)
            print("Log saved successfully to 'shot_learning_log.txt'!")

if __name__ == "__main__":
    main()
