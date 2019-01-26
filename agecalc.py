from datetime import date


def calculate(birthdate: date, evaldate: date) -> int:
    '''Returns age given birthdate and evaldate

    Raises:
        ValueError: if evaldate < birthdate
    '''
    if evaldate < birthdate:
        raise ValueError('evaldate must be greater than or equal to birthdate')

    age = evaldate.year - birthdate.year
    if (evaldate.month, evaldate.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age
