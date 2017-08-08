from datetime import datetime


def log(x):
    """Emulates simple logging system"""
    print('[LOG] ' + str(datetime.now()) + ' : ' + str(x))
