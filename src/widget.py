def mask_account(number: str) -> str:
    '''Функия накладывает маску на номер карты или счета в зависимости от длины номера'''
    separate_number = number.split()
    if len(separate_number[-1]) == 16:
        number_card_mask = f"{separate_number[-1][:6]}{"*" * 6}{separate_number[-1][-4:]}"
        return separate_number[0] + " " + number_card_mask
    elif len(separate_number[-1]) > 16:
        number_account_mask = f"**{separate_number[-1][-4:]}"
        return separate_number[0] + " " + number_account_mask


def get_date(date: str) -> str: #"2024-03-11T02:26:18.671407"
    '''Функция переводит дату из одного формата в другой'''
    separate_date = date.split("T")[0]
    year, month, day = separate_date.split("-")
    return f"{day}.{month}.{year}"
