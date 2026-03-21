import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

result_transaction_usd = [
    {
        'id': 939719570,
        'state': 'EXECUTED',
        'date': '2018-06-30T02:08:58.425572',
        'operationAmount': {
            'amount': '9824.07',
            'currency': {
                'name': 'USD',
                'code': 'USD'
            }
        },
        'description': 'Перевод организации',
        'from': 'Счет 75106830613657916952',
        'to': 'Счет 11776614605963066702'
    }
]
result_transaction_rub = [
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
]

@pytest.mark.parametrize(
    "currency, result",
    [
        ("USD", result_transaction_usd),
        ("RUB", result_transaction_rub),
        ("", [])
    ]
)
def test_filter_by_currency(data_transaction, currency, result):
    result = list(filter_by_currency(data_transaction, currency))
    assert result == result


def test_filter_by_currency_empty_list():
    result = filter_by_currency([], "RUB")
    assert result == 'StopIteration'


def test_transaction_descriptions(data_transaction, transaction_description_empty):
    result = list(transaction_descriptions(data_transaction))
    result_description_empty = list(transaction_descriptions(transaction_description_empty))
    assert result == ['Перевод организации', 'Перевод со счета на счет']

    assert result_description_empty == ['', 'Перевод со счета на счет']

    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, end, expected_num",
    [
        (1, 3, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003']),
        (44, 44, ['0000 0000 0000 0044']),
        (0, 0, ['0000 0000 0000 0000']),
        (9999, 10002, [
            '0000 0000 0000 9999',
            '0000 0000 0001 0000',
            '0000 0000 0001 0001',
            '0000 0000 0001 0002'
        ])
    ]
)
def test_card_number_generator(start, end, expected_num):
    result = list(card_number_generator(start, end))
    assert result == expected_num