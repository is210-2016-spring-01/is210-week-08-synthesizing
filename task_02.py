#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""


DAY = raw_input("What day is it? ")
TIME = raw_input("What time is it? ")

if len(TIME) != 4:
    raise ValueError()
TIME = int(TIME)

if len(DAY) > 3:
    DAY = DAY.lower()
    DAY = DAY[0:3]
if len(DAY) < 3:
    raise ValueError()

WEEKEND = DAY == 'sun' or DAY == 'sat'
NIGHTTIME = TIME < 0600 or TIME < 600

SNOOZE = True if WEEKEND or NIGHTTIME else False

if False:
    ALARM = "BEEP!" * 5
    print ALARM

print SNOOZE
