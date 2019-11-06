FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /mycontacts
WORKDIR /mycontacts
COPY requirements.txt /mycontacts/
RUN pip install -r requirements.txt
COPY . /mycontacts/
