FROM python:3.10

ADD main.py .
ADD valueSheet.py .
ADD portfolioSheet.py .
ADD evalSheet.py .
ADD credentials.json .

RUN pip install requests
RUN pip install pygsheets
RUN pip install pycoingecko

CMD ["python", "./main.py"]

