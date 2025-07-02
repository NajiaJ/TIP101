class Student:
    def __init__(self, name, grade, major): # Whenever I create a Student, a name must be provided
        self.name = name
        self.grade = grade
        self.major = major

nina_the_student = Student("Nina")
print(nina_the_student.name)