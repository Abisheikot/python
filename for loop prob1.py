sum=0
for i in range(1,6):
     sum=sum+i
print(sum)

a=int("10")
b=int("20")
print(a+b)

a=[]
print("enter 5 number: ")
for i in range(5):
    num=int(input("enter num:"+str(i+1)))
    a.append(num)
print(a)

sum=0
for i in a :
    sum=sum+i
    print(sum)
    
num=int(input("enter the number: "))
if(num%3==0 and num%5==0):
    print("the give number is divissible by 3&5")
else:
    print("the given number is not divissible by 3&5")
    

sum=0
for i in range(11):
    sum=sum+i
    ave=sum/10
print(sum)
print(ave)

score_percentage=int(input("enter the percentage: "))
if(score_percentage>70):
            input("enter the name: ")
            input("enter the department: ")
            input("enter the location: ")
            print("you are eligible")
else:
            print("you are not eligible")
            
score_percentage=int(input("enter the percentage: "))
if(score_percentage>70):
            input("enter the name: ")
            input("enter the department: ")
            input("enter the location: ")
            print("you are eligible")
else:
            print("you are not eligible")
            
n=int(input("enter the number to check : "))
if(n%2==0):
    if(1<= n <=5):
        print("not wired")
    if(6<= n <=20):
        print("wired")
    if(n>20):
        print("not wired")
else:
    print("wired")
    
a=int(input("A: "))
b=int(input("B: "))
operation=input("add/sub/mulp/div")
if(operation=="add"):
        print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mulp"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    ("invalid number")
    

    

    
num=int(input("enter the number:" ))
if(num%2==0):
    print("the given number is even")
else:
    print("the given number is odd")
 
