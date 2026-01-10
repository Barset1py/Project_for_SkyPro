from src import masks, widget

input_numbers_card = input("Номер карты: ")
input_account_number = input("Номер счета: ")

print(f"Маска номера карты: {masks.get_mask_card_number(input_numbers_card)}")
print(f"Маска номера счета: {masks.get_mask_account(input_account_number)}\n")

print("Введите номер счета или карты")
print(widget.mask_account_card())

print("Введите дату")
print(widget.get_date())
