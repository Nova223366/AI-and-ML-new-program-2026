import cv2
from tkinter import *
image = cv2.imread(r"C:\AI and ML new program 2026\Class Work files\Computer vision\website.jpg")

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow("Loaded Image", 800, 500)

cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"image Dimensions: {image.shape}")

root = Tk()
root.title("Panda Image")
root.geometry("800x500")
label1 = Label(root, text = "What you just see in image?")
label1.pack()
entry1 = Entry(root)
entry1.pack()

def Submit():
    if entry1.get().capitalize() == "Panda":
        label2 = Label(root, text = "Correct answer it was a panda!")
        label2.pack()
    else:
        label3 = Label(root, text = "Wrong answer it was a panda!")
        label3.pack()

button = Button(root, text = "Submit", command = Submit)
button.pack(pady=10)

root.mainloop()