#inheritence on multilevel and multiple:-
class Box:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class Student:
    def __init__(self,fees):
       self.fees=fees
class Box2(Box,Student):
    def __init__(self,name,rollno,fees,marks):
        self.marks=marks
        Student.__init__(self,fees)
        Box.__init__(self,name,rollno)
class Box3(Box2):
    def __init__(self,sem):
        self.sem=sem
        Box2.__init__(self,"shiv-raj",12,23,200000)


obj=Box3("2-1")
print(obj.sem)
print(obj.name)

obj2=Box2("shiv",12,23,200000)
print(obj2.fees)
print(obj2.marks)
print(obj2.name)
print(obj2.rollno)

obj3=Box2("raj",45,67,78900)
print(obj3.name)
print(obj3.rollno)
print(obj3.marks)
print(obj3.fees)
