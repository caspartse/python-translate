## python-translate
python-translate is a simple command line dictionary, it powered by Bing, Youdao and Iciba translation services.

### Screenshot
![](https://raw.githubusercontent.com/caspartse/python-translate/master/screenshot.jpg)

### Features
* English-Chinese / Chinese-English
* Spell checking and suggestion (English only)
* Data storage (with dbm module)
* Pronunciation

### Usage
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

#### 关于本地数据使用

默认使用本地数据库，如需关闭，可使用 `-w` 或 `--webonly` 选项。
```
$ python2 translate.py hello -w
```

#### 关于翻译服务选择

可使用 `-s` 或 `--service` 选项指定翻译服务：bing |  youdao |  iciba ，默认使用必应翻译。以下三种表示方法均有效：
```
$ python2 translate.py hello -s=youdao
$ python2 translate.py hello -s youdao
$ python2 translate.py hello -syoudao
```

#### 关于单词发音

单词发音功能默认关闭，如需启用，可使用 `-p` 或 `--pronounce` 选项。
可修改源码中的 `pronounce` 部分以更改 eSpeak 的[发音配置](http://espeak.sourceforge.net/docindex.html)。

另外 TTS 合成语音效果一般，若有真人语音文件，可配合 aplay、mpg321、sox 等命令使用。
```
$ python2 translate.py hello -p
```

### Requirements
* [requests](http://python-requests.org)
* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)
* [lxml](http://lxml.de/)
* [pyenchant](https://pythonhosted.org/pyenchant/)
* [eSpeak](http://espeak.sourceforge.net/) (for pronunciation, optional)

### Tips
`$ alias t="python2 /path/to/the/translate.py"`

### External Resources
* [SCOWL (Spell Checker Oriented Word Lists)](http://wordlist.aspell.net/)
* [List of spell checkers](http://www.dmoz.org/Arts/Writers_Resources/Software/Spelling_and_Grammar/Spell_Checkers)
* [Wiktionary:Frequency lists](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists)
* [wordlist.10000](http://www.mit.edu/~ecprice/wordlist.10000)
* [top10000en.txt](http://wortschatz.uni-leipzig.de/Papers/top10000en.txt)
* [google-10000-english](https://github.com/first20hours/google-10000-english)
