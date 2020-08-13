import random;
n=1
z=input("Please enter your name sir:")
print(f"Hello {z}!\n")
while n<11:
    a=['s' , 'w' , 'g']
    b=random.choice(a);
    c=input(f"Here are the options:\n(s)Snake\n(w)Water\n(g)Gun\nPlease enter your option number {n}:");
    i=0;j=0
    if c==b:
        pass
    elif c=='s' and b=='w':
        i+=1;
    elif c=='w' and b=='g': 
        i+=1;
    elif c=='g' and b=='s':
        i+=1;
    elif b=='s' and c=='w':
        j+=1;
    elif b=='w' and c=='g':
        j+=1;
    elif b=='g' and c=='s':
        j+=1;
    n+=1
if i>j:
    print(f"Congrats {z}!!!!\nYOU WIN\nThe scores are {i}:{j} in favour of you")
elif i==j :
    print(f"It's a TIE\nThe scores are {i}:{j}")
else:
    print(f"You Lose\nBetter try next time")