#!/usr/bin/env python
# -*- coding:utf-8 -*
import os
import argparse
import dbm
import re
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Process


class Bing(object):

    def __init__(self):
        super(Bing, self).__init__()

    def query(self, word):
        import requests
        from bs4 import BeautifulSoup
        sess = requests.Session()
        headers = {
            'Host': 'cn.bing.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
        }
        sess.headers.update(headers)
        url = 'http://cn.bing.com/dict/SerpHoverTrans?q=%s' % (word)
        try:
            resp = sess.get(url, timeout=100)
        except:
            return None
        text = resp.text
        if (resp.status_code == 200) and (text):
            soup = BeautifulSoup(text, 'lxml')
            if soup.find('h4').text.strip() != word.decode('utf-8'):
                return None
            lis = soup.find_all('li')
            trans = []
            for item in lis:
                transText = item.get_text()
                if transText:
                    trans.append(transText)
            return '\n'.join(trans)
        else:
            return None


class Youdao(object):

    def __init__(self):
        super(Youdao, self).__init__()

    def query(self, word):
        import requests
        try:
            import xml.etree.cElementTree as ET
        except ImportError:
            import xml.etree.ElementTree as ET
        sess = requests.Session()
        headers = {
            'Host': 'dict.youdao.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate'
        }
        sess.headers.update(headers)
        url = 'http://dict.youdao.com/fsearch?q=%s' % (word)
        try:
            resp = sess.get(url, timeout=100)
        except:
            return None
        text = resp.content
        if (resp.status_code == 200) and (text):
            tree = ET.ElementTree(ET.fromstring(text))
            returnPhrase = tree.find('return-phrase')
            if returnPhrase.text.strip() != word.decode('utf-8'):
                return None
            customTranslation = tree.find('custom-translation')
            if not customTranslation:
                return None
            trans = []
            for t in customTranslation.findall('translation'):
                transText = t[0].text
                if transText:
                    trans.append(transText)
            return '\n'.join(trans)
        else:
            return None


class Iciba(object):

    def __init__(self):
        super(Iciba, self).__init__()

    def query(self, word):
        import requests
        from bs4 import BeautifulSoup
        sess = requests.Session()
        headers = {
            'Host': 'open.iciba.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate'
        }
        sess.headers.update(headers)
        url = 'http://open.iciba.com/huaci_new/dict.php?word=%s' % (word)
        try:
            resp = sess.get(url, timeout=100)
            text = resp.text
            pattern = r'(<div class=\\\"icIBahyI-group_pos\\\">[\s\S]+?</div>)'
            text = re.search(pattern, text).group(1)
        except:
            return None
        if (resp.status_code == 200) and (text):
            soup = BeautifulSoup(text, 'lxml')
            ps = soup.find_all('p')
            trans = []
            for item in ps:
                transText = item.get_text()
                transText = re.sub(
                    r'\s+', ' ', transText.replace('\t', '')).strip()
                if transText:
                    trans.append(transText)
            return '\n'.join(trans)
        else:
            return None


path = os.path.dirname(os.path.realpath(__file__))
db = dbm.open(path + '/data/vocabulary', 'c')
DEFAULT_SERVICE = 'bing'


class Client(object):

    def __init__(self, word, service=None, webonly=False):
        super(Client, self).__init__()
        if not service:
            service = DEFAULT_SERVICE
        self.service = service
        self.word = word
        self.trans = None
        if webonly:
            self.db = {}
        else:
            self.db = db

    def translate(self):
        trans = self.db.get(self.word)
        if trans:
            return trans
        else:
            if self.service == 'bing':
                S = Bing()
            if self.service == 'youdao':
                S = Youdao()
            elif self.service == 'iciba':
                S = Iciba()
            trans = S.query(self.word)
            self.trans = trans
            return trans

    def suggest(self):
        if re.sub(r'[a-zA-Z\d\'\-\.\s]', '', self.word):
            return None
        import enchant
        try:
            d = enchant.DictWithPWL(
                'en_US', path + '/data/spell-checker/american-english-large')
        except:
            d = enchant.Dict('en_US')
        suggestion = d.suggest(self.word)
        return suggestion

    def pronounce(self, tts):
        if tts == 'festival':
            cmd = ' echo "%s" | festival --tts > /dev/null 2>&1' % (self.word)
        elif tts == 'espeak':
            cmd = 'espeak -v en-us "%s" > /dev/null 2>&1' % (self.word)
        elif tts == 'real':
            cmd = 'find %s/data/RealPeopleTTS/ -type f -iname "%s.wav" | head -n1 | xargs -I {} aplay {} > /dev/null 2>&1' % (
                path, self.word)
        import commands
        try:
            status, output = commands.getstatusoutput(cmd)
        except:
            pass
        return True

    def updateDB(self):
        if self.trans:
            db[self.word] = self.trans.encode('utf-8')
        db.close()
        return True


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help="word or 'some phrase'")
    parser.add_argument('-n', '--nostorage', dest='nostorage',
                        action='store_true', help='turn off data storage')
    parser.add_argument('-p', '--pronounce', dest='pronounce', choices=[
                        'espeak', 'festival', 'real'], help="text-to-speech software: 'espeak', 'festival' or 'real'")
    parser.add_argument('-s', '--service', dest='service', choices=[
                        'bing', 'youdao', 'iciba'], help="translate service: 'bing', 'youdao' or 'iciba'")
    parser.add_argument('-w', '--webonly', dest='webonly',
                        action='store_true', help='ignore local data')
    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s 0.1.3')
    return parser.parse_args()


if __name__ == '__main__':
    args = parseArgs()
    word = args.word.strip()
    service = args.service
    webonly = args.webonly
    if service:
        webonly = True
    C = Client(word, service=service, webonly=webonly)
    pool = ThreadPool()
    _trans = pool.apply_async(C.translate)
    _suggestion = pool.apply_async(C.suggest)
    trans = _trans.get()
    if trans:
        print trans
        if args.pronounce:
            p1 = Process(target=C.pronounce, args=(args.pronounce,))
            p1.daemon = True
            p1.start()
        if not args.nostorage:
            p2 = Process(target=C.updateDB)
            p2.daemon = True
            p2.start()
    else:
        suggestion = _suggestion.get()
        if not suggestion:
            print 'No translations found for \"%s\" .' % (word)
        else:
            print 'No translations found for \"%s\", maybe you meant:\
                  \n\n%s' % (word, ' / '.join(suggestion))
