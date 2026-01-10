from src import masks


def mask_account_card():
    """Функия накладывает маску на номер карты или счета в зависимости от длины номера"""
    result = None
    input_numbers_account = input("В формате <имя счета или карты> <номер карты или счета>: ")
    while not input_numbers_account:
        print('Поле ввода пустое!')
        input_numbers_account = input("В формате <имя счета или карты> <номер карты или счета>: ")

    separate_num = input_numbers_account.split()
    if len(separate_num[-1]) == 16:
        result = ' '.join(separate_num[:-1]) + " " + masks.get_mask_card_number(separate_num[-1])
    else:
        result = ' '.join(separate_num[:-1]) + " " + masks.get_mask_account(separate_num[-1])
    return result


def get_date(date: str) -> str:
    """Функция переводит дату из одного формата в другой"""
    separate_date = date.split("T")[0]
    year, month, day = separate_date.split("-")
    return f"{day}.{month}.{year}"
