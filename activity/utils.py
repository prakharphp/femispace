from datetime import datetime
import datetime as dt

from activity.models import EatRainbowActivity
from master.models import EatRainbowMaster


def get_previous_date(date_str):
    """

    :param date_str: date in yyyy-mm-dd formate
    :return:  date in yyyy-mm-dd formate
    """
    date_object = datetime.strptime(date_str, "%Y-%m-%d")
    day = dt.timedelta(days=1)
    reduce_date = date_object - day
    return reduce_date.strftime("%Y-%m-%d")


def get_difference_from_current_date(date_str):
    date_object = datetime.strptime(date_str, "%Y-%m-%d")
    date = datetime.now() - date_object
    return date.days


def user_first_login(user, eat_date):
    """

    this methods takes user and date object
    return eat_activity object matched with master first sequence

    """
    master = EatRainbowMaster.objects.get(sequence=1)
    eat_rainbow_object = EatRainbowActivity.objects.create(user=user, date=eat_date, master=master,
                                                               red_serving=master.red_serving,
                                                               cream_serving=master.cream_serving,
                                                               yellow_serving=master.yellow_serving,
                                                               kiwi_serving=master.kiwi_serving,
                                                               blue_serving=master.blue_serving,
                                                               green_serving=master.green_serving)
    eat_rainbow_object.enjoy_regular.set(master.enjoy_regular.all(), clear=True)
    eat_rainbow_object.eat_more.set(master.eat_more.all(), clear=True)
    eat_rainbow_object.eat_less.set(master.eat_less.all(), clear=True)
    eat_rainbow_object.eat_avoid.set(master.eat_avoid.all(), clear=True)
    eat_rainbow_object.tag.set(master.tag.all(), clear=True)
    eat_rainbow_object.save()
    return eat_rainbow_object
