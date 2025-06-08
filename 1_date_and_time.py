import locale
from datetime import datetime, timedelta


"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    locale.setlocale(locale.LC_TIME, "ru_RU")

    dt_now = datetime.now().date()
    yesterday = dt_now - timedelta(hours=24)
    one_month_later = dt_now - timedelta(days=30)
    print(f"Сегодняшняя дата - {dt_now.strftime('%d %B %Y')} год")
    print(f"Вчерашняя дата - {yesterday.strftime('%d %B %Y')} год")
    print(f"Дата месяц назад - {one_month_later.strftime('%d %B %Y')} год")


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
