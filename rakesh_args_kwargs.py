def func(*he,**hey):
    for item in he:                                     # for item,value in hey.items():
        print(item)                                     #     print(item,value)
    for key, value  in hey.items():
        print(key,':',value);        

n=[1,2,3,4]
a={"rakesh":"Good Boy","rocky":"Good Boy"}
func(*n,**a)
