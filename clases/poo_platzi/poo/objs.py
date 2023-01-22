class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self, another_person):
        return f"Hi {str(another_person)}, I'm {str(self.name)}"
