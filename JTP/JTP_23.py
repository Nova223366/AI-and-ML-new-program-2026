import pickle

def new_data():
    rec = {}
    f = ("Product.dat", "ab")

    Prod_code = int(input("Enter your product code: "))
    Prod_dese = input("Enter your product description: ")
    Prod_stock = int(input("Enter your product stock: "))

    rec = {"Prod_code": Prod_code, "Prod_dese": Prod_dese, "Prod_stock": Prod_stock}
    print("\n",rec,"\n")
    print("Data has been added successfully")
    pickle.dump(rec, f)
    f.close()

new_data()
