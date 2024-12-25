FROM python:3.12
ENV TZ=Europe/Moscow
ENV PYTHONUNBUFFERED=1
WORKDIR /
EXPOSE 8000
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

