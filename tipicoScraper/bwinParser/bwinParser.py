__author__ = 'selver'

import glob
import os
import sys
from html.parser import HTMLParser
import urllib

import urllib.request
import urllib.error


class pyHTMLParse(HTMLParser):
    currLeague = ''
    currCountry = ''
    currPlayDay = ''
    currPlayTime = ''
    currTeam1 = ''
    currTeam2 = ''
    currQ1 = 0
    currQX = 0
    currQ2 = 0
    indicators = [0, 0, 0, 0, 0, 0]  # Q1,T1,QX,TX,Q2,T2
    currRow = ''
    outputContent = ''
    currTag = ''

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
        if tag == 'h2' and len(attrs) > 0 and len(attrs[0]) > 0 and attrs[0][1] == 'event-group-level1':
            self.currTag = tag
            self.currPlayDay = '?'
            return

        if tag == 'a' and len(attrs) > 0 and len(attrs[0]) > 0 and attrs[0][0] == 'class' \
                and attrs[0][1] == 'league-link':
            self.currTag = tag
            self.currLeague = '?'
            return

        if tag == 'h6' and len(attrs) > 0 and len(attrs[0]) > 0 and attrs[0][0] == 'class' \
                and attrs[0][1] == 'event-header-level0':
            self.currTag = tag
            self.currPlayTime = '?'
            return

        if tag == 'span' and len(attrs) > 0 and len(attrs[0]) > 0 and attrs[0][0] == 'class' \
                and attrs[0][1] == 'option-name':
            self.currTag = tag
            self.indicators = self.shiftIndicators()
            return

        if tag == 'span' and len(attrs) > 0 and len(attrs[0]) > 0 and attrs[0][0] == 'class' \
                and attrs[0][1] == 'odds':
            self.currTag = tag
            self.indicators = self.shiftIndicators()
            return

    def handle_data(self, data):
        if self.currTag != '' and self.currPlayDay == '?':
            self.currPlayDay = data
            self.currPlayDay = str(self.currPlayDay)[str(self.currPlayDay).find('-', 0) + 1:].strip()
            self.currTag = ''

        if self.currTag != '' and self.currPlayTime == '?':
            self.currPlayTime = str(data).strip()
            self.currTag = ''

        if self.currTag != '' and self.currLeague == '?':
            self.currLeague = data
            self.currLeague = str(self.currLeague)[:str(self.currLeague).find('-', 0)].strip()
            self.currCountry = str(data)[str(data).find('-', 0) + 1:].strip()
            self.currTag = ''

        if self.currTag != '' and self.indicators == [1, 0, 0, 0, 0, 0]:
            self.currQ1 = float(data)
            self.currTag = ''

        if self.currTag != '' and self.indicators == [0, 1, 0, 0, 0, 0]:
            self.currTeam1 = str(data).strip()
            self.currTag = ''

        if self.currTag != '' and self.indicators == [0, 0, 1, 0, 0, 0]:
            self.currQX = float(data)
            self.currTag = ''

        if self.currTag != '' and self.indicators == [0, 0, 0, 0, 1, 0]:
            self.currQ2 = float(data)
            self.currTag = ''

        if self.currTag != '' and self.indicators == [0, 0, 0, 0, 0, 1]:
            self.currTeam2 = str(data).strip()
            self.currTag = ''
            self.outputContent += self.composeLine()


    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        pass

    def getFinal(self):
        print(self.outputContent)
        return self.outputContent

    def shiftIndicators(self):
        if self.indicators == [0, 0, 0, 0, 0, 0]:
            return [1, 0, 0, 0, 0, 0]
        elif self.indicators == [1, 0, 0, 0, 0, 0]:
            return [0, 1, 0, 0, 0, 0]
        elif self.indicators == [0, 1, 0, 0, 0, 0]:
            return [0, 0, 1, 0, 0, 0]
        elif self.indicators == [0, 0, 1, 0, 0, 0]:
            return [0, 0, 0, 1, 0, 0]
        elif self.indicators == [0, 0, 0, 1, 0, 0]:
            return [0, 0, 0, 0, 1, 0]
        elif self.indicators == [0, 0, 0, 0, 1, 0]:
            return [0, 0, 0, 0, 0, 1]
        elif self.indicators == [0, 0, 0, 0, 0, 1]:
            return [1, 0, 0, 0, 0, 0]

    def composeLine(self):
        line = ','.join([self.currCountry, self.currLeague, self.currPlayDay, self.currPlayTime,
                         self.currTeam1, self.currTeam2, str(self.currQ1), str(self.currQX), str(self.currQ2), '\n'])
        return line


import codecs


class ReadHtml:
    file_location = ''
    file_content = ''
    fd = 0

    def __init__(self, file):
        self.file_location = file
        print('Location ', self.file_location)

    def parse(self):
        try:
            self.fd = codecs.open(self.file_location, 'r', 'utf8')
            self.file_content = self.fd.read()
        except IOError:
            print('error reading file:', self.file_location)
            self.fd.close()
        self.fd.close()


def main():
    tipico_home = "bwin_BL1.html"
    reader = ReadHtml(tipico_home)
    reader.parse()
    parser = pyHTMLParse()
    parser.feed(reader.file_content)
    parser.close()
    outputName = "output.csv"
    o = open(outputName, 'a')
    o.write(parser.getFinal())
    o.close()


if __name__ == "__main__":
    main()
