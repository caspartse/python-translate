# python-translate
python-translate is a simple command line dictionary, it powered by Bing, Youdao and Iciba translation services.

![](https://raw.githubusercontent.com/caspartse/python-translate/master/screenshot.jpg)

# Features
* English-Chinese / Chinese-English
* Spell checking and suggestion (English only)
* Data storage (with dbm module)
* Pronunciation

# Usage
```
usage: translate.py [-h] [-n] [-p] [-s SERVICE] [-w] [-V] word

positional arguments:
  word                  word or 'some phrase'

optional arguments:
  -h, --help            show this help message and exit
  -n, --nostorage       turn off data storage
  -p, --pronounce       eSpeak text-to-speech
  -s SERVICE, --service SERVICE
                        choose translate service: 'bing', 'youdao' or 'iciba'
  -w, --webonly         ignore local data
  -V, --version         show program's version number and exit
```

# Requirements
* [requests](http://python-requests.org)
* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)
* [lxml](http://lxml.de/)
* [pyenchant](https://pythonhosted.org/pyenchant/)
* [eSpeak](http://espeak.sourceforge.net/) (for pronunciation, optional)

# Tips
`$ alias t="python2 /path/to/the/translate.py"`

# External Resources
* [SCOWL (Spell Checker Oriented Word Lists)](http://wordlist.aspell.net/)
* [List of spell checkers](http://www.dmoz.org/Arts/Writers_Resources/Software/Spelling_and_Grammar/Spell_Checkers)
* [Wiktionary:Frequency lists](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists)
* [wordlist.10000](http://www.mit.edu/~ecprice/wordlist.10000)
* [top10000en.txt](http://wortschatz.uni-leipzig.de/Papers/top10000en.txt)
* [google-10000-english](https://github.com/first20hours/google-10000-english)
