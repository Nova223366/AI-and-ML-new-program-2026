def get_domain_choice():
    print("\n--- Select Prompt Domain ---")
    print("1. Business & Marketing")
    print("2. Academic & Education")
    print("3. Technical & Programming")
    choice = input("Enter choice (1-3): ")
    return choice

def refine_business(prompt):
    role = "Act as an experienced Marketing Director."
    audience = "Audience: Working professionals and young adults."
    task = "Task: " + prompt
    constraints = "Constraints: Concise, professional tone, actionable Call to Action (CTA), under 150 words."
    return f"{role}\n{task}\n{audience}\n{constraints}"

def refine_academic(prompt):
    role = "Act as a High School Science and Tech Educator."
    audience = "Audience: Class 12 students learning new concepts."
    task = "Task: " + prompt
    constraints = "Constraints: Clear bullet points, 1 simple real-world analogy, max 200 words."
    return f"{role}\n{task}\n{audience}\n{constraints}"

def refine_technical(prompt):
    role = "Act as a Senior Python Developer."
    audience = "Audience: Junior programmers looking for clear solutions."
    task = "Task: " + prompt
    constraints = "Constraints: Provide step-by-step logic, clean code, and defensive error handling."
    return f"{role}\n{task}\n{audience}\n{constraints}"

def save_record(original, domain, refined):
    file = open("prompt_records.txt", "a")
    file.write("ORIGINAL VAGUE PROMPT:\n" + original + "\n\n")
    file.write("DOMAIN: " + domain + "\n\n")
    file.write("REFINED CONTEXTUAL PROMPT:\n" + refined + "\n")
    file.write("-" * 50 + "\n\n")
    file.close()

def view_records():
    try:
        file = open("prompt_records.txt", "r")
        content = file.read()
        file.close()
        if content.strip() == "":
            print("\nNo saved records found.")
        else:
            print("\n--- SAVED PROMPT RECORDS ---")
            print(content)
    except FileNotFoundError:
        print("\nNo records file found. Save a prompt first!")

def main():
    while True:
        print("\n==================================")
        print("  AI PROMPT REFINEMENT TOOL")
        print("==================================")
        print("1. Refine a Vague Prompt")
        print("2. View Saved Records")
        print("3. Exit")
        
        option = input("Enter your option (1-3): ")
        
        if option == '1':
            vague_prompt = input("\nEnter your vague prompt: ")
            domain_choice = get_domain_choice()
            
            if domain_choice == '1':
                domain_name = "Business & Marketing"
                refined = refine_business(vague_prompt)
            elif domain_choice == '2':
                domain_name = "Academic & Education"
                refined = refine_academic(vague_prompt)
            elif domain_choice == '3':
                domain_name = "Technical & Programming"
                refined = refine_technical(vague_prompt)
            else:
                print("Invalid domain choice!")
                continue
                
            print("\n" + "="*40)
            print("REFINED CONTEXTUAL PROMPT:")
            print("="*40)
            print(refined)
            print("="*40)
            
            save_opt = input("\nDo you want to save this record to file? (y/n): ")
            if save_opt.lower() == 'y':
                save_record(vague_prompt, domain_name, refined)
                print("Record saved successfully to 'prompt_records.txt'!")
                
        elif option == '2':
            view_records()
            
        elif option == '3':
            print("\nExiting program. Thank you!")
            break
            
        else:
            print("Invalid option! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
