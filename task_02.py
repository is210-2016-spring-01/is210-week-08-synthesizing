#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 2 docstring."""


QUESTION1 = raw_input('What day is it?: ')
QUESTION1 = QUESTION1[0:3].lower() == 's'
QUESTION2 = int(raw_input('What time is it?: '))

SNOOZE = (True if QUESTION1 or QUESTION2 < 600
          else False)

if SNOOZE is False:
    SNOOZE = 'Beep! Beep! Beep! Beep! Beep!'

print SNOOZE
