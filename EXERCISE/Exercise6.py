import random
n = int(input(f'Enter number of friends: '))
l = []
a = {}
for i in range(1, (n+1)):
    l.append(input(f'Enter the name of friend number {i}: '))
for i in l:
    z=i.split(' ')
    a[z[0]]=z[1]
x=[]
for k, v in a.items():
    x.append(v)
for k, v in a.items():
    r = random.randint(0,n-1)
    b = x[r]
    print(f'{k} {b}')

# print(a)