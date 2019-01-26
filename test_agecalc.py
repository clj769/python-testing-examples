from datetime import date

import pytest
import agecalc


def test_calculate():
    assert agecalc.calculate(date(2000, 1, 1), date(2010, 1, 1)) == 10
    assert agecalc.calculate(date(2000, 1, 1), date(2010, 1, 2)) == 10

def test_calculate_different_months_days():
    assert agecalc.calculate(date(2000, 7, 1), date(2010, 6, 30)) == 9

def test_calculate_present_date_equals_birthdate():
    birthdate = date(2000, 1, 1)
    evaldate = date(2000, 1, 1)

    assert agecalc.calculate(birthdate, evaldate) == 0

def test_calculate_present_date_less_than_birthdate_raises_valueerror():
    birthdate = date(2000, 1, 1)
    evaldate = date(1999, 1, 1)

    # exepct ValueError exception
    with pytest.raises(ValueError):
        agecalc.calculate(birthdate, evaldate)
