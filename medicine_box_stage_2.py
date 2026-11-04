# === Stage 2: Проверка полей ===
# Project: MedicineBox
import datetime


class InvalidInputError(Exception):
    pass


def normalize_name(name):
    return " ".join(name.strip().split())


def normalize_form(form):
    return form.strip().lower()


def normalize_quantity(quantity):
    try:
        return float(quantity)
    except (TypeError, ValueError):
        raise InvalidInputError("Количество должно быть числом.")


def normalize_expiry(date_value):
    try:
        return datetime.datetime.strptime(date_value.strip(), "%d.%m.%Y").date()
    except (TypeError, ValueError):
        raise InvalidInputError("Срок годности должен быть в формате ДД.ММ.ГГГГ.")


def validate_name(name):
    if not name or not name.strip():
        raise InvalidInputError("Название препарата не может быть пустым.")
    normalized = normalize_name(name)
    if len(normalized) > 100:
        raise InvalidInputError("Название препарата слишком длинное (максимум 100 символов).")
    return normalized


def validate_form(form):
    if not form or not form.strip():
        raise InvalidInputError("Форма препарата не может быть пустой.")
    normalized = normalize_form(form)
    if len(normalized) > 50:
        raise InvalidInputError("Форма препарата слишком длинная (максимум 50 символов).")
    return normalized


def validate_quantity(quantity):
    normalized = normalize_quantity(quantity)
    if normalized <= 0:
        raise InvalidInputError("Количество должно быть больше нуля.")
    return normalized


def validate_expiry(date_value):
    expiry = normalize_expiry(date_value)
    if expiry <= datetime.date.today():
        raise InvalidInputError("Срок годности уже истёк.")
    return expiry


def normalize_packaging(packaging):
    return packaging.strip().lower()


def validate_packaging(packaging):
    if not packaging or not packaging.strip():
        raise InvalidInputError("Упаковка не может быть пустой.")
    normalized = normalize_packaging(packaging)
    if len(normalized) > 100:
        raise InvalidInputError("Упаковка слишком длинная (максимум 100 символов).")
    return normalized


def validate_price(price):
    try:
        normalized = float(price)
    except (TypeError, ValueError):
        raise InvalidInputError("Цена должна быть числом.")
    if normalized < 0:
        raise InvalidInputError("Цена не может быть отрицательной.")
    return normalized


def normalize_and_validate_packaging(packaging):
    return validate_packaging(packaging)


def normalize_and_validate_price(price):
    return validate_price(price)
