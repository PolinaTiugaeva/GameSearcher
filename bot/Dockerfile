FROM python:3.12-slim 

WORKDIR /bot

COPY requirements.txt /bot/

RUN pip install --upgrade pip && pip install -r /bot/requirements.txt

CMD ["python", "run_bot.py"]