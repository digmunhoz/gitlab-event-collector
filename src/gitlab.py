import requests
import logging
from settings import Settings


logging.basicConfig(level=logging.INFO)


class Gitlab:

    def get_users(self, max_users):

        endpoint = "/api/v4/users"
        query_string = {
            "active": "true",
            "without_project_bots": "true",
            "active": "true"
        }

        max_page = int(max_users) / 100 if max_users else None

        logging.info(f"Getting users with query string: {query_string}")
        gitlab_users = self.get_data(endpoint, max_page=max_page, **query_string)

        return gitlab_users

    def get_data(self, endpoint, max_page=None, **query_string):
        headers = {"PRIVATE-TOKEN": f"{Settings.GITLAB_API_TOKEN}",
                   "Accept": "application/json"}

        response = []

        page = 1
        while page:
            if page == max_page:
                break

            query_string.update({"per_page": 100, "page": page})

            try:
                logging.info(f"Getting data from endpoint {endpoint} on page {page}")
                parcial_response = requests.get(
                    f"{Settings.GITLAB_API_URL}{endpoint}",
                    params=query_string,
                    headers=headers,
                    timeout=10
                ).json()
            except Exception as e:
                raise (e)

            if parcial_response:
                page = page + 1
                for item in parcial_response:
                    response.append(item)
            else:
                page = None

        return response
