#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for an alarm clock"""

CURRENTDAY = str(raw_input('What day is it?: ')).lower()
CURRENTTIME = int(raw_input('What time is it?: '))
SNOOZE = (True if ('sat' in CURRENTDAY or 'sun' in CURRENTDAY)
          or (CURRENTTIME < 600) else False)

if SNOOZE is False:
    print 'Beep! Beep! Beep! Beep! Beep!'
else:
    pass
