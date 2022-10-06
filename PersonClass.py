class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Greeting(self):
        print("Hello, my name is " + self.name)
        hello
    
    def Bday(self):
        self.age += 1


p = Person("Nick", 17)

p.Greeting()
p.Bday()
print("My age now is: " + str(p.age))