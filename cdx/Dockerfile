FROM python:3.8

RUN apt update
RUN apt install -y libpython3-dev \
    python3-lxml\
    libzbar0

ADD ./requirements.txt /srv/www/cdx/requirements.txt

WORKDIR srv/www/cdx
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


ENTRYPOINT ["./entrypoint.sh"]
