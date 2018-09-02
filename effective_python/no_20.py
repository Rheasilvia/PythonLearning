from datetime import datetime
from time import sleep
import json


def log(message, when=None):
    """Log a message with a timestamp
    :param message: Message to print
    :param when: datetime of when the message occurred.
    Default to the present time
    :return:
    """
    when = datetime.now() if when is None else when
    print('%s: %s' % (when, message))


# if __name__ == '__main__':
#     log('Hi there!')
#     sleep(0.1)
#     log('Hi again!')

def decode(data, default=None):
    """
    Load data from a string

    :param data: JSON data to decode.
    :param default: Value to return if decoding fails.
    :return:
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


if __name__ == '__main__':
    foo = decode('bad data')
    foo['stuff'] = 5
    foo['haha'] = '23'
    bar = decode('also bad')
    bar['meep'] = 1
    print('Foo:', foo)
    print('Bar', bar)
