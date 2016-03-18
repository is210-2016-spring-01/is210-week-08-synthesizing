#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring to calculate the lifetime interest of a loan."""

import decimal

NAME = raw_input('What is your name? ')

PRINCIPAL = int(raw_input('What is the amount of your principal? '))

DURATION = int(raw_input('For how many years is this loan being borrowed? '))

PRE_QUALIFIED = raw_input('Are you pre-qualified for this loan? ')

RATE = None

TOTAL = None

if 0 <= PRINCIPAL and PRINCIPAL <= 199999:
    if 1 <= DURATION and DURATION <= 15:
        if PRE_QUALIFIED == 'Yes' or PRE_QUALIFIED == 'y':
            RATE = '0.0363'
        elif PRE_QUALIFIED == 'No' or PRE_QUALIFIED == 'n':
            RATE = '0.0465'
    elif 16 <= DURATION and DURATION <= 20:
        if PRE_QUALIFIED == 'Yes' or PRE_QUALIFIED == 'y':
            RATE = '0.0404'
        elif PRE_QUALIFIED == 'No' or PRE_QUALIFIED == 'n':
            RATE = '0.0498'
    elif 21 <= DURATION and DURATION <= 30:
        if PRE_QUALIFIED == 'Yes' or PRE_QUALIFIED == 'y':
            RATE = '0.0577'
        elif PRE_QUALIFIED == 'No'or PRE_QUALIFIED == 'n':
            RATE = '0.0639'
elif 200000 <= PRINCIPAL and PRINCIPAL <= 999999:
    if 1 <= DURATION and DURATION <= 15:
        if PRE_QUALIFIED == 'Yes' or PRE_QUALIFIED == 'y':
            RATE = '0.0302'
        elif PRE_QUALIFIED == 'No' or PRE_QUALIFIED == 'n':
            RATE = '0.0398'
    elif 16 <= DURATION and DURATION <= 20:
        if PRE_QUALIFIED == 'Yes' or PRE_QUALIFIED == 'y':
            RATE = '0.0327'
        elif PRE_QUALIFIED == 'No' or PRE_QUALIFIED == 'n':
            RATE = '0.0408'
    elif 21 <= DURATION and DURATION <= 30:
        if PRE_QUALIFIED == 'Yes' or PRE_QUALIFIED == 'y':
            RATE = '0.0466'
elif 1000000 <= PRINCIPAL:
    if 1 <= DURATION and DURATION <= 15:
        if PRE_QUALIFIED == 'Yes' or PRE_QUALIFIED == 'y':
            RATE = '0.0205'
    elif 16 <= DURATION and DURATION <= 20:
        if PRE_QUALIFIED == 'Yes' or PRE_QUALIFIED == 'y':
            RATE = '0.0262'
N = 12
if RATE is not None:
    RATE = decimal.Decimal(RATE)
    TOTAL = int(round(PRINCIPAL * (1 + RATE/N)**(N*DURATION)))
else:
    TOTAL = None

print ''
print 'Loan Report For: {}'.format(NAME)
print '---------------------------------------'
print '      Principle:{:>15}'.format(PRINCIPAL)
print '      Duration:{:>13}'.format(DURATION)+'years'
print '      Pre-qualified?:{:>10}'.format(PRE_QUALIFIED)
print''
if TOTAL is not None:
    print '      Total:{:>19.0f}'.format(TOTAL)
else:
    print '      Total:{:>20}'.format(None)
