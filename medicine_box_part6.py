# === Stage 6: Генерация идентификаторов ===
# Project: MedicineBox
PREFIX = "MB"


def new_id(base: str, existing: list[str]) -> str:
    name = str(base).strip().lower()
    candidate = f"{PREFIX}-{name}"
    if candidate not in existing:
        return candidate
    i = 1
    while True:
        candidate = f"{PREFIX}-{name}-{i}"
        if candidate not in existing:
            return candidate
        i += 1
