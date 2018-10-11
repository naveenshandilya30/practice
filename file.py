#Q.No.1

"""f=open(r"c:\python\text.txt","r")
f1=f.readlines()
for i in f1:
    print(i)
f.close()

#Q.No.2

f=open(r"c:\python\text1.txt","r")
f1=f.read()
s=input("enter a word to count its occurence: ")
c=0
for i in f1:
    if i==s:
        c+=1
f.close()
print(s,"occurs",c,"times.")

#Q.No.3

f=open(r"c:\python\text1.txt","r")
f1=f.read()
f.close()
f2=open(r"c:\python\text.txt","w")
f2.write(f1)
f2.close()

#Q.No.4

f=open(r"c:\python\text1.txt","r")
f1=open(r"c:\python\text2.txt","r+")
for i,j in zip(f,f1):
    f1.write(i+j)
f.close()
f1.close()"""

#Q.No.5
import random
f=open(r"c:\python\text3.txt","w+")
for i in range(10):
    num=random.randint(1,10)
    f.write(str(num))
f.close()
f=open(r"c:\python\text3.txt","r")
f1=f.read()
l=[]
for i in f1:
    i=int(i)
    l.append(i)
l.sort()
f2=open(r"c:\python\text4.txt","w")
for j in l:
    f2.write(str(j))
f2.close()
f.close()

        



