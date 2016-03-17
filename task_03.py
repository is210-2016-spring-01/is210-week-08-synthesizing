#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compounding interest calculator."""

import decimal as dec

CUSTNAME = str(raw_input('What is your name? '))
BORROWED = int(raw_input('What is the principal amount? '))
LOANYEARS = int(raw_input('For how many years is this being borrowed? '))
PREQUAL = str(raw_input('Are you pre-qualified? '))
APR = 0
TOTAL = 0
TITLE = 'Loan Report for: ' + CUSTNAME + '\n' + ('-' * 35)
INDENT = ' ' * 4
REPORT = ''

if 0 < BORROWED <= 199999:
    if LOANYEARS <= 15:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = '.0363'
        else:
            APR = '.0465'
    elif 16 <= LOANYEARS <= 20:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = '.0404'
        else:
            APR = '.0498'
    elif 21 <= LOANYEARS <= 30:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = '.0577'
        else:
            APR = '.0639'
    else:
        pass
elif 200000 <= BORROWED <= 999999:
    if LOANYEARS <= 15:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = '.0302'
        else:
            APR = '.0398'
    elif 16 <= LOANYEARS <= 20:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = '.0327'
        else:
            APR = '.0408'
    elif 21 <= LOANYEARS <= 30:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = '.0466'
        else:
            APR = None
    else:
        TOTAL = None
elif BORROWED >= 1000000:
    if LOANYEARS <= 15:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = '.0205'
        else:
            APR = None
    elif 16 <= LOANYEARS <= 20:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = '.0262'
        else:
            APR = None
    else:
        APR = None
else:
    APR = None

if APR is not None:
    APR = dec.Decimal(APR)
    TOTAL = int(round(BORROWED * (1 + APR / 12) ** (12 * LOANYEARS)))
else:
    TOTAL = None

BORROWED = '${:,}'.format(BORROWED)
REPORT = TITLE + '\n'
REPORT += INDENT + 'Principal:' + '{:>15}'.format(BORROWED) + '\n'
REPORT += INDENT + 'Duration:' + '{:>13}'.format(LOANYEARS) + 'yrs \n'
REPORT += INDENT + 'Pre-qualified?:' + '{:>8}'.format(PREQUAL) + '\n\n'

if TOTAL is not None:
    REPORT += INDENT + 'Total:' + '{:>19}'.format('${:,}'.format(TOTAL))
else:
    REPORT += INDENT + 'Total:' + '{:>19}'.format('None')
print REPORT
