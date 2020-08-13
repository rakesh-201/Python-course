def getdate():
     import datetime
     return datetime.datetime.now()

def Register(z):
     print('About what is the data amoung the following:\n (1)Diet\n (2)Exercise ')
     y=int(input());
     if z==1:
          if y==1:  
               f = open("Rakesh_Diet.txt","a")
               print("You now may enter data: ")
               f.write(str([getdate]))
               f.write(input())
               f.write("\n")
               f.close()
          elif y==2:
               f = open("Rakesh_Exercise.txt","a")
               print("You now may enter data: ")
               f.write([getdate] + input() + "\n")
               f.close()
               
     elif z==2:
          if y==1:
               f = open("Rocky_Diet.txt","a")
               print("You now may enter data: ")
               f.write([getdate] + input() + "\n")
               f.close()
          elif y==2:
               f = open("Rocky_Exercise.txt","a")
               print("You now may enter data: ")
               f.write([getdate] + input() + "\n")
               f.close()
               
     elif z==3:
          if y==1:
               f = open("Rock_Diet.txt","a")
               print("You now may enter data: ")
               f.write([getdate] + input() + "\n")
               f.close()
          elif y==2:
               f = open("Rock_Exercise.txt","a")
               print("You now may enter data: ")
               f.write([getdate] + input() + "\n")
               f.close()
def Retrive(z) :         
     print('About what is the data amoung the following:\n (1)Diet\n (2)Exercise ')
     y=int(input());
     if z==1:
          if y==1:
               f = open("Rakesh_Diet.txt")
               print("You now may enter data: ")
               print(f.read())
               f.close()
          elif y==2:
               f = open("Rakesh_Exercise.txt")
               print("You now may enter data: ")
               print(f.read())
               f.close()
               
     elif z==2:
          if y==1:
               f = open("Rocky_Diet.txt")
               print("You now may enter data: ")
               print(f.read())
               f.close()
          elif y==2:
               f = open("Rocky_Exercise.txt")
               print("You now may enter data: ")
               print(f.read())
               f.close()
               
     elif z==3:
          if y==1:
               f = open("Rock_Diet.txt")
               print("You now may enter data: ")
               print(f.read())
               f.close()
          elif y==2:
               f = open("Rock_Exercise.txt")
               print("You now may enter data: ")
               print(f.read())
               f.close()
x=1
while x:
     print("What do you want to do amoung the following\n (1)Enter data \n (2)Retrive data ");
     a=int(input());

     if (a==1):
          print('Whose data you want to enter amoung the following:\n (1)Rakesh\n (2)Rocky\n (3)Rock')
          b=int(input());
          if b==1:
               Register(1) 
          elif b==2:
               Register(2) 
          else :     
               Register(3) 

     elif a==2:
          print('Whose data you want to retrive amoung the following:\n (1)Rakesh\n (2)Rocky\n (3)Rock')
          c=int(input());    
          if c==1:
               Retrive(1) 
          elif c==2:
               Retrive(2) 
          else :     
               Retrive(3) 
     print("Do you want to go to the menu:\n (1)yes\n (0)no ")
     x=int(input())
