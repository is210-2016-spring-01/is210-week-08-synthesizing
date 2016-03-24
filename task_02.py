#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 2 docstring."""


QUESTION1 = raw_input('What day is it?: ')
QUESTION1 = QUESTION1[:3].lower()
QUESTION2 = int(raw_input('What time is it?: '))

SNOOZE = (True if QUESTION1 == 'sat' or QUESTION1 == 'sun' or QUESTION2 < 600
          else 'Beep! ' * 5)

print SNOOZE
