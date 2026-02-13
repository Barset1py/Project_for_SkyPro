import pytest


@pytest.fixture
def num_card():
    """Результат маски номера карты."""
    return "1234 12** **** 1234"


@pytest.fixture
def num_account():
    """Результат маски номера банковского счета."""
    return "**1234"


base_transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

@pytest.fixture
def transactions_with_missing_state():
    """Транзакции, где у одной записи нет ключа 'state'."""
    return [
        {'id': 1, 'amount': 100},  # нет 'state'
        {'id': 2, 'state': 'EXECUTED', 'amount': 200},
        {'id': 3, 'amount': 300},  # нет 'state'
    ]

@pytest.fixture
def exec_only():
    """Ожидаемый результат для state == 'EXECUTED'."""
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.fixture
def canceled_only():
    """Ожидаемый результат для state == 'CANCELED'."""
    return [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.fixture(params=[
    ("missing_state", "EXECUTED"),
    ("executed", "EXECUTED"),
    ("canceled", "CANCELED"),
    ("empty_list", "EXECUTED")
])
def test_cases(request, exec_only, canceled_only):
    """
    Параметризованная фикстура готовит входные данные и ожидаемый результат
    для каждого сценария.
    """
    case_name, filter_state = request.param

    if case_name == "missing_state":
        input_data = [
            {'id': 1, 'amount': 100},
            {'id': 2, 'state': 'EXECUTED', 'amount': 200},
            {'id': 3, 'amount': 300}
        ]
        expected = [{'id': 2, 'state': 'EXECUTED', 'amount': 200}]
    elif case_name == "executed":
        input_data = base_transactions
        expected = exec_only
    elif case_name == "canceled":
        input_data = base_transactions
        expected = canceled_only
    elif case_name == "empty_list":
        input_data = []
        expected = []
    else:
        raise ValueError(f"Неизвестный кейс: {case_name}")


    return {
        "name": case_name,
        "input_data": input_data,
        "filter_state": filter_state,
        "expected": expected
    }