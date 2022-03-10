FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 4000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]