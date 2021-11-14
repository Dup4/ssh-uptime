import paramiko
from enum import Enum


class Status(Enum):
    FAILURE = 1
    SUCCESS = 2


class SSHAgent:
    def __init__(self, ip, username, password, port=22):
        self.ip = ip
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.ip, port=port,
                         username=self.username, password=self.password, banner_timeout=200)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ssh.close()

    def remote_command(self, command: str) -> tuple[Status, str]:
        stdin, stdout, stderr = self.ssh.exec_command(command)

        error = stderr.read().decode('utf-8')
        if error:
            return Status.FAILURE, error
        else:
            return Status.SUCCESS, stdout.read().decode('utf-8')


def ping_test(ip: str, username: str, password: str, port: int = 22) -> tuple[Status, str]:
    try:
        with SSHAgent(ip, username, password, port) as ssh_agent:
            return ssh_agent.remote_command('echo -n ping')
    except Exception as e:
        return Status.FAILURE, e
