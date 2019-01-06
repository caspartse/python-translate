#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re

sess = requests.Session()
url = 'http://dict.cn/dictionary'
try:
    resp = sess.get(url, allow_redirects=False)
    pattern = ur'<h1 class="keyword" tip="音节划分：([^"]+)">'
    hyphenation = re.search(pattern, resp.text).group(1).replace('&#183;', '-')
    print hyphenation
except Exception, e:
    print e
