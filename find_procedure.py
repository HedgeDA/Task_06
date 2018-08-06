# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os
import subprocess


# Состояния поиска. 0 - новый поиск, 1 - продолжение поиска
STATE_NEW_SEARCH = 0
STATE_CONTINUE_SEARCH = 1


def launch_chrome():
    print()
    input('После нажатия ввод, запустится браузер chrome с открытой страницей google.com')

    try:
        # По какаим то причинам иногда запуск выполняется с командой Popen иногда с командой Run
        subprocess.Popen('cmd /c start chrome "http://www.google.com" --new-window', shell=True)
    except OSError:
        print('Ошибка запуска браузера')


def main():
    migrations = 'Migrations'
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # ваша логика
    print('Инструкция:')
    print('1. Ввод пустой строки в качестве начального значения поиска перейдет ко второй части задания.')
    print('2. Ввод пустой строки в качестве продолжающего значения поиска начнет новый поиск.')
    print()

    find_state = STATE_NEW_SEARCH;

    # формируем абсолютный путь к директории Migrations
    migration_dir = os.path.join(current_dir, 'Migrations')

    # сформируем список sql файлов для дальнешйего поиска нужных строк файлов
    full_list = list()
    for path in os.listdir(migration_dir):
        file_name, file_extension = os.path.splitext(path)

        if file_extension.lower() == '.sql':
            full_list.append(file_name)

    print('Всего файлов в директории поиска: {}'.format(len(full_list)))
    print()

    # список найденных файлов
    find_list = list()

    while True:
        if find_state == STATE_NEW_SEARCH:
            find_list = list(full_list)

            print()
            str = input('Введите строку начала поиска:')
        elif find_state == STATE_CONTINUE_SEARCH:
            print()
            str = input('Введите строку продолжения поиска:')
        else:
            print('Неизвестное сосотяние поиска')
            break

        if not str:
            if find_state == STATE_NEW_SEARCH:
                break
            else:
                find_state = STATE_NEW_SEARCH

                continue
        else:
            find_state = STATE_CONTINUE_SEARCH

        new_find_list = list()
        for path in find_list:
            with open(os.path.join(migration_dir, path)) as file:
                for line in file:
                    if str in line:
                        new_find_list.append(path)

                        break

        find_list = new_find_list

        if len(find_list) > 10:
            print('... большой список файлов ...')
        else:
           for path in find_list:
               print(path)

        print('Всего найдено файлов: {}'.format(len(find_list)))

    print()
    print('---------------------------------------------------------------------------')
    print('Вторая часть задания.')

    launch_chrome()

    print()
    print('Работа завершена.')


if __name__ == '__main__':
    main()