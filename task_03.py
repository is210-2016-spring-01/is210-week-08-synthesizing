#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 Module"""

import decimal

CUSTNAME = str(raw_input('What is your name? '))
PRINCIPAL = int(raw_input('What is the amount of your principal? '))
LOANYEAR = int(raw_input('For how many years is this loan borrowed? '))
PREQUAL = raw_input('Are you prequalified for this loan? ')
RATE = 0
TOTAL = 0
LOANREPORT = ''

if 0 < PRINCIPAL <= 199999:
    if LOANYEAR <= 15:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0363'
        else:
            RATE = '0.0465'
    elif 16 <= LOANYEAR <= 20:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0404'
        else:
            RATE = '0.0498'
    elif 21 <= LOANYEAR <= 30:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0577'
        else:
            RATE = '0.0639'
elif 200000 < PRINCIPAL <= 999999:
    if LOANYEAR <= 15:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0302'
        else:
            RATE = '0.0398'
    elif 16 <= LOANYEAR <= 20:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0327'
        else:
            RATE = '0.0408'
    elif 21 <= LOANYEAR <= 30:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0466'
        else:
            RATE = None
elif PRINCIPAL >= 1000000:
    if LOANYEAR <= 15:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0205'
        else:
            RATE = None
    elif 16 <= LOANYEAR <= 20:
        if PREQUAL == 'Yes' or PREQUAL == 'y':
            RATE = '0.0262'
        else:
            RATE = None
    else:
        RATE = None
else:
    RATE = None

if RATE is not None:
    RATE = decimal.Decimal(RATE)
    TOTAL = int(round(PRINCIPAL * (1 + RATE / 12) ** (12 * LOANYEAR)))
else:
    TOTAL = None

LOANREPORT = 'Loan Report for: ' + CUSTNAME + '\n' + ('-' * 70) + '\n'
LOANREPORT += (' ' * 6) + 'Principal:' + '{:>15}'.format('${:,}'.format
                                                         (PRINCIPAL)) + '\n'
LOANREPORT += (' ' * 6) + 'Duration:' + '{:>13}'.format(LOANYEAR) + 'yrs' + '\n'
LOANREPORT += (' ' * 6) + 'Prequalified?:' + '{:>8}'.format(PREQUAL) + '\n\n'

if TOTAL is not None:
    LOANREPORT += (' ' * 6) + 'Total:' + '{:>19}'.format('${:,}'.format(TOTAL))
else:
    LOANREPORT += (' ' * 6) + 'Total:' + '{:>19}'.format('None')

print LOANREPORT
