#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week-08 Synthesizing Tasks"""

import sys

inputday = raw_input("What day is it?:")
try:
    inputtime = int(raw_input("What time is it?:"))
except ValueError:
    print("Invalid input")
    sys.exit(0)

if inputday != 'Sat' and inputday != 'Sun' and inputtime > 600:
    SNOOZE = False
else:
    SNOOZE = True

if SNOOZE == False:
    print "Beep! Beep! Beep! Beep! Beep!"
