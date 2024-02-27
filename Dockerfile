# Distroless image 

FROM python:3.11-slim AS base

WORKDIR /app

COPY pyproject.toml pyproject.toml

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# Set environment variable for Poetry to create a virtual environment on app folder
ENV POETRY_VIRTUALENVS_IN_PROJECT=true 

RUN pip3 install poetry
RUN poetry config virtualenvs.create true \
    && poetry config virtualenvs.in-project true \
    && poetry install --no-dev

COPY . /app/

FROM gcr.io/distroless/python3-debian12@sha256:d1427d962660c43d476b11f9bb7d6df66001296bba9577e39b33d2e8897614cd as production

WORKDIR /app

COPY --from=base /app /app 

ENV PYTHONPATH=/app/.venv/lib/python3.11/site-packages

CMD ["/app/.venv/bin/gunicorn", "careers.wsgi", "-b", "0.0.0.0"]