#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Second task for this week"""

DAY = raw_input('What day is it? ')
DAY = DAY.strip().lower()[:3]
TIME = int(raw_input('What time to start alarm? '))


SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < 600 else False

if SNOOZE is False:
    print 'Beep! Beep! Beep! Beep! Beep! Beep!'
