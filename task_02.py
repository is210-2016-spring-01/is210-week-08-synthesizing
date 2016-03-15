#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Alarm Clock BZZZZZ"""

DAY = raw_input('What day is today?: ').strip().lower()[:3]
TIME = int(raw_input('What time is it now?: '))

SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < 600 else False

if not SNOOZE:
    print ('Beep! '*5).strip()
