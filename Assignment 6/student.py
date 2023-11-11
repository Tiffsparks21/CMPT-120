# oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''
import random


class Student:
    def __init__(self, name, student_id, year, major, gpa):
        self.name = name
        self.studentID = student_id
        self.year = year
        self.major = major
        self.gpa = gpa

    def honorsProgram(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    def id(self):
        x = random.randint(1, 9999)  # Student ID? or a different varibale
        # return self.studentId = x
        if self.studentID == x:
            return("Winner! student " + str(self.name) + " gets free lunch!")
        else:
            return("Loser!")


def main():
    student1 = Student("Tom", 8972, "freshman", "Biochem", 3.4)
    student2 = Student("Alessandra", 1726, "senior", "Biochem", 3.7)
    student3 = Student("Sebastian", 8249, "sophomore", "Biochem", 3.07)
    # create three students and check if they get free lunch and if they qualify for honors
    print(str(student1.honorsProgram()) + " " + str(student1.id()))
    print(str(student2.honorsProgram()) + " " + str(student2.id()))
    print(str(student3.honorsProgram()) + " " + str(student3.id()))


main()
