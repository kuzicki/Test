from turtle import pen


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Nick", 17)

print(p.name + " " + str(p.age))