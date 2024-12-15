FROM python:3.12

LABEL maintainer="yandexeats"
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /app/requirements.txt

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /app/requirements.txt && \
    adduser --disabled-password --gecos '' django_user && \
    chown -R django_user /app

COPY . /app
WORKDIR /app

USER django_user
ENV PATH="/venv/bin:$PATH"

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
