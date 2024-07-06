from datetime import datetime, date, timedelta
from decimal import Decimal


goods: dict = {}


def add(items, title, amount, expiration_date=None):
    if expiration_date is None:
        final_expiration_date = None
    else:
        final_expiration_date = datetime.date(
            datetime.strptime(expiration_date, '%Y-%m-%d'))
    if title not in items:
        items[title] = list()
        list.append(items[title], {'amount': amount,
                    'expiration_date': final_expiration_date})
    else:
        list.append(items[title], {'amount': amount,
                    'expiration_date': final_expiration_date})


def add_by_note(items, note):
    all_data = str.split(note, ' ')
    if len(str.split(all_data[-1], '-')) == 3:
        expiration_date = all_data[-1]
        amount = all_data[-2]
        title = str.join(' ', all_data[0:-2])
        add(items, title, Decimal(amount), expiration_date)
    else:
        amount = all_data[-1]
        title = str.join(' ', all_data[0:-1])
        add(items, title, Decimal(amount))


def find(items, needle):
    items_list = []
    finded_goods = []
    for item in items:
        list.append(items_list, item)
    needle = str.lower(needle)
    for item in items_list:
        if needle in str.lower(item):
            list.append(finded_goods, item)
    return finded_goods


def amount(items, needle):
    needle = str.lower(needle)
    count = Decimal('0')
    for item in items:
        if needle in str.lower(item):
            for values in items[item]:
                count += values['amount']
    return count


def expire(items, in_advance_days=0):
    date_for_check = date.today() + timedelta(days=in_advance_days)
    expired_goods = []
    for item in items:
        quantity = Decimal('0')
        name = 0
        for values in items[item]:
            if (
                values['expiration_date'] is not None and
                values['expiration_date'] <= date_for_check
            ):
                quantity += values['amount']
                name = item
        if name != 0:
            expired_goods.append((name, quantity))
    return expired_goods
