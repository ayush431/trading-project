import time
from datetime import datetime


def get_current_time():
    return time.time()


def format_date(input_date_str):
    input_date = datetime.strptime(input_date_str, "%Y%m%d")
    formatted_date_str = input_date.strftime("%Y-%m-%d")
    return formatted_date_str
