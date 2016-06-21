#!/usr/bin/python

import os
import random
from sys import argv
from sys import exit as sysex

from lxml import etree
import requests


_max_index = 1142

def get_banek(index):
    req = requests.get('http://baneks.ru/' + str(index))
    req.encoding = 'utf-8'

    parser = etree.HTMLParser()
    root = etree.fromstring(req.text, parser)
    li = root.xpath("//meta[@name='description']")

    if len(li) == 0:
        return 'Banek not found'
    return li[0].attrib['content']

def main():
    if len(argv) == 1:
        num = random.randint(1,_max_index)
    elif argv[1].isdecimal():
        num = int(argv[1])
    else:
        print("        --USAGE--              ")
        print("banek     -- print random banek")
        print("banek NUM -- print banek #NUM")
        sysex(0)
    print(get_banek(num))

if __name__ == '__main__':
    main()
