#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple alarm clock with snooze."""

DAY = raw_input('What day is it? ')
TIME = int(raw_input('What time is it? '))
SNOOZE = (DAY.lower()[:3] == 'sat' or 'sun') or TIME < 600
if SNOOZE == False:
    print 'Beep' * 5

