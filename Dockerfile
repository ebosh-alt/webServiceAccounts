FROM python:3.12
ENV TZ=Europe/Moscow
ENV PYTHONUNBUFFERED=1
EXPOSE 443
COPY . /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Копирование SSL-сертификатов
COPY server.crt /etc/ssl/certs/
COPY server.key /etc/ssl/private/


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "443", "--ssl-keyfile", "/etc/ssl/private/server.key", "--ssl-certfile", "/etc/ssl/certs/server.crt"]

