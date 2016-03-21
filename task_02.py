#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple alarm clock with snooze."""

DAY = raw_input('What day is it? ')
TIME = int(raw_input('What time is it? '))
DAY = DAY.lower()[:3]
if DAY == 'sat' or DAY == 'sun' or (TIME < 0600)is True:
    SNOOZE = True
else:
    SNOOZE = False
    print 'Beep! ' * 5
