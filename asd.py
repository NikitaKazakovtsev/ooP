class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)   
    def rate_hw_(self, Lecturer1, course, grade):
        if isinstance(Lecturer1, Lecturer) and course in self.courses_in_progress and course in Lecturer1.courses_attached:
            if course in Lecturer1.grades_:
                Lecturer1.grades_[course] += [grade]
            else:
                Lecturer1.grades_[course] = [grade]
        else:
            return 'Ошибка'    
    def _average_rating1(self):
        self.average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return self.average
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self._average_rating1()}\nКурсы в процессе изучения:{" ".join(self.courses_in_progress)}\nЗавершенные курсы:{" ".join(self.finished_courses)}'
        return res
    def __lt__(self, st):
        if not isinstance(st, Student):
            print('not a student')
            return
        return self._average_rating1 < st._average_rating1


     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_ = {}
    def _average_rating(self):
        self.average = round(sum(sum(self.grades_.values(), [])) / len(sum(self.grades_.values(), [])), 1)
        return self.average
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции:{self._average_rating()}'
        return res
    def __lt__(self, lt):
        if not isinstance(lt, Lecturer):
            print('not a Lecturer')
            return
        return self._average_rating < lt._average_rating

class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

l1 = Lecturer('Ruoy', 'Eman')
l2 = Lecturer('boy', 'karl')

l2.courses_attached += ['Python']
l1.courses_attached += ['Python']

s1 = Student('Some', 'Buddy', 'm')
s1.add_courses('Python')


s2 = Student('tan', 'boba', 'g')
s2.courses_in_progress += ['Python']

s1.rate_hw_(l1, 'Python', 10)
s1.rate_hw_(l1, 'Python', 9)
s1.rate_hw_(l1, 'Python', 8)
s2.rate_hw_(l2, 'Python', 10)
s2.rate_hw_(l2, 'Python', 8)
s2.rate_hw_(l2, 'Python', 7)

print(l1.grades_)
print(l1)

r1 = Reviewer('bobs', 'giga')
r1.courses_attached += ['Python']
r2 = Reviewer('bobs', 'giga')
r2.courses_attached += ['Python']
 
 
r1 = Reviewer('Some', 'Buddy')
r1.courses_attached += ['Python']
 
r1.rate_hw(s1, 'Python', 10)
r1.rate_hw(s1, 'Python', 9)
r1.rate_hw(s1, 'Python', 10)
r2.rate_hw(s2, 'Python', 10)
r2.rate_hw(s2, 'Python', 8)
r2.rate_hw(s2, 'Python', 9)
 


std = [s1, s2]
def grade_s(std, course):
    sum = 0
    count = 0
    for person in std:
        for s in person.grades[course]:
            sum += s
            count += 1
    return round(sum/count, 1)
print(grade_s(std,'Python'))


lek = [l1, l2]
def grade_l(lek, course):
    sum = 0
    count = 0
    for person in lek:
        for s in person.grades_[course]:
            sum += s
            count += 1
    return round(sum/count, 1)
print(grade_l(lek,'Python'))


print(s1)