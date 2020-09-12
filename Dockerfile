
FROM python:alpine3.7 
COPY . /app
WORKDIR /appD

EXPOSE 5001 
ENTRYPOINT [ "python3" ] 
CMD [ "app.py" ] 
