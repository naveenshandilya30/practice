#Q.No.1

a=3
if a<4:
    try:
        a=a/(a-3)
        print(a)
    except Exception as a:
        print("ZeroDivisionError")
        print(a)

#Q.No.2

l=[1,2,3]
try:
    print(l[3]) 
except Exception as b:
    print("IndexError")
    print(b)
    
#Q.No.3

#try:
#   raise NameError("Hi there")  # Raise Error
#except NameError:
#   print("An exception")
#   raise  # To determine whether the exception was raised or not
    
#output
print("NameError: Hi there")

#Q.No.4

def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
    
    # Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#output
print("-5.0 \n a/b result in 0")

#Q.No.5

#Import Error

try:
    import aba
except Exception as i:
    print(i)

#Value Error

try:
    a=1
    print(z)
except Exception as v:
    print(v)

#Index Error

l=[1,2,3]
try:
    print(l[3]) 
except Exception as b:
    print("IndexError")
    print(b)
    
    

