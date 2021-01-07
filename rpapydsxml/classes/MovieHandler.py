#!/usr/bin/python3.7

"""
@origin: https://www.tutorialspoint.com/python/python_xml_processing.html

"""

import xml.sax
from logger_multi_modules.SingleLogger import SingleLogger
import logging


class MovieHandler(xml.sax.ContentHandler):
    _name = "movie.handler"
    
    def __init__(self):
        try:
            #self.srvclog = SingleLogger(("%s.%s" %("Service Logger", __name__)), 0, "./log/global/", "service.log").logger
            #self.srvclog.setLevel(logging.INFO)
            #self.srvclog.info("Initializing Movie Handler object.......")
            self.array_dict = []
            self.xmlBlock = {}
            self.CurrentData = ""
            self.description = ""
            self.title  = ""
            self.type   = ""
            self.format = ""
            self.year   = ""
            self.rating = ""
            self.stars  = ""
        except:
            raise Exception
    
    
    def startElement(self, tag, attributes):
        try:
            
            self.CurrentData = tag
            if tag == "movie":
                self.xmlBlock['tag'] = tag
                print("\n***** Movie *****")
                #title = attributes["title"]
                #print("Title:", title)
            
        except:
            raise Exception
    
    
    # Call when a character is read
    def characters(self, content):
        try:
            if self.CurrentData == "title":
                self.title   = content
            elif self.CurrentData == "type":
                self.type   = content
            elif self.CurrentData == "format":
                self.format = content
            elif self.CurrentData == "year":
                self.year   = content
            elif self.CurrentData == "rating":
                self.rating = content
            elif self.CurrentData == "stars":
                self.stars  = content
            elif self.CurrentData == "description":
                self.description = content
                
                self.xmlBlock['description'] = self.description
                self.array_dict.append(self.xmlBlock)
                self.xmlBlock.clear()
        except:
            raise Exception
    
    
    
    def endElement(self, tag):
        try:
            if self.CurrentData == "title":
                #self.xmlBlock['title'] = self.title
                print("Title:", self.title)
            elif self.CurrentData == "type":
                #self.xmlBlock['type'] = self.type
                print("Type:", self.type)
            elif self.CurrentData == "format":
                #self.xmlBlock['type'] = self.format
                print("Format:", self.format)
            elif self.CurrentData == "year":
                #self.xmlBlock['year'] = self.year
                print("Year:", self.year)
            elif self.CurrentData == "rating":
                #self.xmlBlock['rating'] = self.rating
                print("Rating:", self.rating)
            elif self.CurrentData == "stars":
                #self.xmlBlock['stars'] = self.stars
                print("Stars:", self.stars)
            elif self.CurrentData == "description":
                #self.xmlBlock['description'] = self.description
                print("Description:", self.description)
            
            self.CurrentData = ""
            
            #self.array_dict.append(self.xmlBlock)
            print(self.array_dict)
            #print(self.xmlBlock)
        except:
            raise Exception
    
    
    
    def readDataSource(self):
        try:
            #self.srvclog.info("Start to Reading Data Source file.......")
            # create an XMLReader
            parser = xml.sax.make_parser()
            
            # turn off namepsaces
            parser.setFeature(xml.sax.handler.feature_namespaces, 0)
            
            # override the default ContextHandler
            parser.setContentHandler(self)
            parser.parse("../datasource/xml/movies.xml")
        except:
            raise Exception
        
