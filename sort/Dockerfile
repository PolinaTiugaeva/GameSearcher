FROM python:3.12-slim 

WORKDIR /sort

COPY requirements.txt /sort/

RUN pip install --upgrade pip && pip install -r /sort/requirements.txt

CMD ["python", "sort.py"]