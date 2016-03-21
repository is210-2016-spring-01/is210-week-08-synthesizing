#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02: Build a simple alarm clock with snooze function"""


DAY = raw_input("What day is it? ")
TIME = int(raw_input("What time is it (as a four digit number)? "))

if len(DAY) >= 3:
    DAY = DAY.lower()
    DAY = DAY[0:3]


SUNDAY = DAY == 'sun'
SATURDAY = DAY == 'sat'

SNOOZE = True if SATURDAY else False
SNOOZE = True if SUNDAY else False

WEEKEND = DAY == 'sun' or DAY == 'sat'
NIGHTTIME = TIME < 0600 or TIME < 600

SNOOZE = True if WEEKEND or NIGHTTIME else False
    
if SNOOZE is False:
    TIME >= 600
    ALARM = "Beep! " * 5
    print ALARM


