import datetime as dt


class Record:
    '''Класс создат объекты в которых хранятся данные о кол-ве, дате и
    комнтарий. При осутствии даты, сохраняется дата на момент
    создания объекта'''
    def __init__(self, amount, comment, date='date_now') -> None:

        self.amount = amount
        self.comment = comment
        self.date = date

        if date == 'date_now':
            self.date = dt.datetime.now().date()
        else:
            date_format = '%d.%m.%Y'
            self.date = dt.datetime.strptime(date, date_format).date()


class Calculator:
    '''Класс Calculator прнимает на вход кол-во едениц которые можно потрать.
    Имее три функции add_record, get_today_stats и get_week_stats.
    add_record добавляет обьект класса Record в список records.
    get_today_stats возвращает кол-во единиц потраченых за день.
    get_week_stats возвращает кол-во единиц потраченых за неделю'''
    def __init__(self, limit) -> None:
        self.limit = limit
        self.records: list = []

    def add_record(self, obj):
        self.records.append(obj)

    def get_today_stats(self) -> int:
        date_now = dt.datetime.now().date()
        spent_cash = 0
        for i in range(0, len(self.records)):
            if self.records[i].date == date_now:
                spent_cash += self.records[i].amount
        return spent_cash

    def get_week_stats(self) -> int:
        date_now = dt.datetime.now().date()
        date_now -= dt.timedelta(days=7)
        spent_week_cash = 0
        for i in range(0, len(self.records)):
            if self.records[i].date > date_now:
                spent_week_cash += self.records[i].amount
        return spent_week_cash


class CaloriesCalculator(Calculator):
    '''Унаследован от класса Calculator.
    Добавлена функция get_calories_remained которая возвращает строку
    с данными сколько сегодня можно еще съесть(в кКал)'''
    def get_calories_remained(self) -> str:
        result = 'Хватит есть!'
        callories = self.limit - self.get_today_stats()

        if callories > 0:
            result = (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                      f'калорийностью не более {callories} кКал')
        else:
            result

        return result


class CashCalculator(Calculator):
    '''Унаследован от класса Calculator.
    Добавлена функция get_today_cash_remained которая примает а вход 
    валюту(rub, usd или eur) и возвращает строку
    с данными сколько сегодня можно еще потратить в укзанной валюте)'''

    USD_RATE = 94.07
    EURO_RATE = 99.93

    def get_today_cash_remained(self, currency) -> str:

        result = 'Денег нет, держись'

        balance = self.limit - self.get_today_stats()

        if currency == 'rub':
            balance
            currency = 'руб'
        elif currency == 'usd':
            balance /= self.USD_RATE
            currency = 'USD'
        elif currency == 'eur':
            balance /= self.EURO_RATE
            currency = 'Euro'

        if balance > 0:
            result = f'На сегодня осталось {balance:.2f} {currency}'
        elif balance < 0:
            balance *= -1
            result = f'Денег нет, держись: твой долг - {balance:.2f} {currency}'
        else:
            result

        return result


cash_calculator = CashCalculator(1000)

r1 = Record(750, 'comment 1')
r2 = Record(750, 'comment 2')
r3 = Record(100, 'comment 3', '11.04.2024')

cash_calculator.add_record(r1)
cash_calculator.add_record(r2)
cash_calculator.add_record(r3)

print(cash_calculator.get_today_cash_remained('eur'))
print(cash_calculator.get_today_stats())
print(cash_calculator.get_week_stats())
print(Record.__doc__)
print()

r4 = Record(amount=1186, comment='Кусок тортика. И ещё один.')
r5 = Record(amount=84, comment='Йогурт.')
r6 = Record(amount=1240, comment='Баночка чипсов.')

callories_calc = CaloriesCalculator(2500)
callories_calc.add_record(r4)
callories_calc.add_record(r5)
callories_calc.add_record(r6)

print(callories_calc.get_week_stats())
