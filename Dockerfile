FROM python:3.6
MAINTAINER Wilhelm van der walt "1@1.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["volunteer_dashboard_api/app.py"]