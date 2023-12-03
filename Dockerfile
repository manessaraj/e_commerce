FROM python:3.11
WORKDIR /usr/src/server

COPY . /usr/src/server

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
