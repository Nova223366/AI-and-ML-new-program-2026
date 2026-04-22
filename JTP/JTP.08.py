while True:
    user = input("Want number table? (y/n): ").lower()
    if user == "y":
        numx = int(input("Enter the number: "))
        for i in range(1, 11):
            print(f"{numx} X {i} = {numx * i}")
            break
        else:
            numa = int(input("Enter first number: "))
            numb = int(input("Enter second number: "))
            z = input("What you want to do? (+,-,*,/,//): ")

            if z == "+":
                print(f"{numa} + {numb} = {numa + numb}")
            elif z == "-":
                print(f"{numa} - {numb} = {numa - numb}")
            elif z == "*":
                print(f"{numa} * {numb} = {numa * numb}")
            elif z == "/":
                print(f"{numa} / {numb} = {numa / numb}")
            elif z == "//":
                print(f"{numa} // {numb} = {numa // numb}")
    
            elif (z) == " " or (z) < " ":
                print("Go from here")
            elif z.isalnum():
                print("Are you serious?")
            else:
                print("Invalid operator")
    print("\n")
