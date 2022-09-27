#!/usr/bin/python3
""" add serialized object to file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

f = 'add_item.json'
a = list(sys.argv)
a.pop(0)
mylist = []
with open(f, 'a') as op:
    pass
with open(f, 'r', encoding='utf-8') as op:
    rd = op.read()
if len(rd) > 0:
    mylist = load_from_json_file(f)
mylist += a
save_to_json_file(mylist, f)
