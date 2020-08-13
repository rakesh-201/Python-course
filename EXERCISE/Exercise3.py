a=int(input(f'Enter the number of Test Cases:'))
while(a>0):
    z=int(input())
    while(1):
        b=str(z)
        b=b[::-1]
        if z==int(b):
            print(z)
            break
        else:
            z+=1
    a-=1