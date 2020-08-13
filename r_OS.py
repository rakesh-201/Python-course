import os
def soldier(a,b,c):
    f1 = open(b,"r")
    # print(f1.read(100))
    os.chdir(a)
    for i in os.listdir():
        if os.path.splitext(i)[1].lower() in ('.jpg' , '.jpeg'):
            continue
        else:
            if i == f1 :
                print("doing")
                continue
            else:
                os.replace( i , i.capitalize())
                print('done')
    
    print(os.listdir())
soldier("C:/Users/USER/Desktop/python/rakesh_prac","f1.txt",".jpg")
