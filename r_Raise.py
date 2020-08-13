try:print(a)
except Exception as e:
    a= input()
    if a=="Hello":
        raise RuntimeError("hii")
        # print("incorrect input")