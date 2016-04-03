#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Alarm clock to wake if needed."""

CURRENTDAY = str(raw_input('What day is it?: ')).lower()
CURRENTTIME = int(raw_input('White time is it?: '))
SNOOZE = (True if ('sat' in CURRENTDAY or 'sun' in CURRENTDAY)
          or (CURRENTTIME < 600) else False)

if SNOOZE is False:
    print 'Beep! Beep! Beep! Beep! Beep!'
else:
    pass
