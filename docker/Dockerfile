FROM python:buster AS build

USER root
WORKDIR /root/
COPY ./ ./

RUN pip install -U -r requirements.txt

FROM python:slim-buster

COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=build /root /root

WORKDIR /root/

ENTRYPOINT ["/root/docker/docker_entry.sh"]

CMD ["/bin/sh"]
