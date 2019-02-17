FROM rcarmo/ubuntu-python:3.7-onbuild-amd64
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install -y tzdata
RUN apt-get install -y vlc
RUN apt-get install -y pulseaudio socat
RUN apt-get install -y alsa-utils
RUN pulseaudio -D --exit-idle-time=-1
RUN pulseaudio -D --exit-idle-time=-1
RUN pacmd load-module module-virtual-sink sink_name=v1
RUN pacmd set-default-sink v1
RUN pacmd set-default-source v1.monitor
EXPOSE 4444
EXPOSE 5000
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
