class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.enroll_course(self)

    def get_students(self):
        return self.students

    def __str__(self):
        return f"Курс: {self.name} ({self.code})"


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def get_courses(self):
        return self.courses


# Створення студентів та курсів
student1 = Student("Олександр", "1")
student2 = Student("Марія", "2")
student3 =Student("Володимир","3")

course1 = Course("Математика", "MATH")
course2 = Course("Інформатика", "IT")
course3 = Course("Іноземна мова", "ENG")
# Запис студентів на курси

course1.add_student(student1)
course1.add_student(student2)
course2.add_student(student1)
course2.add_student(student3)
course3.add_student(student3)
course3.add_student(student2)
# Перевірка курсів та студентів
print(f"{student1.name} зареєстрований на курси:")
for course in student1.get_courses():
    print(course)

print(f"\nСтуденти, які проходять на 1 курс {course1}:")
for student in course1.get_students():
    print(student.name)

print(f"\nСтуденти, які проходять на 2 курс {course2}:")
for student in course2.get_students():
    print(student.name)

print(f"\nСтуденти, які проходять на 3 курс {course3}:")
for student in course3.get_students():
    print(student.name)
