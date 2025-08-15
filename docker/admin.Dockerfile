FROM python:3.13-slim

WORKDIR /src


COPY pyproject.toml ./

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY ./src/ ./

CMD ["python", "-m", "admin.app"]
