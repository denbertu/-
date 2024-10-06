class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        super().__init__(name, surname)
        self.courses_rates = {}
        self.courses_attached = []

    def average_rate(self):
        list_ = list(self.courses_rates.values())
        new_list = []
        result = "-"
        
        if list_:
            for el in list_:
               for int_ in el:
                    new_list.append(int_)
                    result = sum(new_list) / len(new_list)

        return result

    def __str__(self):
        average_rate = '-'
        average_rate if self.average_rate() == '-' else average_rate == round(self.average_rate(), 1)
        
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_rate}"
        

class Reviewer(Mentor):
    def rate_hw(self, student, lecturer, course, grade):
        if isinstance(student, Student) and isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Student:
    instances = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.instances.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if grade in range(1, 11):
            if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
                if course in lecturer.courses_rates:
                    lecturer.courses_rates[course] += [grade]
                else:
                    lecturer.courses_rates[course] = [grade]
            else:
                return 'Error'
        else:
            return "Entered number is out of range"

    def average_grade(self):
        list_ = list(self.grades.values())
        new_list = []
        result = "-"
        
        if list_:
            for el in list_:
               for int_ in el:
                    new_list.append(int_)
                    result = sum(new_list) / len(new_list)
                    
        return result
    
    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        average_grade = '-'

        average_grade if self.average_grade() == '-' else average_grade == round(self.average_grade(), 1)

        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"
    

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Java']
best_student.finished_courses += ['Python']

average_student = Student('asdasd', 'bvchbnvcn', 'asaaa')
average_student.courses_in_progress += ['Python']
average_student.courses_in_progress += ['Java']
average_student.finished_courses += ['Java']
average_student.finished_courses += ['Python']

top_lect = Lecturer('gdfghfdhfgh', 'fdhgfhfdgh')
top_lect.courses_attached += ['Python']
top_lect.courses_attached += ['Java']

average_lect = Lecturer('sadas', 'adas')
average_lect.courses_attached += ['Python']
average_lect.courses_attached += ['Java']
 
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.rate_hw(best_student, average_lect, 'Python', 10)
reviewer_1.rate_hw(best_student, average_lect, 'Python', 12)
reviewer_1.rate_hw(best_student, average_lect, 'Java', 24)

reviewer_2 = Reviewer('dsgdfhjghk', 'hgjkhjgkjhgkh')
reviewer_2.rate_hw(best_student, average_lect, 'Python', 11)
reviewer_2.rate_hw(best_student, average_lect, 'Python', 11)
reviewer_2.rate_hw(best_student, average_lect, 'Java', 24)

best_student.rate_lecturer(average_lect, 'Python', 133)
best_student.rate_lecturer(average_lect, 'Python', 10)
best_student.rate_lecturer(average_lect, 'Java', 5)


print(average_lect.average_rate())
print(average_lect.__str__())
print(top_lect.average_rate())
print(top_lect.__str__())

print(reviewer_1.__str__())
print(reviewer_2.__str__())

print(best_student.average_grade())
print(best_student.__str__())
print(average_student.average_grade())
print(average_student.__str__())


def students_average_grade(*students, course):
    sum_ = 0
    len_ = 0

    for student in students:
        if course in student.finished_courses:
            if student.grades.get(course):
                for grade in student.grades.get(course):
                        sum_ += grade
                        len_ += 1
    avg = sum_ / len_
        
    return avg


def lectors_average_rate(*lecturers, course):
    sum_ = 0
    len_ = 0

    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            if lecturer.courses_rates.get(course):
                for rate in lecturer.courses_rates.get(course):
                    sum_ += rate
                    len_ += 1
    avg = sum_ / len_
        
    return avg

print(students_average_grade(best_student, average_student, course='Python'))
print(students_average_grade(best_student, average_student, course='Java'))
print(lectors_average_rate(top_lect, average_lect, course='Python'))
print(lectors_average_rate(top_lect, average_lect, course='Java'))
