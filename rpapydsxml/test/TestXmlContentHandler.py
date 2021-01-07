# -*- encoding: utf-8 -*-
#!/usr/bin/python3

"""
@reference: https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler
"""

import unittest
import logging
import xml.sax
from xml.sax import ContentHandler
from logger_multi_modules.SingleLogger import SingleLogger


class TestCase(unittest.TestCase):
    
    def setUp(self):
        
        try:
            self.xmlObj = TestXmlContentHandler()
        except:
            raise Exception
    
    
    def testReadDataSource(self):
        try:
            result = self.xmlObj.readDataSource("../datasource/xml/", "movies.xml")
            print(result)
        except:
            raise Exception
    
    
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)



class TestXmlContentHandler(ContentHandler):
    
    def __init__(self):
        try:
            print("TestXmlContentHandler objeto criado")
            self.arrayDict = []
            self.xmlDS = {}
            self.reservedTags = []
            self.movieInfo = []
            self.rootTag = ""
        except:
            raise Exception
    
    
    def __getXmlRootTagName(self, filePath:str, fileName:str) -> str:
        try:
            import xml.etree.cElementTree as ET
            tree = ET.parse("%s%s" %(filePath, fileName))
            root = tree.getroot() 
            root_tag = root.tag.replace("'", '"')
            
            self.reservedTags.append(root_tag)
            
            return root_tag
        except:
            raise Exception
    
    
    def __getXmlNestedTagName(self, filePath:str, fileName:str) -> str:
        """
        @TODO: Implement programming to solve in sequence childs and nested on childs nodes.
        """
        try:
            #not implemented yet
            return "movie"
        except:
            raise Exception
        
    def __getLastXmlNestedTag(self):
        """
        @TODO: Implement programming to get the last nested node
        """
        return "description"
    
    
    def readDataSource(self, filePath:str, fileName:str) -> str:
        try:
            print("TestXmlContentHandler readDataSource() acessado")
            parser = xml.sax.make_parser()
            
            # turn off namepsaces
            parser.setFeature(xml.sax.handler.feature_namespaces, 0)
            
            # override the default ContextHandler
            parser.setContentHandler(self)
            parser.parse("%s%s" %(filePath, fileName))
            
            del(parser)
            dados = self.arrayDict
            del(self.arrayDict)
            del(self.xmlDS)
            del(self.reservedTags)
            del(self.movieInfo)
            del(self.rootTag)
            
            return dados
        except:
            raise Exception
    
    
    
    def startElement(self, name, attrs):
        """
        @TODO: Implement this method for more nested nodes
        @author: Sandro Regis Cardoso | Software Eng.
        """
        try:
            self.rootTag = self.__getXmlRootTagName("../datasource/xml/", "movies.xml")
            if len(attrs._attrs).__gt__(0):
                print("TestXmlContentHandler ContentHandler.startElement() acessado")
                print("Parameter name value: %s" %name, sep=" | ")
                print("Parameter attrs value: %s" %attrs._attrs)
                
                if self.rootTag.__eq__(name) and len(self.xmlDS).__eq__(0):
                    self.xmlDS[self.rootTag] = attrs._attrs
                    #print(self.xmlDS, end="\n\n")
                else:
                    self.reservedTags.append(name)
                    self.xmlDS[self.rootTag][name] = attrs._attrs
                    #print(self.xmlDS, end="\n\n")
        except:
            raise Exception
    
    
    
    def endElement(self, tag):
        """
        @TODO:  Read path and file name from config.yaml
                Do a better programming to solve child and nested child nodes.
                Fix append new object to resulting array
        @author: Sandro Regis Cardoso | Software Eng.
        """
        try:
            print("TestXmlContentHandler ContentHandler.endElement() acessado")
            print("Parameter tag value: %s" %tag, end="\n\n")
            childTag = self.__getXmlNestedTagName("../datasource/xml/", "movies.xml")
            if tag not in self.reservedTags:
                self.movieInfo.append(tag)
            
            if len(self.movieInfo).__eq__(2):
                for val in self.movieInfo:
                    self.xmlDS[self.rootTag][childTag][self.movieInfo[1]] = self.movieInfo[0]
                print(self.xmlDS, end="\n\n")
                self.movieInfo.clear()
                if tag.__eq__(self.__getLastXmlNestedTag()):
                    self.arrayDict.append(self.xmlDS)
                    print(self.arrayDict)
                    self.xmlDS.clear()
        except:
            raise Exception
    
    
    
    def characters(self, content):
        try:
            if len(content.strip()).__gt__(0):
                print("TestXmlContentHandler ContentHandler.characters() acessado")
                print("Parameter content value: %s" %content, end="\n\n")
                self.movieInfo.append(content)
        except:
            raise Exception




if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
