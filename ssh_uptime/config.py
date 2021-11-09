class email:
    def __init__(self, email_dict):
        self.smtp_server = email_dict['smtp_server']
        self.from_addr = email_dict['from_addr']
        self.password = email_dict['password']
        self.from_user = email_dict['from_user']


class machine:
    def __init__(self, machine_dict):
        self.hostname = machine_dict['hostname']
        self.host = machine_dict['host']
        self.port = machine_dict['port']
        self.user = machine_dict['user']
        self.password = machine_dict['password']


class people:
    def __init__(self, people_dict):
        self.user = people_dict['user']
        self.email = people_dict['email']


class config:
    def __init__(self, config_dict):
        self.email = email(config_dict['email'])
        self.machine_list = list(
            map(lambda x: machine(x), config_dict['machine']))
        self.people_list = list(
            map(lambda x: people(x), config_dict['people']))
