#!/usr/bin/python
# -*- coding: utf8 -*-

import time


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for n in xrange(100):
    start_time=time.time()
    result=fib(n)
    end_time=time.time()
    print('fib(%2d)=%d: \tDuration(%d)'%(n, result, end_time-start_time))
