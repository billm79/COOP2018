# U10_Ex06_AddLetterGrade.py
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
#   Adds a addLetterGrade() method to Student to facilitate adding letter grades
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
        Records a grade for the student, using numeric grades
        :param gradePoint: float -> represents a grade
                            (e.g., A = 4.0, A– = 3.7, B+ = 3.3, etc.)
        :param credits: float -> number of credit hours for the class
        :return: None
        """
        self.hours += credits
        self.qpoints += gradePoint * credits

    def addLetterGrade(self, letterGrade, credits):
        """
        Records a grade for the student, using letter grades
        :param letterGrade: str -> letter grade
                            (e.g., A = 4.0, A– = 3.7, B+ = 3.3, etc.)
        :param credits: float -> number of credit hours for the class
        :return: None
        """
        letterGrades = {"A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "D-": 0.7}
        gradePoint = letterGrades.get(letterGrade, 0)
        if gradePoint:
            self.hours += credits
            self.qpoints += gradePoint * credits


def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)


def main():
    print("\nThis program creates a student and adds grades to the student's record.")
    print(("Use these letter grades: A, A-, B+, B, B-, C+, C, C-, D+, D, D-, & F"))
    name = input("\nWhat is the student's name? ")
    student = Student(name, 0, 0)
    gp = '0'
    cr = '0'
    while True:
        lg = input("\nWhat letter grade did the student receive in this course? ")
        if lg == '':
            break
        cr = input("How many credit hours is this course worth? ")
        student.addLetterGrade(lg, float(cr))
    print("\n{}'s GPA is {}".format(name, student.gpa()))


if __name__ == '__main__':
    main()
