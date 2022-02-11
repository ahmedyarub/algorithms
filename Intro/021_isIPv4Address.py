def solution(inputString):
    fields = inputString.split('.')
    if len(fields) != 4:
        return False

    for field in fields:
        if not field.isnumeric() or int(field) < 0 or int(field) > 255 or str(int(field)) != field:
            return False

    return True
