#!/usr/bin/python
# -*- coding: utf-8 -*-
#这是一个注释的练习
#
#
#
#
#itervalues  直接去value值 eg 求平均值
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for v in d.itervalues():
    sum +=v
print sum
print sum/len(d)

#dict