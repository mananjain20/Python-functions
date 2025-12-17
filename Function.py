def cal_sum(a,b):
    sum = a+b
    print (sum)
    return sum

cal_sum(123,2)


def avg_of_num(a,b,c):
    avg = (a+b+c)/3
    print (avg)
    return (avg)

num1= int(input ("enter of 1st numneer:"))
num2= int(input ("enter of 2nd numneer:"))
num3= int(input ("enter of 3rd numneer:"))
avg_of_num(num1,num2,num3)

def fact(n):
    fact=1
    for i in range (1,n+1):
     fact *=i
    print(fact)  

fact(5)
def converter(usd):
    inr=usd*83
    print(usd ,"USD","=", inr,"INR")
    return inr

converter(100)

def identification(n):
    if(n%2==0):
        print(n,"is a even number ")

    elif (n%2!=0):
        print(n,"is a odd number ")

    else:
        print ("special character ") 

def sqroot (n):
    if n<0:
        print("please select a valid number")
    else:
        print("square root of", n, "is", n**0.5)
        return n**0.5
    



