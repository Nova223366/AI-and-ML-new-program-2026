import pickle

def append():
    rec = ()
    f = open("Resource.dat", "ab")

    R_ID = int(input("Enter your ID: "))
    R_Name = input("ENter your name: ")
    R_Expertise = input("Enter your expertise area: ")
    charges = int(input("Enter your charges: "))

    rec = (R_ID, R_Name, R_Expertise, charges)
    pickle.dump(rec, f)
    f.close()

append()