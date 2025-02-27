FROM python:3.12-slim 

WORKDIR /search

COPY requirements.txt /search/

RUN pip install --upgrade pip && pip install -r /search/requirements.txt

CMD ["python", "search.py"]