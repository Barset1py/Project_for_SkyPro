from src import masks, widget

input_numbers_card = input("Номер карты: ")
input_account_number = input("Номер счета: ")

print(f"Маска номера карты: {masks.get_mask_card_number(input_numbers_card)}")
print(f"Маска номера счета: {masks.get_mask_account(input_account_number)}\n")

print("Введите номер счета или карты")
input_numbers_account = input("В формате <имя счета или карты> <номер карты или счета>: ")
print(widget.mask_account_card(input_numbers_account))

print("Введите дату")
format_date = input("В формате <2025-01-01T00:00:00.000000>: ")
print(widget.get_date(format_date))
