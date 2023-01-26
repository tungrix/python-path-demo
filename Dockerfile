FROM python:3.9
MAINTAINER Tung "tungtung2825@gmail.com"

WORKDIR /code

COPY . .
CMD ["python", "-m", "main"]