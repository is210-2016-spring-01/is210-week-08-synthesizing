#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 3 file."""

import decimal

NAME = raw_input('What is your name? ')
PRINCIPLE = int(raw_input('What is the principle of the loan? '))
YEARS = int(raw_input('For how long is this being borrowed? '))
PQUALIFIED = raw_input('Are you prequalified? ')

IR = None
TOTAL = None

if PRINCIPLE >= 0 and PRINCIPLE <= 199999:
    if YEARS >= 1 and YEARS <= 15:
        if PQUALIFIED == ('Yes', 'y'):
            IR = '0.0363'
        elif PQUALIFIED == ('No', 'n'):
            IR = '0.0465'
    elif YEARS >= 16 and YEARS <= 20:
        if PQUALIFIED == ('Yes', 'y'):
            IR = '0.0404'
        elif PQUALIFIED == ('No', 'n'):
            IR = '0.0498'
    elif YEARS >= 21 and YEARS <= 30:
        if PQUALIFIED == ('Yes', 'y'):
            IR = '0.0577'
        elif PQUALIFIED == ('No', 'n'):
            IR = '0.0639'

if PRINCIPLE >= 200000 and PRINCIPLE <= 999999:
    if YEARS >= 1 and YEARS <= 15:
        if PQUALIFIED == ('Yes', 'y'):
            IR = '0.0302'
        elif PQUALIFIED == ('No', 'n'):
            IR = '0.0398'
    elif YEARS >= 16 and YEARS <= 20:
        if PQUALIFIED == ('Yes', 'y'):
            IR = '0.0327'
        elif PQUALIFIED == ('No', 'n'):
            IR = '0.0408'
    elif YEARS >= 21 and YEARS <= 30:
        if PQUALIFIED == ('Yes', 'y'):
            IR = '0.0466'

if PRINCIPLE >= 1000000:
    if YEARS >= 1 and YEARS <= 15:
        if PQUALIFIED == ('Yes', 'y'):
            IR = '0.0205'
    if YEARS >= 16 and YEARS <= 20:
        if PQUALIFIED == ('Yes', 'y'):
            IR = '0.0262'

N = 12

if IR is not None:
    IR = decimal.Decimal(IR)

if TOTAL is not None:
    TOTAL = int(round(PRINCIPLE * (1 + IR/N)**(N*YEARS)))

print ''
print 'Loan Report for: {0}'.format(NAME)
print '-' * 35
print '      Principle:{:>15}'.format(PRINCIPLE)
print '      Duration:{:>16}'.format(YEARS)
print '      Pre-qualified?:{:>10}'.format(PQUALIFIED)
print ''
print '      Total:{:>19}'.format(TOTAL)
