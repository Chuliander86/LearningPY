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
    delta = datetime.timedelta(now, birthday)
    return delta


def print_birthday_information():
    pass


def main():
    print_header()
    birthday = get_birthday_from_user()
    print(birthday)
    print(type(birthday))
    return


main()


