import time

def select_temperature():
    print("\n--- Select Temperature Setting ---")
    print("1. Low Temp (0.2) - Deterministic, Factual, Predictable")
    print("2. Medium Temp (0.5) - Balanced, Standard, Natural")
    print("3. High Temp (0.9) - Highly Creative, Diverse, Expressive")
    choice = input("Enter choice (1-3): ")
    if choice == '1':
        return 0.2, "Low (0.2) - Deterministic"
    elif choice == '2':
        return 0.5, "Medium (0.5) - Balanced"
    elif choice == '3':
        return 0.9, "High (0.9) - Creative"
    else:
        return 0.5, "Medium (0.5) - Balanced (Default)"

def get_instructions():
    print("\n--- Instruction-Based Prompt Builder ---")
    role = input("Enter Persona/Role (e.g., Educator, Sci-Fi Writer): ")
    tone = input("Enter Tone (e.g., Formal, Enthusiastic, Humorous): ")
    format_type = input("Enter Format (e.g., Bullet Points, Essay, Code): ")
    constraints = input("Enter Constraints (e.g., Under 100 words, No technical terms): ")
    return role, tone, format_type, constraints

def simulate_ai_response(prompt, temp_val, role, tone, format_type, constraints):
    built_prompt = f"Role: {role}\nTone: {tone}\nFormat: {format_type}\nConstraints: {constraints}\nUser Query: {prompt}\nTemperature: {temp_val}"
    
    if temp_val <= 0.3:
        behavior_analysis = "Low Temperature Effect: Output will be highly focused, precise, repeatable, and strictly adhere to defined rules with zero creative variation."
    elif temp_val <= 0.6:
        behavior_analysis = "Medium Temperature Effect: Output balances strict rule adherence with smooth, natural phrasing suitable for general communication."
    else:
        behavior_analysis = "High Temperature Effect: Output prioritizes creative phrasing, imaginative vocabulary, and unexpected stylistic choices while maintaining core context."
        
    return built_prompt, behavior_analysis

def save_experiment(prompt, built_prompt, analysis, temp_name):
    file = open("prompt_lab_log.txt", "a")
    file.write("===========================================\n")
    file.write("TIMESTAMP: " + time.ctime() + "\n")
    file.write("TEMPERATURE SETTING: " + temp_name + "\n")
    file.write("ORIGINAL PROMPT: " + prompt + "\n\n")
    file.write("STRUCTURED INSTRUCTION PROMPT:\n" + built_prompt + "\n\n")
    file.write("AI BEHAVIOR ANALYSIS:\n" + analysis + "\n")
    file.write("===========================================\n\n")
    file.close()

def view_logs():
    try:
        file = open("prompt_lab_log.txt", "r")
        content = file.read()
        file.close()
        if content.strip() == "":
            print("\nNo experiment logs found.")
        else:
            print("\n--- PROMPT LAB EXPERIMENT LOGS ---")
            print(content)
    except FileNotFoundError:
        print("\nNo log file found. Run an experiment first!")

def main():
    while True:
        print("\n==============================================")
        print("  PROMPT LAB: CREATIVITY & CONTROL TUNER")
        print("==============================================")
        print("1. Run New Prompt Lab Experiment")
        print("2. View Experiment History")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            user_prompt = input("\nEnter core prompt topic: ")
            temp_val, temp_name = select_temperature()
            role, tone, format_type, constraints = get_instructions()
            
            built_prompt, analysis = simulate_ai_response(user_prompt, temp_val, role, tone, format_type, constraints)
            
            print("\n" + "="*45)
            print("COMPOSED INSTRUCTION-BASED PROMPT:")
            print("="*45)
            print(built_prompt)
            print("="*45)
            print("PREDICTED AI BEHAVIOR & CONTROL ANALYSIS:")
            print(analysis)
            print("="*45)
            
            save_opt = input("\nSave experiment log to file? (y/n): ")
            if save_opt.lower() == 'y':
                save_experiment(user_prompt, built_prompt, analysis, temp_name)
                print("Experiment saved successfully to 'prompt_lab_log.txt'!")
                
        elif choice == '2':
            view_logs()
            
        elif choice == '3':
            print("\nExiting Prompt Lab. Good luck with your project!")
            break
            
        else:
            print("Invalid selection! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
