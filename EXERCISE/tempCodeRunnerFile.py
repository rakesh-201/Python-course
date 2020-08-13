import random
n = int(input(f'Enter number of friends: '))
l = []
for i in range(1, (n+1)):
    l.append(input(f'Enter the name of friend number {i}:'))
print(l)