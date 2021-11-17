"""
Functions to calculate amount of weeks.
"""

from datetime import datetime


def amount_of_weeks(init: datetime, end: datetime) -> int:
    """
    Amount of weeks of simulation.

    Use week number of the year, with sunday as the first day of the week
    as a zero padded decimal number.

    Args:
        init (datetime): Initial date.
        end (datetime): End date.

    Raises:
        ValueError: Works for dates in the same year.

    Returns:
        int: Amount of weeks for the period between
                initial and end date included.
    """
    if init.year != end.year:
        raise ValueError(
            f"Different years for initial {init.date}"
            f" and end {end.date} date."
        )

    # Week number of the year
    week_init = int(init.strftime("%U"))
    week_end = int(end.strftime("%U"))

    weeks = week_end - week_init + 1

    return weeks
