FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends gettext \
    && rm -rf /var/lib/apt/lists/*


EXPOSE 8000
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

COPY project/ /app/

#ENTRYPOINT ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

