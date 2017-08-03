#!/bin/bash
sort testwords.txt | uniq | xargs -I {} sh -c 'echo {} && python2 ../translate.py {} -n && echo'
sort testwords.txt | uniq | xargs -I {} sh -c 'echo {} && python2 ../translate.py {} -n -s=bing && echo'
sort testwords.txt | uniq | xargs -I {} sh -c 'echo {} && python2 ../translate.py {} -n -s=youdao && echo'
sort testwords.txt | uniq | xargs -I {} sh -c 'echo {} && python2 ../translate.py {} -n -s=iciba && echo'
python2 ../translate.py strawberry -p=espeak && sleep 0.5
python2 ../translate.py apple -p=festival && sleep  0.5
python2 ../translate.py orange -p=real
