class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def my_method(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if self.grades > 0 and self.grades <=10:
                return Lecturer.grades

    def __str__(self):
        return f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за домашнее задание: {self.grades}\n'
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {", ".join(self.finished_courses)}'

@classmethod
def __average_grade(cls, other):
    if isinstance(other):
        return other.grades

def __eq__(self, other):
    grade = self.__averege_grade(other(float, Lecturer))
    return self.grades

def __lt__(self, other):
    grade = self.__averege_grade(other,(float, Lecturer))
    return self.grades

def __lt__(self, other):
    grade = self.__averege_grade(other,(float, Lecturer))
    return self.grades




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)


class Lecturer(Mentor):
    grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за лекции: {self.courses_attached[grades]}'

@classmethod

def __average_grade(cls, other):
    if isinstance(other):
        return other.grades

def __eq__(self, other):
    grade = self.__averege_grade(other(float, Lecturer))
    return self.grades

def __lt__(self, other):
    grade = self.__averege_grade(other,(float, Lecturer))
    return self.grades

def __lt__(self, other):
    grade = self.__averege_grade(other,(float, Lecturer))
    return self.grades


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades [course] += [grade]
            else:
                student.grades = [grade]

        
    def __str__(self):
        return f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}'

student = Student("Alex", "Romanov", "male" )
student.finished_courses = ["Python", "Git"]
student.courses_in_progress = ["OOP"]
student.grades = {"Python": 10, "Git": 9.8}
student_2 = Student("Polina", "Abramova", "female")
student_2.finished_courses = ["Python", "Git"]
student_2.courses_in_progress = ["OOP"]
student_2.grades = {"Python": 9.9, "Git": 9.5}





