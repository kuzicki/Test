class Person:
    friends = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Greeting(self):
        print("Hello, my name is " + self.name)
    
    def Bday(self):
        self.age += 1

    def addFriends(self, friend_name):
        self.friends.append(friend_name)

    def sayFriends(self):
        print(self.friends)
    def sayAge(self):
        print(self.age)



p = Person("Nick", 17)
p.addFriends("Kate Young")
p.addFriends("Justin")
p.Greeting()
p.sayFriends()
p.sayAge()
p.Bday()
p.sayAge()





#There are messages
#That's it