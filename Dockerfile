FROM python:3.11-alpine
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .


EXPOSE 8000

RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]