import re
str = '''rakesh@gamil.com, rocky@gammil.com, rakesh.rr@gmail.com, rakesh.rr.rr@gmail.com'''
f1 = open("f1.txt", 'w')
f1.write("")
f1.close()
f1 = open("f1.txt", 'a')
l = re.findall('\S+@\S+',str)
z=0
for i in l:
    z+=1
    f1.write(f"Email{z}:{i}\n")    
f1.close()