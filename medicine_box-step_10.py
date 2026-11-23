# === Stage 10: Постраничный вывод ===
# Project: MedicineBox
page = 1
page_size = 10


def paginate(items, page=1, page_size=10):
    start = (page - 1) * page_size
    end = start + page_size
    return items[start:end]


def apply_pagination(items, page=1, page_size=10):
    if page < 1:
        page = 1
    if page_size < 1:
        page_size = 1
    if page_size < len(items):
        total_pages = (len(items) + page_size - 1) // page_size
        if page > total_pages:
            page = total_pages
    return page, page_size, paginate(items, page, page_size)
