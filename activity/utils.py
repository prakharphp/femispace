from datetime import datetime
import datetime as dt


def get_previous_date(date_str):
    """

    :param date_str: date in yyyy-mm-dd formate
    :return:  date in yyyy-mm-dd formate
    """
    date_object = datetime.strptime(date_str, "%Y-%m-%d")
    day = dt.timedelta(days=1)
    reduce_date = date_object - day
    return reduce_date.strftime("%Y-%m-%d")
