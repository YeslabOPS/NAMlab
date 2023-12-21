import time
import random
import logging

logging.basicConfig(filename='testquit.log', 
                    level=logging.INFO,
                    format = '%(asctime)s  %(filename)s : %(levelname)s  %(message)s',
                    datefmt = '%Y-%m-%d %A %H:%M:%S')

while True:
    number = random.random()
    if number < 0.1:
        logging.error(f'Error: {number}')
    else:
        logging.info(number)
    time.sleep(5)

