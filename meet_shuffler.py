import random
class Student():
    def __init__(self, name, nationality,gender):
        self.name = name
        self.nat = nationality
        self.gender = gender
    def __repr__(self):
        return self.name    
class Section():
    def __init__(self,name):
        self.name = name
        self.students = {}
        self.counter = 0
        self.pairs = []
        self.nat_check = False
        self.gender_check = False

    def add_student(self,student):
        self.students[self.counter] = student
        self.counter += 1
    
    