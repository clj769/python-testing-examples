from datetime import date

import pytest
import agecalc


def test_calculate_exact_month_day():
    birthdate = date(2000, 1, 1)
    evaldate = date(2010, 1, 1)
    assert agecalc.calculate(birthdate, evaldate) == 10

def test_calculate_greater_month_day():
    birthdate = date(2000, 1, 1)
    evaldate = date(2010, 2, 1)
    assert agecalc.calculate(birthdate, evaldate) == 10

def test_calculate_smaller_month_day():
    birthdate = date(2000, 1, 2)
    evaldate = date(2010, 1, 1)
    assert agecalc.calculate(birthdate, evaldate) == 9

def test_calculate_present_date_less_than_birthdate_raises_valueerror():
    birthdate = date(2000, 1, 1)
    evaldate = date(1999, 1, 1)

    # exepct ValueError exception
    with pytest.raises(ValueError):
        agecalc.calculate(birthdate, evaldate)
