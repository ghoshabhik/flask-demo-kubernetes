FROM python:3.8-alpine
LABEL maintainer="Abhik Ghosh, avik5324@gmail.com"
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]