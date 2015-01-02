import random

#biggest of 2 numbers

def two_numbers(x, y):
    if x > y:
        print (x)
    else:
        print (y)

#biggest of 3 numbers
        
def three_numbers(x,y,z):
    if x > y:
        if x > z:
            print (x)
        else:
            print(z)   
    else:
         if y > z:
             print(y)
         else:
             print(z)

#positive numbers

def positive(x,y,z,a):
    b=[]
    if x > 0:
        b.append(x)
    if y > 0:
        b.append(y)
    if z > 0:
        b.append(z)
    if a> 0:
        b.append(a)
    print ('are positive number:',b)
    
        
        
    

#give the largest of three input number
                 
def threeinput():
    x = input("Enter a number: ")
    y = input("Enter a number: ")
    z = input("Enter a number: ")
    if x > y:
        if x > z:
            print (x)
        else:
            print(z)   
    else:
         if y > z:
             print(y)
         else:
             print(z)

             
# give the biggest of 3 random integer

def threeran():
    x = random.randint(0,100)
    y = random.randint(0,100)
    z = random.randint(0,100)
    if x > y:
        if x > z:
            print (x)
        else:
            print(z)   
    else:
         if y > z:
             print(y)
         else:
             print(z)
