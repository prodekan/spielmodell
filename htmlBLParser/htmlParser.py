__author__ = 'selver'
#
# import html.parser
#
# class pyHTMLParse(html.parser.HTMLParser):
# def __init__(self):
#         # initialize the base class
#         html.HTMLParser.__init__(self)
#     def handle_starttag(self, tag, attrs):
#         print ("Encountered a start tag:", tag)
#     def handle_endtag(self, tag):
#         print ("Encountered an end tag :", tag)
#     def handle_data(self, data):
#         print ("Encountered some data  :", data)
#
# parser = pyHTMLParse()
# parser.feed('<html><head><title>Test</title></head>'
#             '<body><h1>Parse me!</h1></body></html>')
#

from html.parser import HTMLParser

class pyHTMLParse(HTMLParser):
    playday = ''
    team1 = ''
    team2 = ''
    datum = ''
    g1 = ''
    g2 = ''
    g1_first_half = ''
    g2_first_half = ''
    gotcha = False
    gotchaPlayday = False
    def __init__(self):
        # initialize the base class
        HTMLParser.__init__(self)

    def read(self, data):
        # clear the current output before re-use
        self._lines = []
        # re-set the parser's state before re-use
        self.reset()
        self.feed(data)
        return ''.join(self._lines)

    def handle_starttag(self, tag, attrs):

        if len(attrs) > 1 and len(attrs[0]) > 1:
            if '/spielbericht/bundesliga' in str(attrs[0][1]):
                self.gotcha = True
                #print('-------------->', attrs[1][1])
                idx = str(attrs[1][1]).find('Spielschema', 0)
                if idx == -1:
                    print('Something is wrong')
                    return
                idx = idx + len('Spielschema') + 1
                hyphenIdx = str(attrs[1][1]).find('-', idx)
                self.team1 = str(attrs[1][1])[idx:hyphenIdx].strip()
                self.team2 = str(attrs[1][1])[hyphenIdx+1:].strip()

        elif len(attrs) > 0 and len(attrs[0]) > 0:
            if '/spielplan/bundesliga' in str(attrs[0][1]):
                self.gotchaPlayday = True



    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if self.gotchaPlayday == True:
            self.playday = data
            self.gotchaPlayday = False
        elif self.gotcha == True:
            colonIdx = str(data).find(':')
            spaceIdx = str(data).find(' ', colonIdx)
            lbracketIdx = str(data).find('(', spaceIdx)
            rbracketIdx = str(data).find(')', lbracketIdx)
            self.g1 = str(data)[:colonIdx]
            self.g2 = str(data)[colonIdx+1:spaceIdx]
            colonIdx = str(data).find(':', lbracketIdx)
            self.g1_first_half = str(data)[lbracketIdx+1:colonIdx]
            self.g2_first_half = str(data)[colonIdx+1:rbracketIdx]
            self.gotcha = False
            print(self.composeLine())


    def handle_startendtag(self, tag, attrs):
        pass

    def newPlayDay(self, st):
        if st != self.playday:
            self.playday = st

    def composeLine(self):
        line = ','.join([self.playday, self.team1, self.team2, self.g1, self.g2, self.g1_first_half, self.g2_first_half])
        return line


class ReadHtml:
    file_location = ''
    file_content = ''
    test_line = ''
    fd = 0
    def __init__(self, file):
        self.file_location = file
        print('setting file location ', self.file_location)

    def parse(self):
        self.fd = open(self.file_location, 'r')
        self.file_content = self.fd.read()
        self.fd.close()

    def printLineToFile(self, outputLocation, content):
        wr = open(outputLocation, 'a');
        wr.write(content)


def main():
    reader = ReadHtml('/home/selver/PycharmProjects/htmlBLParser/bl63-64.html')
    reader.parse()
    parser = pyHTMLParse()
    parser.feed(reader.file_content)
    parser.close()

if __name__ == "__main__":
    main()


