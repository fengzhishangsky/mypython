#!/usr/bin/python
# -*- coding: utf-8 -*-
#这是一个注释的练习
#
#
#
#
#itervalues  直接去value值 eg 求平均值
# d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

# sum = 0.0
# for v in d.itervalues():
#     sum +=v
# print sum
# print sum/len(d)

#dict item()
#
#
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for k, v in d.items():
    sum = sum + v
    print k, ":", v
print 'average', ':', sum/len(d)


for m, n in d.iteritems():
    sum = sum + n
    print m, ":", n
print 'average', ':', sum/len(d)
