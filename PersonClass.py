class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Greeting(self):
        print("Hello, my name is " + self.name)
    
    def Bday(self):
        self.age += 1


p = Person("Nick", 17)

p.Greeting()
<<<<<<< HEAD
p.sayFriends()







#There are messages
#That's it
=======
p.Bday()
print("My age now is: " + str(p.age))
#Super important message
>>>>>>> 8c45553 (Message)
