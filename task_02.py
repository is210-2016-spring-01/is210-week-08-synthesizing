#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 2 docstring."""


QUESTION1 = raw_input('What day is it?: ').lower()
QUESTION1 = QUESTION1[0:3]
QUESTION2 = raw_input('What time is it?: ')

SNOOZE = (True if (QUESTION1 == 'sat' and 'sun') or QUESTION2 < 600
          else 'Beep! Beep! Beep! Beep! Beep!')
print SNOOZE
