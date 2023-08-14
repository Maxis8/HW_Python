import argparse
import logging
from collections import namedtuple
from pathlib import Path

logging.basicConfig(filename='logfiles.log',
                    level=logging.INFO,
                    format='{levelname} -> {msg} {asctime}',
                    style='{')
logger = logging.getLogger(__name__)

PathArgs = namedtuple('PathArgs', ['name', 'extension', 'dir', 'home_dir'])


def get_data(path):
    for item in Path(path).iterdir():
        if item.is_file():
            name, extension = item.name.split('.')
            dataset = PathArgs(name, '.' + extension, False, item.parent.name)
            logging.info(dataset)
        elif item.is_dir():
            dataset = PathArgs(item.name, None, True, item.parent.name)
            logging.info(dataset)
    return 'Recorded'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=str)
    args = parser.parse_args()
    print(get_data(args.p))

# python task_1.py -p ../'HW_15'

