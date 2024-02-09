import os
from prettyconf import config
from datetime import datetime

def date_format(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except Exception as e:
        raise (e)
    return value

class Settings:
    ELASTICSEARCH_ADDRESS = config("ELASTICSEARCH_ADDRESS", default="http://elasticsearch:9200")
    ELASTICSEARCH_GITLAB_INDEX_PREFIX = config("ELASTICSEARCH_GITLAB_INDEX_PREFIX", default="gitlab_")
    GITLAB_API_URL = config("GITLAB_API_URL")
    GITLAB_API_TOKEN = config("GITLAB_API_TOKEN")
    MAX_USERS = config("MAX_USERS", default=0)

    if os.getenv("TIME_WINDOW_START_DATE"):
        TIME_WINDOW_START_DATE = config("TIME_WINDOW_START_DATE", cast=date_format)
    else:
        TIME_WINDOW_START_DATE = None

    if os.getenv("TIME_WINDOW_END_DATE"):
        TIME_WINDOW_END_DATE = config("TIME_WINDOW_END_DATE", cast=date_format)
    else:
        TIME_WINDOW_END_DATE = None
