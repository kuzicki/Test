class Person:
    friends = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Greeting(self):
        print("Hello, my name is " + self.name)
        hello
    
    def Bday(self):
        self.age += 1

    def addFriends(self, friend_name):
        self.friends.append(friend_name)

    def sayFriends(self):
        print(self.friends)



p = Person("Nick", 17)
p.addFriends("Kate Young")
p.addFriends("Justin")
p.Greeting()
p.sayFriends()
