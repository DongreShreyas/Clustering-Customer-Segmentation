<<<<<<< HEAD
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
=======
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
>>>>>>> e929eb443c02a4807f44db3344206250e8973ff2
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app