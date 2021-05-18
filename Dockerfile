# syntax=docker/dockerfile:1
FROM python:3.9-alpine
WORKDIR .
ENV FLASK_APP=task_manager/app.py
ENV FLASK_ENV=development
ENV PYTHONPATH="."
#RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
