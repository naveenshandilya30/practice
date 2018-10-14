#Q.No.1

n1=int(input("enter total number of keys: "))
d1={}
for i in range(1,n1+1):
    v=input("enter value of key: ")
    d1[i]=v
l=[]
for j in d1:
    l.append(j)
print("keys of dictionary is: ",l)

#Q.No.2

d={"a":{"math":45,"science":56,"hindi":67,"english":89},"b":{"math":34,"english":67,"hindi":45,"science":76},"c":{"science":35,"maths":65,"english":23,"hindi":78}}
n=input("enter student name (a,b,c) to print marks: ")
for i in d:
    if n.lower()==i:
        print(d[n.lower()])
    
