import calendar

def print_calendar (year):
    for month in range(1, 13):
        print(calendar.month(year, month))


if __name__ == "__main__":
    print_calendar(2023)
