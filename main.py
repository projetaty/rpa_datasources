#!/usr/bin/python3.7
# encoding: utf-8
    
import logging
from logger_multi_modules.SingleLogger import SingleLogger
from pid.decorator import pidfile
import os

import threading
import sys

@pidfile("rpads.pid", "./bin/")
def main(*args, **kwargs):
    try:
        srvclog = SingleLogger(("%s.%s" %("Service Logger", __name__)), 0, "./log/global/", "service.log").logger
        srvclog.setLevel(logging.INFO)
        srvclog.info("Logger instance created.......")
        srvclog.info("Running main program....... pidg: %s"  %os.getpgid(os.getpid()))
        ##########
        i = 0
        while True:
            srvclog.info("Ele é o bãooooo.......")
            srvclog.info("é o bãooooo.......")
            srvclog.info("é o bãooooo!")
            i += 1
            if i == 3:
                break
    
    except:
        raise Exception


if __name__ == "__main__":
    try:
        main()
        print(threading.current_thread().is_alive())
        sys.exit
        print(threading.current_thread().daemon)
    except:
        raise Exception
    
    
    
    
    
