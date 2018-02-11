FROM python:3.6
MAINTAINER Wilhelm van der walt "1@1.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]