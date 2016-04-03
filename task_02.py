#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring that shows the time."""

DAY = raw_input('What day is it today?: ').strip().lower()[:3]
TIME = int(raw_input('What time is it now?: '))

SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < 600 else False

if not SNOOZE:
    print ('BEEP! '*5).strip()
