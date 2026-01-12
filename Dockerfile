FROM python:3.11-slim

LABEL maintainer="hello@marvinkweyu.net"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=masomo.config.prod

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    netcat-openbsd \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput --settings=masomo.config.prod || true

RUN chmod +x /app/entrypoint.sh

# Create non-root user
RUN useradd -m -u 1000 masomo && \
    chown -R masomo:masomo /app
USER masomo

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
