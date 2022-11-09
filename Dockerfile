FROM python:3.10-slim-bullseye
EXPOSE 80
EXPOSE 443

WORKDIR /app
COPY . .

RUN pip install pipenv
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system

ENTRYPOINT python server.py
