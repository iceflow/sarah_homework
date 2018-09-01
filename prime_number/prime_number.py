#!/usr/bin/python
# -*- coding: utf8 -*-

def isPrimeNumber(num):
    if num < 2:
        return False

    for i in xrange(num):
        if i < 2:
            continue
        else:
            if num%i == 0:
                return False

    return True

for i in xrange(10000):
    if isPrimeNumber(i+1):
        print i+1,
