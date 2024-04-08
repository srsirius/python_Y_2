import math


#
#
# class Planet:
#     def __init__(self, name, radius, average_temp_celcius):
#         # функция принимает аргументы и сохраняет их в объекте
#         self.name = name
#         self.radius = radius
#         self.average_temp_celcius = average_temp_celcius
#         self.average_temp_fahrenheit = average_temp_celcius * (9 / 5) + 32
#         self.surface_area = 4 * math.pi * radius**2
#         print(f'Создаем планету {name}')
#
#     def show_planet_info(self):
#         print(f'Название планеты: {self.name}\n'
#               f'Радиус: {self.radius} км\n'
#               f'Площадь поверхности: {self.surface_area} кв.км\n'
#               f'Средняя температура(градусы цельсия): {self.average_temp_celcius}\n'
#               f'Средняя температура(градусы фаренгейта): {self.average_temp_fahrenheit}')
#
#
#     def __str__(self):
#         return f'Объект планеты {self.name}'
#
#
# class Contact:
#     def __init__(self, name, phone, address, birthday):
#         #  Функция, которая принимает агрументы name, phone, address, birthday
#         #  создает объект и в нем сохраняет их значения
#         self.name = name
#         self.phone = phone
#         self.address = address
#         self.birthday = birthday
#         print(f'Создан новый контакт: {name}')
#
#
#     def show_contact(self):
#         print(f'Имя: {self.name} \n'
#               f'Телефон: {self.phone}\n'
#               f'Адрес: {self.address}\n'
#               f'Дата рождения: {self.birthday}')
#
#     def __str__(self):
#         return f'Контакт: {self.name}'
#
#
# leo = Contact(name='Лев Толстой',
#               phone='+7 (123) 456-78-90',
#               address='Ясная поляна',
#               birthday='9.09.1828')
# mike = Contact('Михаил Булгаков', '2-03-27', 'Россия, Москва, Большая Пироговская, дом 35б, кв. 6', '15.05.1891')
# vlad = Contact('Владимир Маяковский', '73-88', 'Россия, Москва, Лубянский проезд, д. 3, кв. 12', '19.07.1893')
#
#
#
# mike.address = 'Россия, Москва, Нащокинский переулок, дом 3, кв. 44'
# mike.phone = 'К-058-67'
#
# vlad.address = 'Россия, Москва, Гендриков переулок, дом 15, кв. 5'
# vlad.phone = '2-35-71'
#
# vlad.show_contact()
# print()
#
# zem = Planet('Земля', 3000, 20)
#
# jupiter = Planet('Юпитер', 69911, -110)
# jupiter.show_planet_info()
# print()
# print(jupiter)

# class Bird:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#
#     def show(self):
#         print(f'{self.name} носит одежду размера {self.size}.')
#
#
# class Parrot(Bird):
#     def __init__(self, name, size, sound):
#         super().__init__(name, size)
#         self.sound = sound
#
#     def show(self):
#         print(f'{self.name} носит одежду размера {self.size} и {self.sound}.')
#
#
# class Predator(Bird):
#     def __init__(self, name, size, claws_size):
#         super().__init__(name, size)
#         self.claws_size = claws_size
#
#     def show(self):
#         print(f'{self.name} носит одежду размера {self.size} и '
#               f'когти размера {self.claws_size}.')
#
#
# class Egg(Predator):
#     def show(self):
#         print(f'Из яйца вылупится птичка {self.name} размера {self.size} с '
#               f'когтями размера {self.claws_size}.')
#
#
# bird1 = Bird('Птичка', 3)
#
# bird1.show()
#
# parrot1 = Parrot('Попка', 2, 'Попка дурак')
#
# parrot1.show()
#
# egg1 = Egg('Кеша', 1, 1)
#
# egg1.show()


