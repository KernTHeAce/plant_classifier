FROM python:3.11
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends gdal-bin=3.6.*

WORKDIR /app

ADD . /app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
