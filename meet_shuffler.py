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

    def __repr__(self):
        to_return = "\n"
        for stud0,stud1 in self.pairs:
            to_return += "["+repr(stud0)+" and "+repr(stud1)+"]\n"
        return to_return
    
    