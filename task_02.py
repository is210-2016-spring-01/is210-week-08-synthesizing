#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Second task for this week"""

DAY = raw_input('What day is it? ')
TIME = raw_input('What time to start alarm? ')
TIME = int(TIME)

SNOOZE = True if DAY == 'Sat' or DAY == 'Sun' or TIME < 600 else False

if SNOOZE is False:
    print 'Beep! Beep! Beep! Beep! Beep! Beep!'
