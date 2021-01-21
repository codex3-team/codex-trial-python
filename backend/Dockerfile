FROM python:3.8

RUN apt update
RUN apt install -y libpython3-dev \
    zlib1g-dev \
    musl-dev \
    libgdk-pixbuf2.0-dev \
    libgdk-pixbuf2.0 \
    libjpeg-dev \
    libwebp-dev \
    gettext \
    libpq-dev \
    libffi-dev \
    libgdal-dev \
    postgis \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1-mesa-dev \
    libxml2-dev\
    libxslt-dev\
    python3-lxml\
    libzbar0        # for qr-decoding

ADD ./backend/requirements.txt /srv/www/backend/requirements.txt
WORKDIR srv/www/backend
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


ENTRYPOINT ["./entrypoint.sh"]
