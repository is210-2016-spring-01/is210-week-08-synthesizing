#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 2 file."""

DAY = raw_input('What day is it?: ')
DAY = DAY[:3]
DAY = DAY.lower()

TIME = raw_input('What time is it?(in a 4 digit format): ')
TIME = int(TIME)

SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < 600 else False

if SNOOZE is False:
    print 'Beep! Beep! Beep! Beep! Beep!'
