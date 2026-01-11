import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_date, mask_account_card


def test_get_mask_card_number(num_card):
    assert get_mask_card_number("1234123412341234") == num_card


def test_get_mask_account(num_account):
    assert get_mask_account("1263789612873678123121234") == num_account


@pytest.mark.parametrize('value, expected', [
    ('Visa 1234123412341234', 'Visa 1234 12** **** 1234'),
    ('Qiwi 484698468468464684681234', 'Qiwi **1234')
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize('time, expected', [
    ('2025-01-01T00:00:00.000000', '01.01.2025'),
    ('2026-12-31T00:00:00.000000', '31.12.2026')
])
def test_get_date(time, expected):
    assert get_date(time) == expected