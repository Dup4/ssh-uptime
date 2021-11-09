import json
import os
from typing import Dict

db_file = './db.json'


class machine_status:
    FIELD_HOSTNAME = 'hostname'
    FIELD_IS_SURVIVAL = 'is_survival'
    FIELD_LAST_SURVIVAL_TIME = 'last_survival_time'

    def __init__(self, machine_dict: Dict):
        self.hostname = machine_dict[self.FIELD_HOSTNAME]
        self.is_survival = machine_dict[self.FIELD_IS_SURVIVAL]
        self.last_survival_time = machine_dict[self.FIELD_LAST_SURVIVAL_TIME]


def get_new_machine(hostname: str) -> machine_status:
    return machine_status({
        machine_status.FIELD_HOSTNAME: hostname,
        machine_status.FIELD_IS_SURVIVAL: True,
        machine_status.FIELD_LAST_SURVIVAL_TIME: None,
    })


def dict2machines(machines_dict: Dict) -> Dict[str, machine_status]:
    machines = dict()

    for key in machines_dict:
        machines[key] = machine_status(machines_dict[key])

    return machines


def get() -> Dict[str, machine_status]:
    if not os.path.exists(db_file):
        put({})

    with open(db_file, 'r') as f:
        text = f.read()
        if len(text) == 0:
            text = '{}'

        return dict2machines(json.loads(text))


def put(data: Dict) -> None:
    with open(db_file, 'w') as f:
        f.write(json.dumps(data, sort_keys=False,
                separators=(',', ':'), ensure_ascii=False, default=lambda obj: obj.__dict__))
