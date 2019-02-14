FROM rcarmo/ubuntu-python:3.7-onbuild-amd64
COPY . /videoplayer
WORKDIR /videoplayer
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update ;\
    apt-get install -y tzdata
RUN apt-get install -y vlc
CMD python ./videoScheduler.py
