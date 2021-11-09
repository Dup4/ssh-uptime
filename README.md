# ssh-uptime

## Install Deps

```bash
pip3 install -U -r requirements.txt
```

## Use Docker

### Build

```bash
docker build -t ssh-uptime:latest -f ./docker/Dockerfile .
```

### Start Container

```bash
docker run \
    -d \
    --restart=always \
    --name=ssh-uptime \
    -v ${PWD}/config.yaml:/root/config.yaml \
    ssh-uptime:latest
```
