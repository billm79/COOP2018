# U10_Ex05_AddGrade.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 01 Mar 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 5
#     Source: Python Programming
#    Chapter: 10
#
# Program Description
#   Adds a addGrade() method to Student to facilitate adding grades
#   and credit hours for several courses, then calculates GPA on
#   the total hours and quality points.
#
# Algorithm (pseudocode)
#   introduce program
#   get students name
#   create student object with 0 hours and 0 quality points
#   loop to get hours and grade for each course
#   print GPA


class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours

    def addGrade(self, gradePoint, credits):
        """
        Records a grade for the student
        :param gradePoint: float -> represents a grade
                            (e.g., A = 4.0, A– = 3.7, B+ = 3.3, etc.)
        :param credits: float -> number of credit hours for the class
        :return: None
        """
        self.hours += credits
        self.qpoints += gradePoint * credits


def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)


def main():
    print("\nThis program creates a student and adds grades to the student's record.")
    name = input("What is the student's name? ")
    student = Student(name, 0, 0)
    gp = '0'
    cr = '0'
    while True:
        gp = input("\nWhat grade did the student receive in this course? ")
        if gp == '':
            break
        cr = input("How many credit hours is this course worth? ")
        student.addGrade(float(gp), float(cr))
    print("\n{}'s GPA is {}".format(name, student.gpa()))


if __name__ == '__main__':
    main()
