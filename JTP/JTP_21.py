'''
def show_word():
    f = open("JTP/Notes.txt")
    x = f.read()
    x = x.upper()
    print(x)
    f.close()

show_word()
'''

def countline():
    f = open("JTP/Notes.txt")
    lines = f.readline()
    while lines:
        if lines [0] == "k" or lines [0] == "K":
            print(lines)
        lines = f.readline()
    f.close()

countline()
        