FROM rcarmo/ubuntu-python:3.7-onbuild-amd64
COPY . /tmp
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install -y tzdata
RUN ["chmod", "+x", "/tmp/entrypoint.sh"]
WORKDIR /app
CMD python ./app.py
