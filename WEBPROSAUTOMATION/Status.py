from pickle import TRUE
import sys
from colorama import init
from termcolor import colored

def PrintStatus(status,color):
    print(colored(status,color))

def printdone():
    PrintStatus('Done','green')


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()