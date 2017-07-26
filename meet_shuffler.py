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
        #is it uni-gender or uni-nationality
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

    #helper to update mixing checks
    def update_checks(self):
        #initializing
        keys = list(self.students.keys())
        gender = self.students[keys[0]].gender
        nat = self.students[keys[0]].nat
        for i in range(1,len(self.students)):
            #nat check
            if self.students[keys[i]].nat == nat:
                self.nat_check = True
            else:
                self.nat_check = False
            #gender check
            if self.students[keys[i]].gender == gender:
                self.gender_check = True
            else: 
                self.gender_check = False


    def shuffle(self):
        #base cases
        if len(self.students) == 0:
            return
         #also checks for uneven numbers
        elif len(self.students) == 1:
            self.pairs.append((self.students[0],None))

        #find 2 different students
        i0 = random.choice(list(self.students.keys()))
        i1 = random.choice(list(self.students.keys()))
        while i0 == i1:
            i0 = random.choice(list(self.students.keys()))
            i1 = random.choice(list(self.students.keys()))

        student0 = self.students[i0]
        student1 = self.students[i1]  

        #gender and nationality check
        self.update_checks()

        if (student0.nat != student1.nat and student0.gender != student1.gender) or (student0.nat != student1.nat and self.gender_check
        )or (student0.gender != student1.gender and self.nat_check) or (self.gender_check and self.nat_check):
            self.pairs.append((student0,student1))
            del self.students[i0]
            del self.students[i1]

        #recursive step
        self.shuffle()
