# === Stage 4: Удаление и восстановление ===
# Project: MedicineBox
from datetime import date


class Medication:
    def __init__(self, name, form, quantity, expiration):
        self.name = name
        self.form = form
        self.quantity = quantity
        self.expiration = expiration
        self.deleted = False

    def delete(self):
        self.deleted = True

    def restore(self):
        self.deleted = False

    def is_expired(self, today=None):
        if self.deleted:
            return False
        return self.expiration < (today or date.today())


class MedicationManager:
    def __init__(self):
        self._medications = []
        self._deleted = []

    def add(self, medication):
        self._medications.append(medication)
        return medication

    def get_all(self):
        return [m for m in self._medications if not m.deleted]

    def get_deleted(self):
        return list(self._deleted)

    def find(self, name):
        for m in self._medications:
            if m.name == name and not m.deleted:
                return m
        return None

    def delete(self, name):
        medication = self.find(name)
        if medication and not medication.deleted:
            self._deleted.append(medication)
            self._medications.remove(medication)
            return True
        return False

    def restore(self, name):
        for deleted in self._deleted:
            if deleted.name == name:
                self._deleted.remove(deleted)
                self._medications.append(deleted)
                return True
        return False

    def remove_permanently(self, name):
        for deleted in self._deleted:
            if deleted.name == name:
                self._deleted.remove(deleted)
                return True
        return False


if __name__ == "__main__":
    manager = MedicationManager()
    manager.add(Medication("Аспирин", "таблетки", 10, date(2025, 12, 1)))
    manager.add(Medication("Парацетамол", "сироп", 5, date(2024, 6, 1)))

    print(manager.get_all())
    print(manager.delete("Парацетамол"))
    print(manager.get_all())
    print(manager.restore("Парацетамол"))
    print(manager.get_all())
    print(manager.remove_permanently("Парацетамол"))
    print(manager.get_deleted())
