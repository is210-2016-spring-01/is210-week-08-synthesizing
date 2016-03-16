#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compounding interest calculator."""

import decimal as dec

CUSTNAME = str(raw_input('What is your name? '))
BORROWED = int(raw_input('What is the principal amount? '))
LOANYEARS = int(raw_input('For how many years is this being borrowed? '))
PREQUAL = str(raw_input('Are you pre-qualified? '))
APR = dec.Decimal(0.0)
TOTAL = int()
TITLE = 'Loan Report for: ' + CUSTNAME + '\n' + ('-' * 35)
INDENT = ' ' * 4
REPORT = ''

if BORROWED <= 199999:
    if LOANYEARS <= 15:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = dec.Decimal(.0363)
        else:
            APR = dec.Decimal(.0465)
    elif 16 <= LOANYEARS <= 20:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = dec.Decimal(.0404)
        else:
            print bool(PREQUAL)
            APR = dec.Decimal(.0498)
    elif 21 <= LOANYEARS <= 30:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = dec.Decimal(.0577)
        else:
            APR = dec.Decimal(.0639)
    else:
        pass
elif 200000 <= BORROWED <= 9999999:
    if LOANYEARS <= 15:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = dec.Decimal(.0302)
        else:
            APR = dec.Decimal(.0398)
    elif 16 <= LOANYEARS <= 20:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = dec.Decimal(.0327)
        else:
            APR = dec.Decimal(.0408)
    elif 21 <= LOANYEARS <= 30:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = dec.Decimal(.0466)
        else:
            TOTAL = None
    else:
        TOTAL = None
elif BORROWED <= 1000000:
    if LOANYEARS <= 15:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = dec.Decimal(.0205)
        else:
            TOTAL = None
    elif 16 <= LOANYEARS <= 20:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            APR = dec.Decimal(.0262)
        else:
            TOTAL = None
    else:
        TOTAL = None
else:
    TOTAL = None

TOTAL = int(round((BORROWED * ((1 + APR / 12) ** (12 * LOANYEARS)))))
BORROWED = '${:,}'.format(BORROWED)
TOTAL = '${:,}'.format(TOTAL)
REPORT = TITLE + '\n'
REPORT += INDENT + 'Principal:' + '{:>15}'.format(BORROWED) + '\n'
REPORT += INDENT + 'Duration:' + '{:>13}'.format(LOANYEARS) + 'yrs \n'
REPORT += INDENT + 'Pre-qualified?:' + '{:>8}'.format(PREQUAL) + '\n\n'
REPORT += INDENT + 'Total:' + '{:>19}'.format(TOTAL)

print REPORT
