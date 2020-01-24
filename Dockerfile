FROM python:3.6
ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app"]