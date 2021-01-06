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
        except:
            raise Exception
        
    
    def tearDown(self):
        try:
            del(self.srvclog)
            unittest.TestCase.tearDown(self)
        except:
            raise Exception
        

    def testMain(self):
        try:
            pass
        except:
            raise Exception
    
        

if __name__ == '__main__':
    unittest.main()
    
    
    
    