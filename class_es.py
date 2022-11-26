# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(self.age)
#         print(age)
#
#     def bark(self, age):
#         print(age)
#         self.age = age
#
#
# dog = Dog("Tim", 30)
# dog.bark(12)
# print(dog.age)

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def get_grade(self):
#         return self.grade
#
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)
#
#
# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)
#
# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# course.add_student(s3)
# print(course.get_average_grade())

"""Inheritance"""

# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(f"I am {self.name} and i am {self.age} years old !")
#
#
# class Dog(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#
#     def speak(self):
#         print("bark")
#
#
# class Cat(Pet):
#     def speak(self):
#         print("Meow")
#
#
# p = Pet("tim", 19)
# p.show()
# c = Cat("bill", 34)
# c.show()
# c.speak()
# d = Dog("Jill", 25, "Brown")
# d.show()
# d.speak()

# classmethod


# class Person:
#     num = 0
#
#     def __init__(self, name):
#         self.name = name
#         Person.num_()
#
#     @classmethod
#     def num__(cls):
#         return cls.num
#
#     @classmethod
#     def num_(cls):
#         cls.num += 1
#
#
# p1 = Person("Tim")
#
# print(Person.num__())

# staticmethod

class Math:

    @staticmethod
    def add5(x):
        return x + 5


print(Math.add5(5))
