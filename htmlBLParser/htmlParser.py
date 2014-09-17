__author__ = 'selver'

import glob

from html.parser import HTMLParser

class pyHTMLParse(HTMLParser):
    saison = ''
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
    outputContent = ''
    def __init__(self, saison = '0/0'):
        # initialize the base class
        HTMLParser.__init__(self)
        self.saison = saison

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
                hyphenIdx = str(attrs[1][1]).find(' - ', idx)
                self.team1 = str(attrs[1][1])[idx:hyphenIdx].strip()
                self.team2 = str(attrs[1][1])[hyphenIdx+3:].strip()

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
            self.outputContent += self.composeLine()


    def handle_startendtag(self, tag, attrs):
        pass

    def newPlayDay(self, st):
        if st != self.playday:
            self.playday = st

    def composeLine(self):
        line = ','.join([self.playday, self.team1, self.team2, self.g1, self.g2, self.g1_first_half, self.g2_first_half, self.saison, '\n'])
        return line

    def getFinal(self):
        return self.outputContent


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


def main():
    dir = '/home/selver/PycharmProjects/htmlBLParser/site_results/*.html'
    all_html_files = glob.glob(dir)
    print(all_html_files)
    for f in all_html_files:
        reader = ReadHtml(f)
        reader.parse()
        last_slash = f.rfind('/')
        x1 = f.find(' ', last_slash)
        x1 = x1 + 1
        x2 = f.find(' ', x1)
        saison = f[x1:x1+4] + '/' + f[x1+5:x1+9]
        parser = pyHTMLParse(saison)
        parser.feed(reader.file_content)
        parser.close()
        outputName = "/home/selver/PycharmProjects/htmlBLParser/bundesliga1.csv"
        o = open(outputName, 'a')
        o.write(parser.getFinal())
        o.close()

if __name__ == "__main__":
    main()
