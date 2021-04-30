# syntax=docker/dockerfile:1
FROM python:3.9-alpine
WORKDIR /task_manager
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
