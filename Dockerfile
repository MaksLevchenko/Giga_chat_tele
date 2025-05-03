FROM python:3.11-alpine3.18

COPY requirements.txt /temp/requirements.txt

COPY .env /.env

COPY . .

# ADD /giga_bot/bot.py .

# WORKDIR .

RUN pip install -r /temp/requirements.txt
