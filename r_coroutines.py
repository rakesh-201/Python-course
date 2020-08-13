import time    
def nameFinder():
    f1 = open("f1.txt")
    f2 = open("f2.txt")
    f3 = open("f3.txt")
    f4 = open("f4.txt")
    f5 = open("f5.txt")
    time.sleep(2)
    while True:
        text = (yield)
        # if ((text in f1) or (text in f2) or (text in f3) or (text in f4) or (text in f5)):
        if "Rakesh" in f4:
            print(f"{text} is present")
        else:
            print(f"{text} is not present")

search = nameFinder()
next(search)
z = input(f"Please enter your name:")
search.send(z)
z = input(f"Please enter your name:")
search.send(z)
