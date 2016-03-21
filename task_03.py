#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Loans are great for studens!!"""

import decimal
NAME = raw_input('What is your name? ')
LOAN = raw_input('What is the principal of the loan? ')
YEARS = raw_input('How many years is this loan being borrowed? ')
QUALIFIED = raw_input('Are you pre-qualified for this loan? ')

LOAN = int(LOAN)
YEARS = int(YEARS)
RATE = None
TOTAL = None

if LOAN >= 0 and LOAN <= 199999:
    if YEARS >= 1 and YEARS <= 15:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0363'
        elif QUALIFIED == 'No' or QUALIFIED == 'n':
            RATE = '0.0465'
    elif YEARS >= 16 and YEARS <= 20:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0404'
        elif QUALIFIED == 'No' or QUALIFIED == 'n':
            RATE = '0.0498'
    elif YEARS >= 21 and YEARS <= 30:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0577'
        elif QUALIFIED == 'No' or QUALIFIED == 'n':
            RATE = '0.0639'
elif LOAN >= 200000 and LOAN <= 999999:
    if YEARS >= 1 and YEARS <= 15:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0302'
        elif QUALIFIED == 'No' or QUALIFIED == 'n':
            RATE = '0.0398'
    elif YEARS >= 16 and YEARS <= 20:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0327'
        if QUALIFIED == 'No' or QUALIFIED == 'n':
            RATE = '0.0408'
    elif YEARS >= 21 and YEARS <= 30:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0466'
elif LOAN >= 1000000:
    if YEARS >= 1 and YEARS <= 15:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0205'
    elif YEARS >= 16 and YEARS <= 20:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0262'

N = 12
if RATE is not None:
    RATE = decimal.Decimal(RATE)
    TOTAL = int(round(LOAN * (1 + RATE/N)**(N*YEARS)))
else:
    TOTAL = None

LINE1 = 'Principal:'
LINE2 = 'Duration:'
LINE3 = 'Pre-Qualified?:'
REPORT = ('Loan report for: {0} \n'
          + '-------------------------------------------------' + '\n'
          + '       Principal:      ' + '${1}'.rjust(21) + '\n'
          + '       Duration:             ' + '{2}'.rjust(20) + '\n'
          + '       Pre-Qualified?:        ' + '{3}'.rjust(20) + '\n'
          + '\n'
          + '       Total:                ' + '${4}'.rjust(15))
LOAN = '{:0,d}'.format(LOAN)
TOTAL = '{:0,d}'.format(TOTAL)
LOAN = str(LOAN)
TOTAL = str(TOTAL)

print REPORT.format(NAME, LOAN, YEARS, QUALIFIED, TOTAL)
