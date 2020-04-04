FROM python:3.6.8
LABEL maintainer='Amom Mendes Luiz'
RUN apt-get update && \
    apt-get install -y \
    python-pip \
    python-dev \
    python-setuptools \
    libpq-dev \
    build-essential \
    autoconf \
    libtool \
    libssl-dev \
    libffi-dev \
    vim \
    jq \
    locales \
    lsof

WORKDIR /app
COPY ./requirements.txt .

RUN python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./app .
RUN chmod 775 /app/start_app.sh
WORKDIR /
ENV FLASK_ENV=development
ENV FLASK_APP=app
ENTRYPOINT /app/start_app.sh


