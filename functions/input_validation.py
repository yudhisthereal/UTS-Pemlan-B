def is_valid_int(value):
    try:
        x = int(value)
        return True
    except ValueError:
        return False

def is_valid_float(value):
    try:
        x = float(value)
        return True
    except ValueError:
        return False