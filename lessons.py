import math


class Planet:
    def __init__(self, name, radius, average_temp_celcius):
        # функция принимает аргументы и сохраняет их в объекте
        self.name = name
        self.radius = radius
        self.average_temp_celcius = average_temp_celcius
        self.average_temp_fahrenheit = average_temp_celcius * (9 / 5) + 32
        self.surface_area = 4 * math.pi * radius**2
        print(f'Создаем планету {name}')

    def show_planet_info(self):
        print(f'Название планеты: {self.name}\n'
              f'Радиус: {self.radius} км\n'
              f'Площадь поверхности: {self.surface_area} кв.км\n'
              f'Средняя температура(градусы цельсия): {self.average_temp_celcius}\n'
              f'Средняя температура(градусы фаренгейта): {self.average_temp_fahrenheit}')


    def __str__(self):
        return f'Объект планеты {self.name}'


class Contact:
    def __init__(self, name, phone, address, birthday):
        #  Функция, которая принимает агрументы name, phone, address, birthday
        #  создает объект и в нем сохраняет их значения
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = birthday
        print(f'Создан новый контакт: {name}')


    def show_contact(self):
        print(f'Имя: {self.name} \n'
              f'Телефон: {self.phone}\n'
              f'Адрес: {self.address}\n'
              f'Дата рождения: {self.birthday}')

    def __str__(self):
        return f'Контакт: {self.name}'


leo = Contact(name='Лев Толстой',
              phone='+7 (123) 456-78-90',
              address='Ясная поляна',
              birthday='9.09.1828')
mike = Contact('Михаил Булгаков', '2-03-27', 'Россия, Москва, Большая Пироговская, дом 35б, кв. 6', '15.05.1891')
vlad = Contact('Владимир Маяковский', '73-88', 'Россия, Москва, Лубянский проезд, д. 3, кв. 12', '19.07.1893')



mike.address = 'Россия, Москва, Нащокинский переулок, дом 3, кв. 44'
mike.phone = 'К-058-67'

vlad.address = 'Россия, Москва, Гендриков переулок, дом 15, кв. 5'
vlad.phone = '2-35-71'

vlad.show_contact()
print()

zem = Planet('Земля', 3000, 20)

jupiter = Planet('Юпитер', 69911, -110)
jupiter.show_planet_info()
print()
print(jupiter)