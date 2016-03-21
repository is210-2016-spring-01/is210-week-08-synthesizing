#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Total owned over life of loan."""

import decimal

NAME = raw_input('What is your name? ')
PRIN = int(raw_input('What is the amount of your principal (the amount being'
                     ' borrowed? '))
YEARS = int(raw_input('For how many years is this loan being borrowed? '))
QUAL = raw_input('Are you pre-qualified for this loan? Please answer (Yes or y)'
                 'or (No or n). ')

if PRIN >= 0 and PRIN <= 199999:
    if YEARS >= 1 and YEARS <= 15:
        if QUAL is 'Yes' or QUAL is 'y':
            INTEREST = .0363
        else:
            INTEREST = .0465
    elif YEARS >= 16 and YEARS <= 20:
        if QUAL is 'Yes' or QUAL is 'y':
            INTEREST = .0404
        else:
            INTEREST = .0498
    elif YEARS >= 21 and YEARS <= 30:
        if QUAL is 'Yes' or QUAL is 'y':
            INTEREST = .0577
        else:
            INTEREST = .0639
if PRIN >= 200000 and PRIN <= 999999:
    if YEARS >= 1 and YEARS <= 15:
        if QUAL is 'Yes' or QUAL is 'y':
            INTEREST = .0302
        else:
            INTEREST = .0398
    elif YEARS >= 16 and YEARS <= 20:
        if QUAL is 'Yes' or QUAL is 'y':
            INTEREST = .0327
        else:
            INTEREST = .0408
    elif YEARS >= 21 and YEARS <= 30:
        if QUAL is 'Yes' or QUAL is 'y':
            INTEREST = .0466
if PRIN >= 1000000:
    if QUAL is 'Yes' or QUAL is 'y':
        if YEARS >= 1 and YEARS <= 15:
            INTEREST = .0205
        elif YEARS >= 16 and YEARS <= 20:
            INTEREST = .0398

TOTAL = PRIN *(1 + (decimal.Decimal(INTEREST) / 12)) ** (12 * YEARS)
TOTAL = int(round(TOTAL))

REPORT = ('Loan Report for: {0:>15}\n---------------------------------------'
          '----\nPrincipal: {1:>21,.0f}\nDuration: {2:>19}yrs\n'
          'Pre-qualified?: {3:>16}\n'
          '\nTotal: {4:>25,.0f}').format(NAME, PRIN, YEARS, QUAL, TOTAL)
print REPORT
