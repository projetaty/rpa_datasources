

import unittest
from xml.sax.handler import ContentHandler
import xml.sax
import json

class TestCase(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
    
    def testProgramXmlHandler(self):
        
        class TestJsonQueue(object):
            QUEUE = {}
            def addData(self, queueData : dict):
                try:
                    pass
                except:
                    raise Exception
        
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
                    del(self.arrayDict)
                    del(self.xmlDS)
                    del(self.reservedTags)
                    del(self.movieInfo)
                    del(self.rootTag)
                except:
                    raise Exception
                
            
            def startElement(self, name, attrs):
                """
                @TODO: Implement this method for more nested nodes
                @author: Sandro Regis Cardoso | Software Eng.
                """
                try:
                    self.rootTag = self.__getXmlRootTagName("../../datasource/xml/", "movies.xml")
                    if len(attrs._attrs).__gt__(0):
                        print("TestXmlContentHandler ContentHandler.startElement() acessado")
                        print("Parameter name value: %s" %name, sep=" | ")
                        print("Parameter attrs value: %s" %attrs._attrs)
                        
                        if self.rootTag.__eq__(name) and len(self.xmlDS).__eq__(0):
                            self.xmlDS[self.rootTag] = attrs._attrs
                            #print(self.xmlDS, end="\n\n")
                        else:
                            """
                            @TODO: Fix the programming in exception while solving pending methods
                            """
                            self.reservedTags.append(name)
                            try:
                                self.xmlDS[self.rootTag][name] = attrs._attrs
                                #print(self.xmlDS, end="\n\n")
                            except Exception as ex:
                                if self.rootTag in ex.args:
                                    self.xmlDS[self.rootTag] = {'shelf': 'New Arrivals'}
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
                    childTag = self.__getXmlNestedTagName("../../datasource/xml/", "movies.xml")
                    if tag not in self.reservedTags:
                        self.movieInfo.append(tag)
                    
                    if len(self.movieInfo).__eq__(2):
                        #for val in self.movieInfo:
                        self.xmlDS[self.rootTag][childTag][self.movieInfo[1]] = self.movieInfo[0]
                        self.movieInfo.clear()
                        #print(self.xmlDS, end="\n\n")
                    
                    if tag.__eq__(self.__getLastXmlNestedTag()) and self.xmlDS not in self.arrayDict:
                        
                        """
                        @TODO: Implement programming to get path and file name related to source file
                        @author:  Sandro Regis Cardoso | Software Eng.
                        """
                        self.arrayDict.append(self.xmlDS)
                        
                        with open("%s%s" %("../../queue/", "movies.json"), "a", encoding="utf-8") as jf:
                            jf.write(json.dumps(self.xmlDS))
                            jf.close()
                    
                    if tag.__eq__(self.rootTag):
                        print(self.arrayDict)
                        #self.__openJsonFile("../../queue/", "movies.json")
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
    
    
    
            def __openJsonFile(self, filePath : str, jsonFileName : str) -> str:
                try:
                    with open("%s%s" %(filePath, jsonFileName), "r") as jfQueue:
                        #jsq = json.load(jfQueue)
                        jsq = jfQueue.read()
                        print(jsq)
                        jfQueue.close()
                except:
                    raise Exception
                
        
        try:
            program = object.__new__(unittest.TestProgram)
            program.testXmlContentHandler = TestXmlContentHandler()
            program.testXmlContentHandler.readDataSource("../../datasource/xml/", "movies.xml")
        except:
            raise Exception





if __name__ == '__main__':
    unittest.main()









