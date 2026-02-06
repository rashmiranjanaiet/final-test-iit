FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

# Install build dependencies for common Python packages, then clean up.
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-prod.txt requirements.txt ./
RUN python -m pip install --upgrade pip \
    && if [ -f requirements-prod.txt ]; then pip install -r requirements-prod.txt; else pip install -r requirements.txt; fi

COPY . .

EXPOSE 8080

CMD ["gunicorn", "--workers=4", "--worker-class=sync", "--bind=0.0.0.0:8080", "wsgi:app"]
