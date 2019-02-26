FROM rcarmo/ubuntu-python:3.7-onbuild-amd64
COPY . /tmp
WORKDIR /tmp
ENTRYPOINT ["tail", "-f", "/dev/null"]
