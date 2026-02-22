def filter_by_state(my_dicti, optional='EXECUTED'):
    '''
    Функция принимает список словарей, и опциональный параметр.
    Возвращает новый список словарей, у которых ключ 'State' соответствует указанному значению
    '''
    return [item for item in my_dicti if item.get('state') == optional]


def sort_by_date(data, reverse=True):
    '''
    Функция принимает список словарей и опциональный параметр, задающий порядок сортировки.
    Возвращает новый список отфильтрованный по дате.
    False: от меньшего к большему, True: от большего к меньшему.
    '''
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
