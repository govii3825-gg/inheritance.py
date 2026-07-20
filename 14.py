# inheritence

# single level
# multi level
# multiole level

class Person1:
    def __init__(self):
        pass
    def read(self):
        print("a person can read")
    def write(self):
        print("a person can write")
class Person2(Person1):
    def __init__(self):
        pass
    def run(self):
        print("a person can run")
    def jump(self):
        print("a person can jump")
class Person3(Person2):
    def __init__(self):
        pass
    def sleep(self):
        print("a person can sleep")
    def stand(self):
        print("a person can stand ")
class Person4(Person3):
    def __init__(self):
        pass
    def bmw(self):
        print("bmw is a german car brand")
    def tata(self):
        print("tata is an indian car brand")  
  
    


p4=Person4()
p4.read()
p4.jump()
p4.stand()
p4.bmw()
        

# polymorphism

class Students:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        return self.m1+self.m2 ,other.m1+other.m2
    


s1=Students(10,8)
s2=Students(7,6)

print(s1+s2)