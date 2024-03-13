from datetime import datetime

class Parent:

    all = []

    def __init__(self, name, children=None):
        self.name = name
        self._children = []
        if children:
            for child in children:
                self.add_child(child)
        Parent.all.append(self)

    def children(self):
        return self._children
    
    def add_child(self, child):
        if isinstance(child, Child):
            self._children.append(child)
        else:
            raise ValueError("Child must be an instance of the Child class.")

class Child:

    def __init__(self, name):
        self.name = name

    def parents(self):
        return [parent for parent in Parent.all if self in parent.children()]
    
    def add_parent(self, parent):
        if isinstance(parent, Parent):
            parent.add_child(self)
        else:
            raise ValueError("Parent must be an instance of the Parent class")
        

parent1 = Parent('Mom')
parent2 = Parent('Dad')
child1 = Child('Son')
child2 = Child('Daughter')

parent1.add_child(child1)
parent2.add_child(child1)
child2.add_parent(parent1)
child2.add_parent(parent2)

[print(c.name) for c in parent1.children()]
[print(p.name) for p in child1.parents()]

class Student:

    all = []

    def __init__(self, name):
        self.name = name
        Student.all.append(self)

    def enroll_in_course(self, course):
        Enrollment(self, course)

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.student == self]

    def courses(self):
        return [enrollment.course for enrollment in self.enrollments()]


class Course:

    all = []

    def __init__(self, title):
        self.title = title
        Course.all.append(self)

    def enroll_student(self, student):
        Enrollment(student, self)

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.course == self]

    def students(self):
        return [enrollment.students for enrollment in self.enrollments()]

class Enrollment:

    all = []

    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.enrollment_date = datetime.now()
        Enrollment.all.append(self)

student1 = Student('Mumo')
course1 = Course('SDF-FT08')

student1.enroll_in_course(course1)

print("THE FOLLOWING USE INTERMEDIARY CLASS")
print(student1.enrollments()[0].enrollment_date)
print(course1.enrollments()[0].enrollment_date)
print(student1.enrollments()[0].course.title)