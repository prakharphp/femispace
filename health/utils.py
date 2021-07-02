import datetime


def get_all_dates_in_month(year, month):
    """
    1--> take string as a parameter
    2--> return list of date in the month

    """
    list_of_dates = []
    day_delta = datetime.timedelta(days=1)
    start_date = datetime.date(int(year), int(month), 1)
    end_date = datetime.date(int(year), int(month) + 1, 1)
    for i in range((end_date - start_date).days):
        current_date = start_date + i * day_delta
        x = current_date.strftime("%Y-%m-%d")
        list_of_dates.append(x)
    return list_of_dates
