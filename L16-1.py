class Person:
    def __init__(self, name, surname, age):
        self.age = age
        self.surname = surname
        self.name = name

    def __repr__(self):
        return f'Person: {self.name} {self.surname}\n' \
               f'age: {self.age}'


class Student(Person):
    def __init__(self, name, surname, age, group, rating):
        super().__init__(name, surname, age)
        self.group = group
        self.rating = rating

    def __repr__(self):
        return f'Student: {self.name} {self.surname}\n' \
               f'Age: {self.age}\n' \
               f'Group: {self.group}\n' \
               f'Rating: {self.rating}'


class Teacher(Person):
    def __init__(self, name, surname, age, subject, salary, experience):
        super().__init__(name, surname, age)
        self.subject = subject
        self.experience = str(experience)
        self.salary = str(salary)

    def __repr__(self):
        return f'Teacher: {self.name} {self.surname}\n' \
               f'Age: {self.age}\n' \
               f'Subject: {self.subject}\n' \
               f'Salary: {self.salary}\n' \
               f'Experience: {self.experience} year(s)'


student = Student('Dan', 'Shkarupa', '18', '10-B', '9.5')
teacher = Teacher('Olena', 'Zinchenko', '42', 'English', 18400, 13)
print(teacher.__dict__)
print(student)
print(teacher)
