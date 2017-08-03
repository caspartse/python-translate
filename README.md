## python-translate
python-translate is a simple command line dictionary, it powered by Bing, Youdao and Iciba translation services.

### Screenshot
![](https://raw.githubusercontent.com/caspartse/python-translate/master/screenshot_v0.1.3.jpg)

### Features
* English-Chinese / Chinese-English
* Spell checking and suggestion (English only)
* Data storage (with dbm module)
* Pronunciation

### Usage
```
usage: translate.py [-h] [-n] [-p {espeak,festival}] [-s {bing,youdao,iciba}]
                    [-w] [-V]
                    word

positional arguments:
  word                  word or 'some phrase'

optional arguments:
  -h, --help            show this help message and exit
  -n, --nostorage       turn off data storage
  -p {espeak,festival}, --pronounce {espeak,festival}
                        text-to-speech software: 'espeak' or 'festival'
  -s {bing,youdao,iciba}, --service {bing,youdao,iciba}
                        translate service: 'bing', 'youdao' or 'iciba'
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
若该选项非空，则 `webonly` 会自动开启，即不使用本地数据库。

#### 关于单词发音

单词发音功能默认关闭，如需启用，可使用 `-p` 或 `--pronounce` 选项，选择具体的软件发音： espeak | festival 。

另外 TTS 合成语音效果一般，若有真人语音文件，可配合 aplay、mpg321、sox 等命令使用，可修改源码中的 `pronounce` 部分以更改的发音配置。
```
$ python2 translate.py hello -p=espeak
$ python2 translate.py hello -p=festival
$ python2 translate.py hello -p=real
```

### Requirements
* [requests](http://python-requests.org)
* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)
* [lxml](http://lxml.de/)
* [pyenchant](https://pythonhosted.org/pyenchant/)

```
$ pip install requests beautifulsoup4 lxml pyenchant
# OR
$ pip install -r requirements.txt
```

* [lxml](http://lxml.de/index.html)
* [eSpeak](http://espeak.sourceforge.net/) (for pronunciation, optional)
* [Festival](http://www.cstr.ed.ac.uk/projects/festival/) (for pronunciation, optional)
* [ALSA](https://www.alsa-project.org/) (for pronunciation, optional)

```
$ sudo apt-get install libxml2-dev libxslt-dev python-dev espeak festival alsa-base alsa-utils
```

### Tips
```
$ alias t="python2 /path/to/the/translate.py"
$ alias te="t -p=espeak"
$ alias tf="t -p=festival"
$ alias tr="t -p=real"
$ alias tb="t -s=bing"
$ alias ty="t -s=youdao"
$ alias ti="t -s=iciba"
```

### External Resources
* [SCOWL (Spell Checker Oriented Word Lists)](http://wordlist.aspell.net/)
* [List of spell checkers](http://www.dmoz.org/Arts/Writers_Resources/Software/Spelling_and_Grammar/Spell_Checkers)
* [Wiktionary:Frequency lists](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists)
* [wordlist.10000](http://www.mit.edu/~ecprice/wordlist.10000)
* [top10000en.txt](http://wortschatz.uni-leipzig.de/Papers/top10000en.txt)
* [google-10000-english](https://github.com/first20hours/google-10000-english)

### Changelog
v0.1.3
---
Aug 4, 2017
* Added support for RealPeopleTTS

v0.1.2
---
Jul 31, 2017

* Change option: "webonly" will be enabled while "service" is given
* Update vocabulary.db and spell-checker word lists

v0.1.1
---
Sep 11, 2016

* Optimized options & arguments
* Added support for festival TTS server

v0.1.0
---
Sep 9, 2016

* Initial release
