FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

ADD requirements.pip /tmp/requirements.pip
WORKDIR /tmp

RUN pip install --upgrade pip && pip install -r requirements.pip --trusted-host pypi.python.org

ADD . /code/

WORKDIR /code/webapp

EXPOSE 8000

RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]