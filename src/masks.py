def get_mask_card_number(number_card: str) -> str:
    """Функция принимает номер карты, и накладывает маску на карту"""
    mask_number = f"{number_card[:6]}******{number_card[-4:]}"
    return " ".join(mask_number[i : i + 4] for i in range(0, 16, 4))


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета, и накладывает маску на счет"""
    return f"**{account_number[-4:]}"
