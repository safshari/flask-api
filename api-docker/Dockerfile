FROM python:3.7.5-slim
RUN apt-get update
RUN apt-get update -y && apt-get upgrade -y && apt-get full-upgrade -y && apt-get auto-remove -y 
RUN apt-get -y install software-properties-common wget
RUN apt-get update && apt-get upgrade -y \
    git \
    libnotify4 libnss3 libxkbfile1 libsecret-1-0 libxss1 \
    tmux \
    vim \
    net-tools \
    iputils-ping \
    htop \
    usbutils \
    python-pip \
    python-pil \ 
    python-rosinstall python-rosinstall-generator python-wstool build-essential

RUN pip install --upgrade pip
RUN apt-get update
RUN  pip install python-magic 
RUN  pip install Flask 
RUN pip install flask_session
RUN pip install opencv-python
RUN apt-get install -y libsm6 libxext6 libxrender-dev
WORKDIR /home
RUN echo "hi 3"
WORKDIR /home
COPY ./xtract /home/xtract
WORKDIR /home/xtract
ENTRYPOINT python ./server.py
# COPY "entrypoint.sh" /
# RUN chmod u+x /entrypoint.sh


