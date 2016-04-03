#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Show me the money!"""

import decimal

NAME = raw_input('What is your name? ')

PRINC = int(raw_input('What is the amount of your principal? '))

YEARS = int(raw_input('For how many years is this loan being borrowed? '))

PREQUAL = raw_input('Are you pre-qualidied for this loan? ')

RATE = None

TOTAL = None

if 0 <= PRINC and PRINC <= 199999:
    if 1 <= YEARS and YEARS <= 15:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0363'
        elif PREQUAL == 'No' or PREQUAL == 'n':
            RATE = '0.0465'
    elif 16 <= YEARS and YEARS <= 20:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0404'
        elif PREQUAL == 'No' or PREQUAL == 'n':
            RATE = '0.0498'
    elif 21 <= YEARS and YEARS <= 30:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0577'
        elif PREQUAL == 'No' or PREQUAL == 'n':
            RATE = '0.0639'
elif 200000 <= PRINC and PRINC <= 999999:
    if 1 <= YEARS and YEARS <= 15:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0302'
        elif PREQUAL == 'No' or PREQUAL == 'n':
            RATE = '0.0398'
    elif 16 <= YEARS and YEARS <= 20:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0327'
        elif PREQUAL == 'No' or PREQUAL == 'n':
            RATE = '0.0408'
    elif 21 <= YEARS and YEARS <= 30:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0466'
elif 1000000 <= PRINC:
    if 1 <= YEARS and YEARS <= 15:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0205'
    elif 16 <= YEARS and YEARS <= 20:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0262'
N = 12
if RATE is not None:
    RATE = decimal.Decimal(RATE)
    TOTAL = int(round(PRINC * (1 + RATE/N)**(N*YEARS)))
else:
    TOTAL = None

print ''
print 'Loan Report For: {}'.format(NAME)
print '-------------------------------------------'
print '      Principle:{:>15}'.format(PRINC)
print '      Duration:{:>13}'.format(YEARS)+'yrs'
print '      Pre-qualified?:{:>10}'.format(PREQUAL)
print ''
if TOTAL is not None:
    print '      Total:{:>19.0f}'.format(TOTAL)
else:
    print '      Total:{:>20}'.format(None)

