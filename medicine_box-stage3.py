# === Stage 3: Хранилище в памяти ===
# Project: MedicineBox
from datetime import date


class Medicine:
    def __init__(self, name, form, quantity, expiry):
        self.name = name
        self.form = form
        self.quantity = quantity
        self.expiry = expiry

    def __repr__(self):
        return f"Medicine(name={self.name!r}, form={self.form!r}, " \
               f"quantity={self.quantity}, expiry={self.expiry!r})"


class MedicineStore:
    def __init__(self):
        self._medicines = {}

    def add(self, medicine):
        self._medicines[medicine.name] = medicine
        return medicine

    def get(self, name):
        return self._medicines.get(name)

    def list_medicines(self):
        return list(self._medicines.values())


if __name__ == "__main__":
    store = MedicineStore()

    store.add(Medicine("Аспирин", "таблетки", 10, date(2026, 3, 15)))
    store.add(Medicine("Парацетамол", "сироп", 5, date(2025, 12, 1)))
    store.add(Medicine("Бинт", "пакет", 2, date(2027, 6, 30)))

    for medicine in store.list_medicines():
        print(medicine)

    print(store.get("Парацетамол"))
    print(store.get("Не существует"))
