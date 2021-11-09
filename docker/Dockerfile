FROM python:3.10-buster

USER root
WORKDIR /root/
COPY ./ ./

RUN pip3 install -U -r requirements.txt

ENTRYPOINT ["/root/docker/docker_entry.sh"]

CMD ["/bin/bash"]
