# -*- encoding: utf-8 -*-
#!/usr/bin/python3

import unittest
import logging
from logger_multi_modules.SingleLogger import SingleLogger
from pid.decorator import pidfile
import os


class TestMain(unittest.TestCase):

    def setUp(self):
        try:
            self.srvclog = SingleLogger(("%s.%s" %("TestCaseServiceLogger", __name__)), 0, "../log/tests/", "test_service.log").logger
            self.assertNotIsInstance(self.srvclog, SingleLogger, "Testing... Logger Instance Created")
            self.srvclog.setLevel(logging.INFO)
            self.srvclog.info("Testing... Log level INFO set.")
            content = self.__readFile("../log/tests/", "test_service.log")
            self.assertFalse(len(content) == 0, "Log file is recording...")
            self.srvclog.info("Testing... Log file is recording")
        except:
            self.srvclog.setLevel(logging.ERROR)
            self.srvclog.exception("%s" %Exception.__doc__)
            raise Exception
    
    
    
    def __readFile(self, filePath:str, fileName:str) -> str:
        try:
            self.srvclog.info("Testing... Read file %s%s" %(filePath, fileName))
            content = ""
            with open("%s%s" %(filePath, fileName), "r") as logfile:
                content = logfile.read()
                logfile.close()
                return content
        except:
            raise Exception
    
    
    @pidfile("test_rpads.pid", "../bin/")
    def testMain(self):
        try:
            varPid = os.getpid()
            rpaPid = self.__readFile("../bin/", "test_rpads.pid")
            self.assertEqual(varPid, int(rpaPid), "Running PID %s is equal %s recorded on file" %(varPid, rpaPid))
            self.srvclog.info("Testing... Running PID %s is equal %s recorded on file" %(varPid, rpaPid))
        except:
            self.srvclog.exception("%s" %Exception)
            raise Exception
    
    
    
    def tearDown(self):
        try:
            self.srvclog.info("Testing... Leaving Unittest")
            del(self.srvclog)
            unittest.TestCase.tearDown(self)
        except:
            raise Exception



if __name__ == '__main__':
    unittest.main()
    
    
    
    