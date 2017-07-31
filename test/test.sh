#!/bin/bash
sort testwords.txt | uniq | xargs -I {} sh -c 'echo {} && python2 ../translate.py {} -n && echo'
sort testwords.txt | uniq | xargs -I {} sh -c 'echo {} && python2 ../translate.py {} -n -s=bing && echo'
sort testwords.txt | uniq | xargs -I {} sh -c 'echo {} && python2 ../translate.py {} -n -s=youdao && echo'
sort testwords.txt | uniq | xargs -I {} sh -c 'echo {} && python2 ../translate.py {} -n -s=iciba && echo'
