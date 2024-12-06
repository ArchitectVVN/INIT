# library_manager/utils/data_validation.py

def validate_book_data(data: dict) -> bool:
    required_fields = ["title", "author", "genre"]
    if not isinstance(data, dict):
        return False
    for field in required_fields:
        if field not in data or not data[field]:
            return False
    return True
