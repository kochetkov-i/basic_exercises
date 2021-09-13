# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
student_repited_names = dict((student['first_name'], students.count(student)) for student in students)
for key in student_repited_names:
    output_repired_student = f"{key}: {student_repited_names[key]}"
    print(output_repired_student)


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
maximum_repited_names = 0

student_repited_names = dict((student['first_name'], students.count(student)) for student in students)
for key in student_repited_names:
    if maximum_repited_names < student_repited_names[key]:
        output_repired_student = f"Самое частое имя среди учеников: {key}"
        maximum_repited_names = student_repited_names[key]
print(output_repired_student)


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


for school_class in school_students:
    maximum_repited_names = 0
    student_repited_names = dict((student['first_name'], school_class.count(student)) for student in school_class)
    for key in student_repited_names:
        if maximum_repited_names < student_repited_names[key]:
            output_repired_student = f"Самое частое имя в классе {school_students.index(school_class)+1}: {key}"
            maximum_repited_names = student_repited_names[key]
    print(output_repired_student)
    

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
female = {'first_name': 'девочки'}
male = {'first_name': 'мальчики'}

for school_class in school:
    for student in school_class["students"]:
        if is_male.get(student["first_name"]):
            student["first_name"] = male["first_name"]
        else:
            student["first_name"] = female["first_name"]
    output_gender_counts = f"Класс {school_class['class']}: девочки {school_class['students'].count(female)}, мальчики {school_class['students'].count(male)}"
    print(output_gender_counts)

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

female = 0
male = 0

for school_class in school:
    school_class['male'] = 0
    school_class['female'] = 0
    for student in school_class["students"]:
        if is_male.get(student['first_name']):
            school_class['male'] += 1
        else:
            school_class['female'] += 1
    if male < school_class['male']:
        male = school_class['male']
        output_male_max = f"Больше всего мальчиков в классе {school_class['class']}"
    if female < school_class['female']:
        female = school_class['female']
        output_female_max = f"Больше всего девочек в классе {school_class['class']}"
print(output_male_max)
print(output_female_max)
