import random;

def incorrect(n):
    l=[]
    for i in range(1,11):
        l.append(n*i)
    r = random.randint(1, 10)
    l[r]=15
    return l;

def iscorrect(n, l):
    z=0
    cl=[]
    for i in range(1, 11):
        cl.append(n*i)
    for i in range(1, 11):
        if l[i]==cl[i]:
            continue
        else:
            z = n*i
            print(f'The value of {n}*{i} is {z} and not {l[i]}')
            return cl
    return cl;
        
n = int(input(f'Enter the number: '))
l = incorrect(n)
cl = iscorrect(n, l)