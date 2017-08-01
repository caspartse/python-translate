#!/usr/bin/env python
# -*- coding:utf-8 -*
import dbm
import codecs

db = dbm.open('./vocabulary', 'r')
vDict = db.keys()
vList = sorted(vDict)

print len(vList)

with codecs.open('vocabulary.list', 'w') as f:
    f.write('\n'.join(vList))
