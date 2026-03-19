def filter_by_currency(transaction: list, currency: str):
    result = []
    for item in transaction:
        operation_user = item.get("operationAmount", {})
        currency_user = operation_user.get("currency", {})
        code_currency = currency_user.get("code", {})
        if code_currency == currency:
            result.append(item)
    return result


def transaction_descriptions(transactions: list):
    for item in transactions:
        yield item.get("description", {})


def card_number_generator(start: int, end: int):
    for num in range(start, end + 1):
        num_str = f"{num:016d}"
        result = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
        yield result
