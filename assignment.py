#Q.No.1

length=int(input("enter length: "))
breadth=int(input("enter breadth: "))
height=int(input("enter height: "))

def area(l,b,h):
    return l*b

print("area of rectangle is: ",area(length,breadth,height))

def s_area(l1,b1,h1):
    return 2*((area(l1,b1,h1))+(area(b1,h1,l1))+(area(h1,l1,b1)))
print("area of rectangular surface is: ",s_area(length,breadth,height))


#Q.No.2

def mid(a,b,c):
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    m=max(l)
    n=min(l)
    if m==a and n==b or m==b and n==a:
        return c
    elif m==a and n==c or  m==c and n==a:
        return b
    elif m==b and n==c or  m==c and n==b:
        return a

n1=int(input("enter number: "))
n2=int(input("enter second number: "))
n3=int(input("enter third number: "))
print("middle number is: ",mid(n1,n2,n3))


#Q.No.3

def lst(l):
    l1=[]
    t1=[]
    for i in l:
        for j in l:
            if i+j>10:
                t1.append(i)
                t1.append(j)
                l1.append(t1)
                t1=[]
    return l1
l=[2,3,4,5,7,8,4,2,1]
print("combination of numbers whose sum is more than 10: ",lst(l))


    
