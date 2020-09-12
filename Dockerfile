FROM tiangolo/uwsgi-nginx-flask:python:alpine3.6.9
RUN apk --update add bash nano
ENV app /static
ENV app /static
RUN pip install -r requirement.txt  