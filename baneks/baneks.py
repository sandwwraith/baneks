#!/usr/bin/python

import os
from sys import argv
from sys import exit as sysex

from lxml import etree
import requests
from html2text import html2text

def get_banek(addr):
    req = requests.get('http://baneks.ru/' + addr)
    req.encoding = 'utf-8'

    parser = etree.HTMLParser()
    root = etree.fromstring(req.text, parser)
    li = root.xpath("//section[@class='anek-view']")
    text = etree.tostring(li[0].find('article'))

    if len(li) == 0:
        return 'Banek not found'
    return html2text(text.decode()).replace("\\-", "-")

def main():
    if len(argv) == 1:
        num = 'random'
    elif argv[1].isdecimal():
        num = argv[1]
    else:
        print("        --USAGE--              ")
        print("banek     -- print random banek")
        print("banek NUM -- print banek #NUM")
        sysex(0)
    print(get_banek(num))

if __name__ == '__main__':
    main()
