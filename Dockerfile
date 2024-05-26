FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE $PORT
ENV PORT=8000
CMD ["gunicorn", "--workers=2", "--timeout=60", "--bind=0.0.0.0:$PORT", "app:app"]
