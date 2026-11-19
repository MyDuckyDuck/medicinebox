# === Stage 8: Текстовый поиск ===
# Project: MedicineBox
def highlight_text(text, matches):
    """Подсвечивает в строке совпадения с учётом регистра."""
    if not text or not matches:
        return text
    result = list(text)
    for match in matches:
        if not match:
            continue
        start, end = text.find(match), 0
        while start != -1:
            for i in range(start, end(start, end)):
                result[i] = '*'
            start = text.find(match, start + 1)
    return ''.join(result)


def find_in_fields(item, keywords):
    """Ищет препараты по текстовым полям без учёта регистра."""
    text = ' '.join(
        field for field in (
            item.get('name'),
            item.get('form'),
        ) if field
    ).lower()
    lowered = [kw.lower() for kw in keywords]
    return [kw for kw in lowered if kw and kw in text]


def search_medicine(items, keywords):
    """Возвращает пары (название, подсвеченная строка) для совпадений."""
    matched = []
    for item in items:
        found = find_in_fields(item, keywords)
        if found:
            name = item.get('name') or ''
            highlighted = highlight_text(name, found)
            matched.append((name, highlighted))
    return matched
