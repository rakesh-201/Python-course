a = []
print(f"Enter the number of items: " )
z = int(input())
for i in range(z):              #taking input
    a.append(int(input()))
print({i for i in a})           #printing the set
