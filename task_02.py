#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Creating a snooze function"""

WEEKDAY = raw_input('What day is it?: ')
WEEKDAY = WEEKDAY.lower()
WEEKDAY = WEEKDAY[0:-3]

TIME_IS_IT = raw_input('What time is it? (Use 4 digit without colon):')
TIME_IS_IT = int(TIME_IS_IT)

BEEP = 'Beep! Beep! Beep! Beep! Beep!'

WEEKEND = 'saturday' or 'sunday'

SNOOZE = True if WEEKEND or TIME_IS_IT < 0600 else BEEP

print SNOOZE
