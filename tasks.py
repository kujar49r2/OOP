# # task 1
# class Gun:
#     def shoot(self):
#         print('pif')

# # task 2
# class User:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.friends = 0

#     def add_friends(self, n):
#         self.friends += n

# # task 3
# class House:
#     def __init__(self, color, rooms) -> None:
#         self.color = color
#         self.rooms = rooms
    
#     def paint(self, new_color):
#         self.color = new_color

#     def add_rooms(self, n):
#         self.rooms += n

# # task 4
# from math import pi
# class Circle:
#     def __init__(self, radius) -> None:
#         self.radius = radius
#         self.diameter = radius * 2
#         self.area = 2 * pi * (radius * radius)

# # task 5
# class Bee:
#     def __init__(self, x=0, y=0) -> None:
#         self.x = x
#         self.y = y
#     def move_up(self, n):
#         self.y += n
#     def move_down(self, n):
#         self.y -=n
#     def move_right(self, n):
#         self.x += n
#     def move_left(self, n):
#         self.x -= n    

# # task 6, 7
# class Gun:
#     def __init__(self) -> None:
#         self.n = 0
    
#     def shoot(self):
#         if self.n % 2 == 0:
#             print('pif')
#         else:
#             print('paf')
#         self.n += 1
    
#     def shots_count(self):
#         return self.n
    
#     def shots_reset(self):
#         self.n = 0
# # task 10
# class Numbers:
#     def __init__(self) -> None:
#         self.numb = []

#     def add_number(self, n):
#         self.numb.append(n)

#     def get_even(self):
#         return [i for i in self.numb if i % 2 == 0]
    
#     def get_odd(self):
#         return [i for i in self.numb if i % 2 != 0]
# ----------------------------------------------------------------------
            # Getter, Setter, Deleter
# # task 1
# from math import pi
# class Circle:
#     def __init__(self, radius) -> None:
#         self._radius = radius
#         self._diameter = radius * 2
#         self._area = pi * radius**2

#     def get_radius(self):
#         return self._radius
    
#     def get_diameter(self):
#         return self._diameter
    
#     def get_area(self):
#         return self._area

# task 2
# class BankAccount:
#     def __init__(self, balance=0) -> None:
#         self._balance = balance

#     def get_balance(self):
#         return self._balance
    
#     def deposit(self, amount):
#         self._balance += amount

#     def withdraw(self, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#         else:
#             raise ValueError('На счете недостаточно средств')
        
#     def transfer(self, account, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#             account._balance += amount
#         else:
#             raise ValueError('На счете недостаточно средств')
# ----------------------------------------------------------------------------
#                       property
# task 1
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def get_perimeter(self):
#         return (self.length + self.width) * 2
    
#     def get_area(self):
#         return self.length * self.width
    
#     perimeter = property(get_perimeter)
#     area = property(get_area)
# task 2
# class HourClock:
#     def __init__(self, hours) -> None:
#         if hours in range(1, 13):
#             self._hours = hours
#         else:
#             raise ValueError('Некорректное время')
      
#     def get_hours(self):
#         return self._hours
    
#     def set_hours(self, hours):
#         if hours in range(1, 13):
#             self._hours = hours
#         else:
#             raise ValueError('Некорректное время')
        
#     hours = property(fget=get_hours, fset=set_hours)

# task 3
# class Person:
#     def __init__(self, name, surname) -> None:
#         self._name = name
#         self._surname = surname
    
#     def get_name(self):
#         return self._name

#     def get_surname(self):
#         return self._surname
    
#     def get_fullname(self):
#         return (self._name + ' ' + self._surname)
    
#     def set_name(self, name):
#         self._name = name

#     def set_surname(self, surname):
#         self._surname = surname

#     def set_fullname(self, fullname):
#         self._name = fullname.split()[0]
#         self._surname = fullname.split()[1]

#     name = property(fget=get_name, fset=set_name)
#     surname = property(fget=get_surname, fset=set_surname)
#     fullname = property(fget=get_fullname, fset=set_fullname)
# ---------------------------------------------------------------------------------------    
#                        decorator 
#task 1
# class Person:
#     def __init__(self, name, surname) -> None:
#         self.name = name
#         self.surname = surname

#     @property
#     def fullname(self):
#         return f'{self.name} {self.surname}'
    
#     @fullname.setter
#     def fullname(self, fullname):
#         self.name, self.surname = fullname.split()

# # task 2
# def hash_function(password):
#     hash_value = 0
#     for char, index in zip(password, range(len(password))):
#         hash_value += ord(char) * index
#     return hash_value % 10 ** 9

# class Account:
#     def __init__(self, login, password) -> None:
#         self._login = login
#         self._password = password

#     @property
#     def login(self):
#         return self._login
    
#     @login.setter
#     def login(self, login):
#         raise AttributeError('Изменение логина невозможно')
    
#     @property
#     def password(self):
#         return hash_function(self._password)
    
#     @password.setter
#     def password(self, new_password):
#         self._password = new_password

#                   method of class and statistic method
# # task 1
# class Circle:
#     def __init__(self, radius) -> None:
#         self.radius = radius

#     @classmethod
#     def from_diameter(cls, diameter):
#         return cls(diameter/2)

# # task 2
# class Pet:
#     lst_of_pets = []
#     def __init__(self, name) -> None:
#         self.name = name
#         Pet.lst_of_pets.append(self)

#     @classmethod
#     def first_pet(cls):
#         if Pet.lst_of_pets == []:
#             return None
#         else:
#             return Pet.lst_of_pets[0]
        
#     @classmethod
#     def last_pet(cls):
#         if Pet.lst_of_pets == []:
#             return None
#         else:
#             return Pet.lst_of_pets[-1]
        
#     @classmethod
#     def num_of_pets(cls):
#             return len(Pet.lst_of_pets)

class StrExtension:

    @staticmethod
    def remove_vowels(s):
        return ''.join([i for i in s if i not in 'AEIOUYaeiouy'])
    
    @staticmethod
    def leave_alpha(s):
        return ''.join([i for i in s if i.isalpha()])
    
    @staticmethod
    def replace_all(s, chars, char):
        for i in chars:
            s = s.replace(i, char)
        return s

print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
    


        
