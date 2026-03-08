FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

RUN pip install uv

WORKDIR /app

COPY pyproject.toml .

RUN uv sync

COPY app .

ENTRYPOINT ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

