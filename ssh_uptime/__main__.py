from ssh_uptime import default_config, logger
from .utils import get_time
from .ssh_test import ping_test, Status
from time import sleep
from . import db
from .mail import warning_report

if __name__ == '__main__':
    machines_status = db.get()

    while True:
        logger.info("Ping Test New Round")

        for machine in default_config.machine_list:
            status, msg = ping_test(
                machine.host, machine.user, machine.password, machine.port)

            if not machine.hostname in machines_status.keys():
                machine_status = machines_status[machine.hostname] = db.get_new_machine(
                    machine.hostname)
            else:
                machine_status = machines_status[machine.hostname]

            logger.info(
                'Ping Test - Hostname:{}, Status:{}, Msg:{}'.format(machine.hostname, status, msg))

            if status == Status.SUCCESS:
                machine_status.is_survival = True
                machine_status.last_survival_time = get_time()

            if status == Status.FAILURE:
                if machine_status.is_survival:
                    warning_report(machines_status[machine.hostname])

                machine_status.is_survival = False

        db.put(machines_status)

        sleep(30)
