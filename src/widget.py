from src import masks


def mask_account_card(input_numbers_account):
    """Функия накладывает маску на номер карты или счета в зависимости от длины номера"""
    result = None
    while not input_numbers_account:
        print('Поле ввода пустое!')
        print('Введите номер карты или счета.')
        input_numbers_account = input("В формате <имя счета или карты> <номер карты или счета>: ")
    separate_num = input_numbers_account.split()
    if len(separate_num[-1]) == 16:
        result = ' '.join(separate_num[:-1]) + " " + masks.get_mask_card_number(separate_num[-1])
    else:
        result = ' '.join(separate_num[:-1]) + " " + masks.get_mask_account(separate_num[-1])
    return result


def get_date(format_date):
    """Функция переводит дату из одного формата в другой"""
    while not format_date:
        print('Поле ввода пустое!')
        print('Введите дату.')
        format_date = input("В формате <2025-01-01T00:00:00.000000>: ")
    separate_date = format_date.split("T")[0]
    year, month, day = separate_date.split("-")
    return f"{day}.{month}.{year}"
