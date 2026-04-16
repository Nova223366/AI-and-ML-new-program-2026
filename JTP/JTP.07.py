while True:
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
    elif str(z) == "0" or str(z) < "0":
        print("Go from here")
    else:
        print("Invalid operator")
    print("\n")
