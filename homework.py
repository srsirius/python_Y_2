import datetime as dt


class Record:

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
    def get_calories_remained(self) -> str:
        result = 'Хватит есть!'
        callories = self.limit - self.get_today_stats()

        if callories > 0:
            result = f'Сегодня можно съесть что-нибудь ещё, но с общей 
                     калорийностью не более {callories} кКал'
        
        return result


class CashCalculator(Calculator):

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
r4 = Record(100, 'comment 4', '10.04.2024')

cash_calculator.add_record(r1)
cash_calculator.add_record(r2)
cash_calculator.add_record(r3)
cash_calculator.add_record(r4)

print(cash_calculator.get_today_cash_remained('eur'))
print(cash_calculator.get_today_stats())
print(cash_calculator.get_week_stats())
