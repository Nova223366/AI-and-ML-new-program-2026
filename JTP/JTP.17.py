first_name = input("Enter your first name: ")
Surname = input("Enter your surname: ")
n = (f"{first_name} {Surname}").title()
print(n)


L = [4,6,9,20]
for i in L:
    for j in range(1,i%5):
        print(j, "#", end = "#")
    print()

