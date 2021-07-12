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


def MonthCycle_algo(date):
    if is_menstruation == True:
        menstruation_phase = date + datetime.timedelta(days=5)
        follicular_phase = menstruation_phase + datetime.timedelta(days=8)
        ovalution_phase = follicular_phase + datetime.timedelta(days=3)
        lutreal_phase = ovalution_phase + datetime.timedelta(days=12)
    elif is_follicular == True:
        follicular_phase = date + datetime.timedelta(days=8)
        ovalution_phase = follicular_phase + datetime.timedelta(days=3)
        lutreal_phase = ovalution_phase + datetime.timedelta(days=12)
        menstruation_phase = lutreal_phase + datetime.timedelta(days=5)
    elif is_ovulation == True:
        ovalution_phase = date + datetime.timedelta(days=3)
        lutreal_phase = ovalution_phase + datetime.timedelta(days=12)
        menstruation_phase = lutreal_phase + datetime.timedelta(days=5)
        follicular_phase = menstruation_phase + datetime.timedelta(days=8)

    pass