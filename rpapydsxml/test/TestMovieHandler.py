# -*- encoding: utf-8 -*-
#!/usr/bin/python3

import unittest
import logging
from logger_multi_modules.SingleLogger import SingleLogger
from rpapydsxml.classes.MovieHandler import MovieHandler


class TestMovieHandler(unittest.TestCase):
    
    def setUp(self):
        try:
            self.srvclog = SingleLogger(("%s.%s" %("TestCaseServiceLogger", __name__)), 0, "../../log/tests/", "test_service.log").logger
            self.srvclog.setLevel(logging.INFO)
            self.srvclog.info("Testing... Initializing tests for XML data source")
            #Create class object
            self.srvclog.info("Testing... Creating object for XML data source")
            self.movieHandler = MovieHandler()
            self.assertIsInstance(self.movieHandler, MovieHandler, "Object MovieHandler created")
        except:
            self.srvclog.setLevel(logging.ERROR)
            self.srvclog.exception("%s" %Exception.__doc__)
            raise Exception
        
        
    
    
    
    def testReadDataSource(self):
        try:
            self.srvclog.info("Testing... Running Read XML data source")
            self.movieHandler.readDataSource()
        except:
            self.srvclog.exception("%s" %Exception.__doc__)
            raise Exception
    
    
    def tearDown(self):
        try:
            self.srvclog.info("Testing... Leaving Unittest")
            del(self.movieHandler)
            del(self.srvclog)
            
            unittest.TestCase.tearDown(self)
        except:
            raise Exception


if __name__ == '__main__':
    unittest.main()



    