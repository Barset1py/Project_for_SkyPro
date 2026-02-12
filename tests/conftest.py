import pytest


@pytest.fixture
def num_card():
    """Результат маски номера карты."""
    return "1234 12** **** 1234"


@pytest.fixture
def num_account():
    """Результат маски номера банковского счета."""
    return "**1234"


@pytest.fixture
def input_data_for_test():
    """Входные данные для тестирования функции `filter_by_state`,
    содержит список словарей, с опциональным ключем `state`."""
    return {
        'my_list': [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],

        'list_empty_key': [{'id': 41428829, 'state': '', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],

        'empty_list': []
    }


@pytest.fixture
def output_data_for_test():
    """Ожидаемые результаты функций при тестировании."""
    return {
        'list_executed': [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],

        'list_canceled':[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],

        'list_empty_key': [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],

        'empty_list': []

    }