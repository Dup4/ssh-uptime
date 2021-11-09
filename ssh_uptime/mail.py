from ssh_uptime import default_config, logger
from .db import machine_status


def get_warning_text(user: str, hostname: str, last_survival_time: str) -> tuple[str, str, str]:
    Subject = '[Warning] Your service is down'

    Text = '''
<html><body>

hello, {}: <br/><br/>

Your service is down, please pay attention.

<ul>
<li>Hostname: {}</li>
<li>Last survival time: {}</li>
</ul>

</body></html>
'''.format(user, hostname, last_survival_time)

    return Subject, Text, 'html'


def send_email(to_addr: str, To: str, Subject: str, Text: str, TextType: str = 'html') -> bool:
    from email import encoders
    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import parseaddr, formataddr
    import smtplib

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    smtp_server = default_config.email.smtp_server
    from_addr = default_config.email.from_addr
    password = default_config.email.password
    from_user = default_config.email.from_user

    msg = MIMEText(Text, TextType, 'utf-8')
    msg['From'] = _format_addr('{} <{}>'.format(from_user, from_addr))
    msg['To'] = _format_addr('{} <{}>'.format(To, to_addr))
    msg['Subject'] = Header(Subject, 'utf-8').encode()

    try:
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()
        # server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

        return True
    except Exception as e:
        print(str(e))
        return False


def warning_report(machine: machine_status) -> None:
    for people in default_config.people_list:
        send_status = send_email(people.email, people.user, *
                                 (get_warning_text(people.user, machine.hostname, machine.last_survival_time)))

        logger.info('send warning email to {}, send status: {}'.format(
            people.user + '-' + people.email, send_status))
