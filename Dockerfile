# Distroless image 

FROM python:3.11-slim AS base

WORKDIR /app

COPY pyproject.toml pyproject.toml

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN pip3 install poetry
RUN poetry config virtualenvs.create true \
    && poetry config virtualenvs.in-project true \
    && poetry install --no-dev

COPY . /app/
RUN chmod +x /app/.venv/bin/activate
RUN chmod +x /app/entrypoint.sh

FROM gcr.io/distroless/python3-debian12@sha256:d1427d962660c43d476b11f9bb7d6df66001296bba9577e39b33d2e8897614cd as production

ENV PYTHONPATH=/app/.venv/lib/python3.11/site-packages
ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app

COPY --from=base /app /app 
COPY entrypoint.sh /app/entrypoint.sh
COPY --from=busybox:stable-uclibc /bin/sh /bin/sh

ENTRYPOINT ["sh"]
CMD ["/app/entrypoint.sh"]