# === Stage 12: Слияние записей ===
# Project: MedicineBox
from itertools import product


def join_records(primary, secondary):
    """Объединяет две записи «препарат» попарно по всем комбинациям полей."""
    fields = ("название", "форма", "количество", "срок годности")
    combinations = []
    for values in product(*[primary[f] for f in fields],
                           *[secondary[f] for f in fields]):
        record = {}
        for field, value in zip(fields, values):
            record[field] = value
        combinations.append(record)
    return combinations


def choose_winner(records, field, strategy):
    """Выбирает победителя среди объединённых записей по заданному полю."""
    if strategy == "max":
        return max(records, key=lambda record: record[field])
    if strategy == "min":
        return min(records, key=lambda record: record[field])
    if strategy == "first":
        return records[0]
    if strategy == "last":
        return records[-1]
    raise ValueError("Неизвестная стратегия выбора победителя")


def combine_and_select(primary, secondary, field, strategy):
    """Объединяет записи и выбирает победителя по указанному полю."""
    records = join_records(primary, secondary)
    return choose_winner(records, field, strategy)


if __name__ == "__main__":
    primary = {"название": "Аспирин", "форма": "таблетки",
               "количество": 100, "срок годности": "2025-12-31"}
    secondary = {"название": "Парацетамол", "форма": "сироп",
                 "количество": 250, "срок годности": "2026-06-30"}
    result = combine_and_select(primary, secondary, "срок годности", "max")
    print(result)
