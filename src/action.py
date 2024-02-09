import logging

from datetime import date
from datetime import timedelta

from settings import Settings
from gitlab import Gitlab
from helpers.elasticsearch import CustomElasticsearch


class Action:
    def gitlab_events(self):
        repository = Gitlab()
        database = CustomElasticsearch()
        max_users = Settings.MAX_USERS
        users = repository.get_users(max_users=max_users)

        today = str(date.today())
        yesterday = str(date.today() - timedelta(days=2))

        start_date = (
            Settings.TIME_WINDOW_START_DATE
            if Settings.TIME_WINDOW_START_DATE
            else yesterday
        )

        end_date = (
            Settings.TIME_WINDOW_END_DATE if Settings.TIME_WINDOW_END_DATE else today
        )

        query_string = {
            "after": start_date,
            "before": end_date,
        }

        for user in users:
            logging.info(
                f"Getting data from user: {user.get('id')} - {user.get('username')}"
            )
            user_id = user.get("id")

            logging.info(f"Looking for event using query string: {query_string}")
            events = repository.get_data(
                f"/api/v4/users/{user_id}/events", **query_string
            )

            if events:
                database.insert_data(
                    events, Settings.ELASTICSEARCH_GITLAB_INDEX_PREFIX, "users_events"
                )
            else:
                logging.info("There is no events for this user")
