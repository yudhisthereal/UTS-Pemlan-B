def float_input(message):
    input_is_valid = False
    result = ''
    while not input_is_valid:
        try:
            result = float(input(message).strip())
        except ValueError:
            print('input must be a real number (e.g. 123.4567)')
        else:
            input_is_valid = True
    
    return str(result)


def int_input(message):
    input_is_valid = False
    result = ''
    while not input_is_valid:
        try:
            result = int(input(message).strip())
        except ValueError:
            print('your input must be a number')
        else:
            input_is_valid = True
    
    return str(result)


def yesno_input(message):
    input_is_valid = False
    result = ''
    while not input_is_valid:
        result = input(message).strip()

        if result in ('y', 'n'):
            input_is_valid = True
        else:
            print("input must be either 'y' or 'n'.")
    
    return result