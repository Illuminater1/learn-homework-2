import csv

"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    peoples = [{'name': 'Артем', 'age': 22, 'job': 'инженер'},
           {'name': 'Борис', 'age': 43, 'job': 'технолог'},
           {'name': 'Денис', 'age': 35, 'job': 'рабочий'},
           {'name': 'Сергей', 'age': 56, 'job': 'регулировщик'},
    ]

    with open('new_file.csv', 'w', encoding='UTF-8', newline='') as f:
        header = [i for i in peoples[0]]
        writer = csv.DictWriter(f, header, delimiter=';')
        writer.writeheader()
        for people in peoples:
            writer.writerow(people)

if __name__ == "__main__":
    main()
