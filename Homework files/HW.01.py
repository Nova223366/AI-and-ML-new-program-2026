print("Hello! I am AI Bot. What's your name: ")

name = input()

print(f"Nice to meet you, {name}")

print("How are you feeling today? (good/bad): ")

mood = input().lower

if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("i'm sorry to hear that. Hope things get better soon.")
elif mood == "":
    print("You can share any thing with me")
else:
    print("I see. Sometimes it's hard to put feeling into words.")

print("want to contienue the conversation (yes or no)")
z = input("").lower()

if z == "yes":
    print("Bro your device get to die bye")
else:
    print(f"it was nice chatting with you {name}. Goodbye!")