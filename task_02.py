#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple alarm clock with snooze."""

DAY = raw_input('What day is it? ')
TIME = int(raw_input('What time is it? '))
SNOOZE = (DAY.lower()[:3] is 'sat' or 'sun') and TIME < 600

print 'Beep!' * 5 if not SNOOZE else True
