def filter_by_currency(transaction: list, currency: str):
    """
    Фильтрует транзакции по коду валюты.
    Args:
        transaction: список транзакций (словарей)
        currency: код валюты (обязательный параметр)
    Returns:
        Список транзакций отфильтрованный по указанному коду валюты.
    """
    result = []
    for item in transaction:
        operation_user = item.get("operationAmount", {})
        currency_user = operation_user.get("currency", {})
        code_currency = currency_user.get("code", {})
        if code_currency == currency:
            result.append(item)
    return result


def transaction_descriptions(transactions: list):
    """
    Выводит описание транзакций.
    Args:
        transactions: список транзакций (словарей)
    Yields:
        Строка с описанием транзакций.
    """
    for item in transactions:
        yield item.get("description", {})


def card_number_generator(start: int, end: int):
    """
    Генерирует номера карт.
    Args:
        start: старт диапазона чисел
        end: конец диапазона чисел
    Yields:
        Строка с номером карты указанного диапазона.
    """
    for num in range(start, end + 1):
        num_str = f"{num:016d}"
        result = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
        yield result
