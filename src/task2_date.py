import datetime


def get_days_between_dates(date1: str, date2: str):
    """ Функция вычесляет разницу между датами в днях"""
    try:
        date1_dt = datetime.datetime.strptime(date1, "%d.%m.%Y")
        date2_dt = datetime.datetime.strptime(date2, "%d.%m.%Y")
        return (date2_dt - date1_dt).days
    except ValueError:
        return "Неверный формат даты"


if __name__ == "__main__":
    print(get_days_between_dates("01.01.2022", "20.01.2022"))
