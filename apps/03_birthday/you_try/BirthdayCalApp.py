import datetime


def print_header():
    print('--------------------------------')
    print('    BIRTHDAY APP')
    print('--------------------------------')
    print()
    return


def get_birthday_from_user():
    year = int(input('What year were you born? [YYYY]'))
    month = int(input('What month were you born? [MM]'))
    day = int(input('What day were you born? [DD]'))
    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_days_between_dates(now, birthday):
    date_this_year = datetime.datetime(now.year, birthday.month, birthday.day)
    date1 = datetime.datetime(now.year, now.month, now.day)
    delta = date_this_year - date1
    return delta


def print_birthday_information(days):
    if days < 0:
        print('Your Birthday was {} days ago' .format(-days))
    elif days > 0:
        print('Your Birthday will be in {} days' .format(days))
    else:
        print('Happy Birthday')
    pass


def main():
    print_header()
    birthday = get_birthday_from_user()
    now = datetime.datetime.now()
    dt = compute_days_between_dates(now, birthday)
    print_birthday_information(dt.days)
    return


main()


