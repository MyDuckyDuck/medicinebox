# === Stage 5: Связи между сущностями ===
# Project: MedicineBox
def get_medicine_intake(medicine: dict, intakes: list) -> list:
    """Получить все приёмы для заданного препарата и проверить целостность связи."""
    medicine_id = medicine.get("id")
    if medicine_id is None:
        raise ValueError("Препарат должен содержать уникальный идентификатор")

    matched_intakes = []
    for intake in intakes:
        intake_medicine_id = intake.get("medicine_id")
        if intake_medicine_id == medicine_id:
            matched_intakes.append(integrity_check(medicine, intake))

    return matched_intakes


def integrity_check(medicine: dict, intake: dict) -> dict:
    """Проверить целостность связи между препаратом и приёмом."""
    if not isinstance(medicine, dict):
        raise TypeError("Препарат должен быть словарём")
    if not isinstance(intake, dict):
        raise TypeError("Приём должен быть словарём")

    if medicine.get("id") is None:
        raise ValueError("Препарат не имеет идентификатора")
    if intake.get("medicine_id") is None:
        raise ValueError("Приём не имеет идентификатора препарата")

    if medicine.get("id") != intake.get("medicine_id"):
        raise ValueError("Несоответствие идентификаторов препарата и приёма")

    return {
        "id": intake.get("id"),
        "medicine_id": intake.get("medicine_id"),
        "medicine_name": medicine.get("name"),
        "dosage": intake.get("dosage"),
        "taken_at": intake.get("taken_at"),
        "integrity": True,
    }


if __name__ == "__main__":
    sample_medicine = {
        "id": 1,
        "name": "Аспирин",
        "form": "таблетки",
        "quantity": 10,
        "expiry": "2026-12-31",
    }
    sample_intakes = [
        {"id": 101, "medicine_id": 1, "dosage": "100 мг", "taken_at": "2025-01-01"},
        {"id": 102, "medicine_id": 1, "dosage": "200 мг", "taken_at": "2025-01-02"},
        {"id": 103, "medicine_id": 2, "dosage": "500 мг", "taken_at": "2025-01-03"},
    ]
    result = get_medicine_intake(sample_medicine, sample_intakes)
    for item in result:
        print(item)
