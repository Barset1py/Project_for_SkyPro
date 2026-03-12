import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(test_cases):
    """
    Параметризованный тест: проверяет 4 сценария:
    1. Отсутствие ключа 'state' в некоторых записях.
    2. Фильтрация только по 'EXECUTED'.
    3. Фильтрация только по 'CANCELED'.
    4. Пустой входной список.
    """
    result = filter_by_state(test_cases["input_data"], test_cases["filter_state"])
    assert result == test_cases["expected"]


date_reverse_true = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

date_reverse_false = [
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]


@pytest.mark.parametrize(
    "data, reverse, result",
    [
        (date_reverse_true, True, date_reverse_true),
        (date_reverse_false, False, date_reverse_false),
        ([], True, []),
    ],
)
def test_sort_by_date(data, reverse, result):
    """
    Параметризованный тест: проверяет 3 сценария:
    1. Сортировка с reverse=True
    2. Сортировка с reverse=False
    3. Входные данные отсутствуют
    """
    assert sort_by_date(data, reverse) == result
