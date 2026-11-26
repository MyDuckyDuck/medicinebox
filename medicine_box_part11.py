# === Stage 11: Быстрые фильтры ===
# Project: MedicineBox
from __future__ import annotations

from datetime import date, timedelta

# Периодичность фильтров задаётся в днях относительно текущей даты.
TODAY_OFFSET = 0
THIS_WEEK_OFFSET = 7

# Порог "просрочено": препарат считается просроченным, если срок годности
# наступил ранее даты расчёта (с небольшим запасом в дни).
EXPIRED_MARGIN = 1


def _parse_due_date(value: object) -> date | None:
    """Преобразуем строку срока годности в объект date или None."""
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value.strip())
        except ValueError:
            return None
    return None


def filter_by_due_date(records, due_date: object) -> list:
    """Возвращает препараты, срок годности которых совпадает с due_date."""
    target = _parse_due_date(due_date)
    if target is None:
        return []
    return [
        record
        for record in records
        if _parse_due_date(record.get("due_date")) == target
    ]


def is_expired(record: dict, reference: date | None = None) -> bool:
    """Определяем, просрочен ли препарат относительно reference (сегодня)."""
    due = _parse_due_date(record.get("due_date"))
    if due is None:
        return False
    return due <= (reference or date.today()) - timedelta(days=EXPIRED_MARGIN)


def filter_today(records, reference: date | None = None) -> list:
    """Препараты с сроком годности ровно сегодня."""
    return filter_by_due_date(records, reference or date.today())


def filter_this_week(records, reference: date | None = None) -> list:
    """Препараты, срок годности которых наступает на этой неделе."""
    start = reference or date.today()
    end = start + timedelta(days=THIS_WEEK_OFFSET)
    return filter_by_due_date(records, (start, end))


def filter_expired(records, reference: date | None = None) -> list:
    """Препараты, срок годности которых уже наступил."""
    ref = reference or date.today()
    return [record for record in records if is_expired(record, ref)]


def filter_due_date_range(records, start: object, end: object) -> list:
    """Возвращает препараты со сроком годности в диапазоне [start, end]."""
    start_date = _parse_due_date(start)
    end_date = _parse_due_date(end)
    result = []
    for record in records:
        due = _parse_due_date(record.get("due_date"))
        if due is not None and start_date <= due <= end_date:
            result.append(record)
    return result
