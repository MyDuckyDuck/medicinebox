# === Stage 9: Группировка ===
# Project: MedicineBox
from collections import OrderedDict


def group_by_form(medicines):
    """Группирует список препаратов по полю 'форма' и подсчитывает
    количество препаратов в каждой группе.

    medicines: итерируемый объект, содержащий словари с полями
        'название', 'форма', 'количество', 'срок годности'.
    Возвращает OrderedDict вида {'форма': {'название': количество}}.
    """
    grouped = OrderedDict()
    for medicine in medicines:
        form = medicine.get('форма', 'без формы')
        name = medicine.get('название', 'без названия')
        count = int(medicine.get('количество', 0))
        grouped.setdefault(form, {})[name] = count
    return grouped


def total_per_form(grouped):
    """Подсчитывает общее количество препаратов в каждой группе.

    grouped: результат работы функции group_by_form.
    Возвращает OrderedDict вида {'форма': общее_количество}'.
    """
    totals = OrderedDict()
    for form, medicines in grouped.items():
        totals[form] = sum(medicines.values())
    return totals


def print_report(grouped, totals):
    """Выводит отчёт о группировке препаратов по форме.

    grouped: результат работы функции group_by_form.
    totals: результат работы функции total_per_form.
    """
    print('Группировка препаратов по форме:')
    print('-' * 40)
    for form, medicines in grouped.items():
        print('Форма: {}'.format(form))
        for name, count in medicines.items():
            print('  {} - {}'.format(name, count))
        print('  Итого: {}'.format(totals[form]))
        print('-' * 40)


if __name__ == '__main__':
    sample = [
        {'название': 'Аспирин', 'форма': 'таблетки', 'количество': 10, 'срок годности': '2025-12-31'},
        {'название': 'Парацетамол', 'форма': 'таблетки', 'количество': 20, 'срок годности': '2025-11-30'},
        {'название': 'Амброксол', 'форма': 'сироп', 'количество': 150, 'срок годности': '2025-10-15'},
        {'название': 'Перекись водорода', 'форма': 'раствор', 'количество': 50, 'срок годности': '2025-09-01'},
        {'название': 'Йод', 'форма': 'раствор', 'количество': 30, 'срок годности': '2025-08-20'},
    ]
    grouped = group_by_form(sample)
    totals = total_per_form(grouped)
    print_report(grouped, totals)
