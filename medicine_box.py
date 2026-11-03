# === Stage 1: Каркас модуля ===
# Project: MedicineBox
from datetime import date, timedelta


class Medicine:
    def __init__(self, name, form, quantity, expiry):
        self.name = name
        self.form = form
        self.quantity = quantity
        self.expiry = expiry

    def __str__(self):
        return f"{self.name} ({self.form}), шт: {self.quantity}, до: {self.expiry}"


def make_demo():
    return [
        Medicine("Аспирин", "Таб. 500 мг", 20, date.today() + timedelta(days=365)),
        Medicine("Парацетамол", "Таб. 500 мг", 10, date.today() + timedelta(days=90)),
        Medicine("Перекись водорода", "Раствор 3%", 1, date.today() + timedelta(days=180)),
    ]


def main():
    meds = make_demo()
    for m in meds:
        print(m)


if __name__ == "__main__":
    main()
