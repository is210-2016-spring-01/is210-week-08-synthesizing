#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Loans are great for students!!"""

from decimal import Decimal

NAME = raw_input('What is your name? ')
LOAN = raw_input('What is the principal of the loan? ')
YEARS = raw_input('How many years is this loan being borrowed? ')
QUALIFIED = raw_input('Are you pre-qualified for this loan? ')

LOAN = int(LOAN)
YEARS = int(YEARS)
RATE = None
TOTAL = None
N = 12

if 0 < LOAN <= 199999:
    if 0 < YEARS <= 15:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0363'
        else:
            RATE = '0.0465'
    elif 16 <= YEARS <= 20:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0404'
        else:
            RATE = '0.0498'
    elif 21 <= YEARS <= 30:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0577'
        else:
            RATE = '0.0639'
elif 200000 <= LOAN <= 999999:
    if YEARS <= 15:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0302'
        else:
            RATE = '0.0398'
    elif 16 <= YEARS <= 20:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0327'
        else:
            RATE = '0.0408'
    elif 21 <= YEARS <= 30:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0466'
elif LOAN >= 1000000:
    if YEARS <= 15:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0205'
    elif 16 <= YEARS <= 20:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            RATE = '0.0262'

REPORT = ('Loan report for: ' + NAME + ' \n'
          + '-------------------------------------------------' + '\n'
          + '       Principal:      ' + str(LOAN).rjust(11) + '\n'
          + '       Duration:       ' + str(YEARS).rjust(11) + '\n'
          + '       Pre-Qualified?: ' + QUALIFIED.rjust(11) + '\n'
          + '\n')
if RATE is not None:
    DEC = Decimal(RATE)
    TOTAL = int(round(LOAN * (1 + DEC/N)**(N*YEARS)))
    LOAN = '${:0,d}'.format(LOAN)
    STOTAL = None if TOTAL < 0 else '${:0,d}'.format(TOTAL)
    REPORT += '       Total:          ' + STOTAL.rjust(11)

print REPORT