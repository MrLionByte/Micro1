FROM python:3.10

WORKDIR /api

COPY requirements.txt /api/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /api/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]