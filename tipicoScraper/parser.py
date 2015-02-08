__author__ = 'selver'

import glob
import os
import sys
from html.parser import HTMLParser
import urllib

import urllib.request
import urllib.error

class pyHTMLParse(HTMLParser):
    currPlayDay = ''
    currPlayTime = ''
    currTeam1 = ''
    currTeam2 = ''
    currQ1 = 0
    currQX = 0
    currQ2 = 0
    outputContent = ''
    def __init__(self):
        HTMLParser.__init__(self)

    def read(self, data):
        # clear the current output before re-use
        self._lines = []
        # re-set the parser's state before re-use
        self.reset()
        self.feed(data)
        return ''.join(self._lines)

    def handle_starttag(self, tag, attrs):
        if tag == 'h2':
            if attrs[0][0] == 'class' and attrs[0][1] == 'event-group-level1':
                print(tag, attrs)


    def handle_endtag(self, tag):
        print('<END>')
        print(tag)

    def handle_data(self, data):
        print(data)

    def handle_startendtag(self, tag, attrs):
        print('handle_startendtag')

    def newPlayDay(self, st):
        pass

    def getFinal(self):
        return self.outputContent

import codecs
class ReadHtml:
    file_location = ''
    file_content = ''
    fd = 0
    def __init__(self, file):
        self.file_location = file
        print('setting file location ', self.file_location)

    def parse(self):
        try:
            #self.fd = open(self.file_location, 'r')
            self.fd = codecs.open(self.file_location, 'r', 'utf8')
            self.file_content = self.fd.read()
        except IOError:
            print ('error reading file:', self.file_location)
            self.fd.close()

        self.fd.close()

def main():
    tipico_home = "C:\\Users\\selver\\PycharmProjects\\tipicoScraper\\bwin_BL1.html"

    reader = ReadHtml(tipico_home)
    reader.parse()
    parser = pyHTMLParse()
    parser.feed(reader.file_content)
    parser.close()
    outputName = "C:\\Users\\selver\\PycharmProjects\\tipicoScraper\\output.csv"
    o = open(outputName, 'a')
    o.write(parser.getFinal())
    o.close()

if __name__ == "__main__":
    main()
