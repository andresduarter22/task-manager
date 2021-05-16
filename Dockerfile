# syntax=docker/dockerfile:1
FROM python:3.8-alpine
WORKDIR .
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
