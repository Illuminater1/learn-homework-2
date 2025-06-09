"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='UTF-8') as file, open('referat2.txt', 'w', encoding='UTF-8') as new_file:
        text = file.read()
        words_count = len(text.split())
        print(f'В тексте {words_count} слов')
        text = text.replace('.', '!')
        print(text, file=new_file)


if __name__ == "__main__":
    main()