# class User:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#     def show(self):
#         print(f'{self.name} ({self.phone})')
#
#
# # наследуем класс Friend от User
# class Friend(User):
#     # Пишем конструктор класса-наследника,
#     # чтобы он принимал все нужные параметры
#     def __init__(self, name, phone, address):
#         # наследуем функциональность конструктора из класса-родителя
#         super().__init__(name, phone)
#         # добавляем новую функциональность: свойство address
#         self.address = address
#
#     # полностью переопределяем родительский метод show()
#     def show(self):
#         print(f'Имя: {self.name} || '
#               f'Телефон: {self.phone} || '
#               f'Адрес: {self.address}')
#
#
# user1 = User('Kol', '+7 983 123 45 67')
# friend1 = Friend('Den', '+7 983 234 56 78', 'Krasnoobsk')
#
# user1.show()
# friend1.show()


# class Point:
#     def __init__(self, latitude, longitude):
#         self._latitude = latitude
#         self._longitude = longitude
#
#     @property
#     def latitude(self):
#         return self._latitude
#
#     @property
#     def longitude(self):
#         return self._longitude
#
#     #  d = arccos {sin(Фa)·sin(Фb) + cos(Фa)·cos(Фb)·cos(Лa - Лb)}
#     def distance(self, other):
#         self_latitude = math.radians(self.latitude)
#         self_longitude = math.radians(self.longitude)
#         other_latitude = math.radians(other.latitude)
#         other_longitude = math.radians(other.longitude)
#
#         dist = 6371 * math.acos(math.sin(self_latitude) * math.sin(other_latitude) +
#                                 math.cos(self_latitude) * math.cos(other_latitude) *
#                                 math.cos(self_longitude - other_longitude))
#         return dist
#
#
# class City(Point):
#     def __init__(self, latitude, longitude, name, population):
#         super().__init__(latitude, longitude)
#         self.name = name
#         self.population = population
#
#     def show(self):
#         print(f'Город {self.name} имеет население {self.population} чел.')
#
#
# class Mountain(Point):
#     def __init__(self, latitude, longitude, name, height):
#         super().__init__(latitude, longitude)
#         self.name = name
#         self.height = height
#
#     def show(self):
#         print(f'Гора {self.name}:\n'
#               f'высота: {self.height} м.\n'
#               f'широта: {self.latitude}\n'
#               f'долгота: {self.longitude}')
#
#
#
# moscow = City(55.75583, 37.6173, 'Москва', 18_323_456)
# everest = Mountain(27.9880, 86.9252, 'Эверест', 8_848)
#
# moscow.show()
# everest.show()
# print(f'Расстояние от города {moscow.name} до горы {everest.name} равно {moscow.distance(everest):.3f} км.')

class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')


class Student(Human):
    #  Student должен уметь задавать вопросы.
    #  Реализуйте в классе Student метод
    #  ask_question(Human, question).
    #  При вызове этот метод должен:
    #  Напечатать на экране вопрос в формате
    #  <имя человека, которому задаём вопрос>, <текст вопроса>
    #  Задать вопрос question человеку, объекту класса Human.
    #  Имя объекта, которому адресован вопрос,
    #  передаётся при вызове метода ask_question().

    def ask_question(self, someone, question):
        print(f'{someone.name}, {question}')
        someone.answer_question(question)
        print()

class Mentor(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)
class CodeReviewer(Human):
    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)


class Curator(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        elif question == 'как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        else:
            super().answer_question(question)


pit = Student('Петя')
marina = Mentor('Марина')
ira = Curator('Ира')
eugeniy = CodeReviewer('Евгений')
vitaliy = Human('Виталий')

pit.ask_question(marina,'мне грустненько, что делать?')
pit.ask_question(ira,'мне грустненько, что делать?')
pit.ask_question(eugeniy,'когда каникулы?')
pit.ask_question(eugeniy,'что не так с моим проектом?')
pit.ask_question(vitaliy,'как устроиться на работу питонистом?')
pit.ask_question(ira,'как устроиться работать питонистом?')