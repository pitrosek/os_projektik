FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . /app

RUN addgroup --system app && adduser --system --ingroup app app

RUN chmod +x /app/docker-entrypoint.sh

USER app

EXPOSE 8000

ENV FLASK_APP=main.py
ENV FLASK_ENV=production

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app"]
