FROM python:3.12-slim

WORKDIR /app

# Установка системных зависимостей для Postgres и других пакетов
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false

# Копирование зависимостей
COPY pyproject.toml poetry.lock* ./

# Установка зависимостей
RUN poetry install --no-root --no-interaction --no-ansi

# Копирование остальных файлов
COPY . .

# Переменные окружения
ENV PYTHONPATH=/app