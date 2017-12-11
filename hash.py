#!/usr/bin/python3
# coding=utf-8
def ChangeKey(key, m, di):
    key01 = (key+di)%m
    return key01

a = input("Please entry the numbers:\n").split()
print(a)
m = len(a)
dict01 = {}
for i in a:
    key = int(i)%m
    if "%s" % key in dict01:
        NewKey = ChangeKey(key, m, 1)
        while "%s" % NewKey in dict01:
            NewKey = ChangeKey(NewKey, m, 1)
            while "%s" % NewKey in dict01:
                NewKeey = ChangeKey(NewKey, m, 1)
            dict01["%s" % NewKey] = int(i)
    else:
        dict01["%s" % key] = int(i)
print(dict01)
