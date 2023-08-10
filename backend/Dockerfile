FROM python:3.9

WORKDIR /app

COPY pyproject.toml README.md ./

RUN python3 -m pip install .

CMD ["python3", "-u", "-m", "flask", "--app", "mta_flask", "run", "--port", "5000", "--host", "0.0.0.0", "--debug"]