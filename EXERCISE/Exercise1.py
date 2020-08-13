a=int(input("Enter your age or Year of Birth: "))
if a<0 or a>2020:
    print(f'You seem to be not present in this world at present')
else:
    if a>1800:
        z=2020-a
        print(f'You are {z} years old ')
        z=input('Do you want to know your age in a particular year? (Y/N): ')
        if z=='Y':
            b=int(input('Enter the year:'))
            if b<a:
                print(f'You seem to be not born in {b}')
            else:
                b=b-a
                print(f'You will be {b} years old ')
    elif a<150:
        z=input('Do you want to know your age in a particular year? (Y/N): ')
        if z=='Y':
            b=int(input('Enter the year:'))
            if b<a:
                print(f'You seem to be not born in {b}')
            else:
                b=b-2020+a
                print(f'You will be {b} years old ')
    elif a>149:
        print(f'You seemed to be the oldest person alive')