FROM python:alpine3.17

WORKDIR /app

ADD requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

ADD ./src /app

CMD ["python", "manager.py", "gitlab-api", "--api", "gitlab_events"]