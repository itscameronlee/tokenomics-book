FROM python:3.10.11-bullseye

# #Install Calibre
RUN apt update
RUN apt install tar wget xdg-utils xz-utils libegl1 libopengl0 -y
RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin version=6.1.0

# Install Python requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt
