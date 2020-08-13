FROM python:3-alpine

COPY main.py .

WORKDIR /var/www

EXPOSE 80

CMD [ "python", "/main.py" ]