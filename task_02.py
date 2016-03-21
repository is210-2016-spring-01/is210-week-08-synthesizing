#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 Module"""

DAY = str(raw_input('What day is it?: ')).lower()
TIME = int(raw_input('What time is it?: '))
SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < 600 else False

if SNOOZE is False:
    print 'Beep! Beep! Beep! Beep!'

else:
    pass
