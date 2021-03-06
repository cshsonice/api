import time
from datetime import datetime
import os


def time_record(f):
    def wrapper(*args, **kwargs):
        t = time.time()
        return_value = f(*args, **kwargs)
        info = 'func: {} start: {} used time: {}'.format(f.__name__, t, time.time() - t)
        log(info, target='response-time.log')
        return return_value

    wrapper.__name__ = f.__name__
    return wrapper


def get_now() -> str:
    """return time of utc now"""
    return datetime.utcnow().strftime('%y-%m-%d %H:%M:%S')


def log(msg: str, target='api.log', log_type='INFO', isprint=False):
    """
    log function
    :param msg: log message
    :param target: save to
    :param log_type: [INFO, WARNING, ERROR]
    :param isprint: is it should be print
    :return:
    """
    log_type = log_type.upper()
    s = '[{}] {} - {} '.format(log_type, get_now(), msg)
    log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'log', target)
    with open(log_file, 'a') as f:
        f.write(s+'\n')
    if isprint:
        print(s)


