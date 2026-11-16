# === Stage 7: Сортировка записей ===
# Project: MedicineBox
from datetime import datetime


def sort_key(record):
    created = record.get("created")
    if isinstance(created, datetime):
        created = created.toordinal()
    return (str(record.get("name", "")).lower(), created if created is None else -created)


def sort_records(records, by="name", ascending=True):
    if by == "name":
        key = lambda r: (str(r.get("name", "")).lower(), r.get("created") or datetime.min)
    elif by == "created":
        key = lambda r: (r.get("created") or datetime.min)
    else:
        raise ValueError("Поле для сортировки должно быть 'name' или 'created'")

    if ascending:
        return sorted(records, key=key)
    return sorted(records, key=key, reverse=True)


def sort_records_by_name(records, ascending=True):
    return sort_records(records, by="name", ascending=ascending)


def sort_records_by_created(records, ascending=True):
    return sort_records(records, by="created", ascending=ascending)


if __name__ == "__main__":
    sample = [
        {"name": "Ибупрофен", "created": datetime(2024, 1, 10)},
        {"name": "Аспирин", "created": datetime(2023, 5, 20)},
        {"name": "Парацетамол", "created": datetime(2024, 3, 5)},
    ]

    print("По названию (возрастание):")
    for record in sort_records_by_name(sample, ascending=True):
        print(f"  {record['name']}")

    print("По названию (убывание):")
    for record in sort_records_by_name(sample, ascending=False):
        print(f"  {record['name']}")

    print("По дате создания (возрастание):")
    for record in sort_records_by_created(sample, ascending=True):
        print(f"  {record['name']}")

    print("По дате создания (убывание):")
    for record in sort_records_by_created(sample, ascending=False):
        print(f"  {record['name']}")
