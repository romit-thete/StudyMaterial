import argparse
import sys
from datetime import date
from datetime import timedelta

day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def _next_date(some_date):
    date_today = date.fromisoformat(some_date)
    day_today = day_list[date_today.weekday()]
    if day_today in day_list[3:]:
        next_date = date_today + timedelta(7 - date_today.weekday())
        return date.isoformat(next_date), date.isoformat(date_today)
    return date.isoformat(date_today + timedelta(1)), date.isoformat(date_today)


def tiffin_next_date(next_start_date, given_delta):
    for i in range(int(given_delta)):
        next_date, date_today = _next_date(next_start_date)
        next_start_date = next_date
    return date_today, next_start_date


def CustomParser():
    # Custom parser to parse command line arguments using argparse package.
    # Three steps:
    ## 1. Initialize the parser
    ## 2. Add custom arguments
    ## 3. Parse the arguments
    parser = argparse.ArgumentParser(
        prog="tiffinDates.py",
        description="Get the last date and next start date (also the pay date) of Tiffin service",
        epilog="Thanks for using! Developed by Romit!"
    )

    # 2. Adding arguments
    # kwargs used:
    ## metavar - Optional name to be displayed in -h
    ## help - Help message to be displayed in -h
    ## default - Can use to set default values (not used here)
    parser.add_argument('-sd', '--start-date', metavar="", help="Start date of the current month")
    parser.add_argument('-d', '--delta', metavar="", help="Difference in start and end date (in days)")

    # 3. Parsing the args
    args = parser.parse_args()
    return args.start_date, args.delta


if __name__ == "__main__":
    start_date, delta = CustomParser()
    if start_date is None:
        start_date = input("Enter start date (YYYY-MM-DD): ")
    if delta is None:
        delta = input("Enter the difference: ")
    print("Start date for this month: {}".format(start_date))
    end_date, pay_date = tiffin_next_date(start_date, delta)
    print("Day: {}: {}".format(delta, end_date))
    print("Next date for payment: {}".format(pay_date))
