FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /law
COPY requirements.txt /law/requirements.txt
RUN pip install -r requirements.txt
COPY . /law

CMD python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000