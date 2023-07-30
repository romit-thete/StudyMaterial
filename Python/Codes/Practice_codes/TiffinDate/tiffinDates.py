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


if __name__ == "__main__":
    if len(sys.argv) == 1:
        start_date = input("Enter start date (YYYY-MM-DD): ")
        delta = input("Enter the difference: ")
    else:
        start_date = sys.argv[1]
        delta = sys.argv[2]

    print("Start date for this month: {}".format(start_date))
    end_date, pay_date = tiffin_next_date(start_date, delta)
    print("Day: {}: {}".format(delta, end_date))
    print("Next date for payment: {}".format(pay_date))
