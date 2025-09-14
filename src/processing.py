from src import widget

def filter_by_state(data: list[dict[str, str]], state: str='EXECUTED') -> list[dict[str, str]]:
    '''Функция сортирует список по параметру "state"'''
    sorted_list = []
    for item in data:
        if item['state'] == state:
            sorted_list.append(item)
    return sorted_list


def sort_by_date(data: list[dict[str, str]], reverse_sorted: bool=False) -> list[dict[str, str]]:
    '''Функция сортирует список по дате от большего к меньшему'''
    return sorted(
        data,
        key=lambda x: widget.get_date(x['date']),  # Используем преобразованную дату
        reverse=reverse_sorted
    )
