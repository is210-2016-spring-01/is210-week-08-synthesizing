#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 3 file."""

import decimal

NAME = raw_input('What is your name? ')
PRINCIPAL = int(raw_input('What is the principle of the loan? '))
YEARS = int(raw_input('For how long is this being borrowed? '))
PQ = raw_input('Are you prequalified? ')

IR = 0
TOTAL = 0

if 0 <= PRINCIPAL <= 199999:
    if YEARS <= 15:
        if PQ == 'Yes' or PQ == 'y':
            IR = '.0363'
        else:
            IR = '.0465'
    elif 16 <= YEARS <= 20:
        if PQ == 'Yes' or PQ == 'y':
            IR = '.0404'
        else:
            IR = '.0498'
    elif 21 <= YEARS <= 30:
        if PQ == 'Yes' or PQ == 'y':
            IR = '.0577'
        else:
            IR = '.0639'
    else:
        IR = None

elif 200000 <= PRINCIPAL <= 999999:
    if YEARS <= 15:
        if PQ == 'Yes' or PQ == 'y':
            IR = '.0302'
        else:
            IR = '.0398'
    elif 16 <= YEARS <= 20:
        if PQ == 'Yes' or PQ == 'y':
            IR = '.0327'
        else:
            IR = '.0408'
    elif 21 <= YEARS <= 30:
        if PQ == 'Yes' or PQ == 'y':
            IR = '.0466'
        else:
            IR = None
    else:
        IR = None

elif PRINCIPAL >= 1000000:
    if YEARS <= 15:
        if PQ == 'Yes' or PQ == 'y':
            IR = '.0205'
        else:
            IR = None
    elif 16 <= YEARS <= 20:
        if PQ == 'Yes' or PQ == 'y':
            IR = '.0262'
        else:
            IR = None
    else:
        IR = None
else:
    IR = None

if IR is not None:
    IR = decimal.Decimal(IR)
    TOTAL = int(round(PRINCIPAL * (1 + IR / 12) ** (12 * YEARS)))
else:
    TOTAL = None

print ''
print 'Loan Report for: {0}'.format(NAME)
print '-' * 35
print '      Principle:{:>15}'.format(PRINCIPAL)
print '      Duration:{:>16}'.format(YEARS)
print '      Pre-qualified?:{:>10}'.format(PQ)
print ''
if TOTAL is not None:
    print '      Total:{:>19}'.format(TOTAL)
else:
    print '      Total:{:>19}'.format('None')
