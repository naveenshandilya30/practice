#Q.No.1

class Circle:
    def __init__(self,radius):
        self.radius=r
    def getArea(self,r):
        area=3.14*(r**2)
        return area
    def getCircumference(self,r):
        circum=2*3.14*r
        return circum

r=int(input("enter radius: "))
c=Circle(r)
print("area of circle is: ",c.getArea(r))
print("circumfrenece of circle i:",c.getCircumference(r))

#Q.No2

class Student:
    def __init__(self,name,r_no,age,marks):
        self.name=name
        self.r_no=r_no
        self.age=age
        self.marks=marks
    def Display(self,name,r_no):
        print("Student's name is: ",self.name)
        print("Student's r.no is: ",self.r_no)
    def setAge(self,age):
        print("Student's age is: ",self.age)
    def setMarks(self,marks):
        print("Student's maarks is:",self.marks)
n=input("enter name: ")
r=int(input("enter r.no: "))
a=int(input("enter age: "))
m=int(input("enter marks: "))
s=Student(n,r,a,m)
s.Display(n,r)
s.setAge(a)
s.setMarks(m)

#Q.no.3

class Temprature:
    def __init__(self,temp):
        self.temp=temp
    def convertFahrenheit(self,temp):
        fah=(temp*(9/5))+32
        return round(fah,2)
    def convertCelsius(self,temp):
        cel=(temp-32)*(5/9)
        return round(cel,2)

t=int(input("for Fahrenheit press 1, for celsius press 2: "))
if t==1:
    n1=int(input("enter temprature in celsius: "))
    t1=Temprature(n1)
    print("Temprature in Fahrenheit is ",t1.convertFahrenheit(n1))
elif t==2:
    n2=int(input("enter temprature in fahrenheit: "))
    t2=Temprature(n2)
    print("Temprature in celsius is ",t2.convertCelsius(n2))

#Q.No.4

class MovieDetails:
    def __init__(self,a_name,y_release,rating):
        self.a_name=a_name
        self.y_release=y_release
        self.rating=rating
        
    def display(self,a_name,y_release,rating):
        print("Artist name is ",a_name)
        print("Year of release is ",y_release)
        print("ratings of movie is",rating)
    def add(self):
        n=input("enter movie name: ")
        year=int(input("enter year of release: "))
        r=input("enter ratings: ")
        self.display(n,year,r)

m=MovieDetails("laila Majnu",2018,4)
m.display("laila Majnu",1988,4)
m.add()

#Q.No.5

class Animal:
    def __init__(self):
        pass
    def animal_attribute(self):
        print("animal class")

class Tiger(Animal):
    def __init__(self):
        pass

a=Animal()
t=Tiger()
t.animal_attribute()

#Q.No.6

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())

#output is

'A','B'
'A','B'

#Q.No.7

class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self,l,b):
        ar=l*b
        return ar
class Rectangle(Shape):
    def __init__(self):
        pass
class Square(Shape):
    def __init__(self):
        pass

    
n=int(input("for area:-\nof rectangle press 1, for square press 2:\n"))
if n==1:
    n1=int(input("enter length: "))
    n2=int(input("enter bredth: "))
    s=Shape(n1,n2)
    r=Rectangle()
    print("area of rectangle is:",r.area(n1,n2))
elif n==2:
    n1=int(input("enter lenth: "))
    s=Shape(n1,n1)
    s1=Square()
    print("area of square is ",s1.area(n1,n1))


    
    

        






