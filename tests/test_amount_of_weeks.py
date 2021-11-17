"""
Tests for amount of weeks in a period between initial and end date included.
"""

import pytest
from datetime import datetime
from weeks.amount_of_weeks import amount_of_weeks


def test_amount_one_week_same_date():
    weeks = 1

    init = datetime(year=2021, month=10, day=1)
    end = datetime(year=2021, month=10, day=1)

    result = amount_of_weeks(init=init, end=end)

    assert result == weeks


def test_amount_two_weeks():
    weeks = 2

    # Week starts on sunday
    init = datetime(year=2021, month=10, day=1)
    end = datetime(year=2021, month=10, day=3)

    result = amount_of_weeks(init=init, end=end)

    assert result == weeks


def test_amount_third_weeks():
    weeks = 3

    init = datetime(year=2021, month=10, day=1)
    end = datetime(year=2021, month=10, day=10)

    result = amount_of_weeks(init=init, end=end)

    assert result == weeks


def test_amount_six_weeks():
    weeks = 6

    init = datetime(year=2021, month=10, day=1)
    end = datetime(year=2021, month=10, day=31)

    result = amount_of_weeks(init=init, end=end)

    assert result == weeks


def test_amount_different_years_raise_value_error():
    init = datetime(year=2021, month=10, day=1)
    end = datetime(year=2022, month=10, day=1)

    message = (
        f"Different years for initial {init.date}"
        f" and end {end.date} date."
    )

    with pytest.raises(ValueError) as info:
        amount_of_weeks(init=init, end=end)

    assert str(info.value) == message
