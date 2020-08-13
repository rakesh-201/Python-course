a = ['hey i am using python','python python','python python python ','python python python python']
b = input(f'What do you want to search? ')
z=0
x={}
for i in a:
    c = i.split(' ')
    for j in c:
        if j==b:
            z+=1
        else:
            continue
    if z==0:
        continue
    else:
        x[z]=i
    z=0
z=[]
for k, v in x.items():
    z.append(k)
for i in z:
    k = max(x)
    print(x.get(k))
    del x[k]
