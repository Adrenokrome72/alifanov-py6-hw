class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = 0

    # метод выставления оценки лекторам
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum = 0
        len = 0
        for key in lecturer.grades.keys():
            for mark in list(lecturer.grades[key]):
                sum = sum + mark
                len += 1
        lecturer.average_grades = round(sum / len, 1)

        # метод выбора студента, относящегося к курсу

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} - не является студентом')
            return
        return self.average_grades < other.average_grades

    # перегрузка класса student
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗаверешенные курсы: {self.finished_courses}'
        return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = 0
        self.students_list = []

    # метод проверки является ли лектором
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} - не является лектором')
            return
        return self.average_grades < other.average_grades

        # перегрузка класса lecturer

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades}'
        return result


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # метод выставления оценки студентам от ревьюеров
    def rate_student_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum = 0
        len = 0
        for key in student.grades.keys():
            for mark in list(student.grades[key]):
                sum = sum + mark
                len += 1
        student.average_grades = round(sum / len, 1)
        # перегрузка класса reviewer

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


student_1 = Student("Иван", "Петров", "М")
student_1.finished_courses += ["Введение в программирование"]
student_1.courses_in_progress += ["Python"]
student_1.courses_in_progress += ["Git"]

student_2 = Student("Сергей", "Васильев", "М")
student_2.courses_in_progress += ["Python"]
student_2.finished_courses += ["C++"]

lecturer_1 = Lecturer("Андрей", "Марков")
lecturer_1.courses_attached += ["Python"]
lecturer_1.courses_attached += ["Git"]

lecturer_2 = Lecturer("Геннадий", "Смирнов")
lecturer_2.courses_attached += ["Git"]

reviewer_1 = Reviewer("Анна", "Дмитриева")
reviewer_1.courses_attached += ["Python"]

reviewer_2 = Reviewer("Алексей", "Симонов")
reviewer_2.courses_attached += ["Git"]
reviewer_2.courses_attached += ["Python"]

list_student = [student_1, student_2]
list_lecturer = [lecturer_1, lecturer_2]


def average_grades_lecturers(lecturers, courses):
    sum_course_grade = 0
    iterator = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 1)


def average_grades_students(students, courses):
    sum_course_grade = 0
    iterator = 0
    for student in students:
        for key, value in student.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 1)


student_1.rate_lecturer(lecturer_2, "Git", 9)
student_1.rate_lecturer(lecturer_1, "Git", 8)
student_1.rate_lecturer(lecturer_1, "Git", 8)
student_1.rate_lecturer(lecturer_2, "Python", 9)
student_2.rate_lecturer(lecturer_2, "Python", 10)
student_2.rate_lecturer(lecturer_1, "Python", 10)

reviewer_1.rate_student_hw(student_1, "Python", 10)
reviewer_1.rate_student_hw(student_2, "Git", 8)
reviewer_1.rate_student_hw(student_1, "Git", 10)
reviewer_2.rate_student_hw(student_1, "Python", 10)
reviewer_2.rate_student_hw(student_2, "Python", 7)
reviewer_2.rate_student_hw(student_1, "Git", 7)
reviewer_2.rate_student_hw(student_2, "Python", 8)

print("=" * 80)
print("Задание №3\n")

print("Ревьюеры:\n")
print(f"{reviewer_1}\n")
print(f"{reviewer_2}\n")

print("Лекторы:\n")
print(f"{lecturer_1}\n")
print(f"{lecturer_2}\n")

print("Студенты:\n")
print(f"{student_1}\n")
print(f"{student_2}\n")

print("Сравнение студентов:\n")
# Сравнение студентов по средней оценке за домашние задания:
print(
    f"Студент {student_1.name} {student_1.surname} учится лучше чем студент {student_2.name} {student_2.surname}?\nРезультат:{student_1 < student_2}\n")

print("Сравнение лекторов:\n")
# Сравнение лекторов по средней оценке за лекции:

print(
    f"Лектор {lecturer_1.name} {lecturer_1.surname} нравится студентам больше чем лектор {lecturer_2.name} {lecturer_2.surname}?\nРезультат:{lecturer_1 < lecturer_2}\n")

print("=" * 80)

print("Задание №4\n")

# Подсчет средней оценки за курсы по дз и за леции:
print(f'Средняя оценка студентов за курс Python: {average_grades_students(list_student, "Python")}')
print(f'Средняя оценка студентов за курс Git: {average_grades_students(list_student, "Git")}')
print(f'Средняя оценка лекторов за курс Python: {average_grades_lecturers(list_lecturer, "Python")}')
print(f'Средняя оценка лекторов за курс Git: {average_grades_lecturers(list_lecturer, "Git")}')