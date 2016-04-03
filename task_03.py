#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 3 docstring."""


import decimal


NAME = raw_input('What is your name? ')
PRINCIPAL = int(raw_input('What is the amount of your principal (the amount '
                          'being borrowed)? '))
YEARS = int(raw_input('For how many years is this loan being borrowed? '))
QUALIFIED = raw_input('Are you pre-qualified for this loan? ')
PREQUALIFIED_BOOL = QUALIFIED[:1].lower() == 'y'

INTEREST = None
if PRINCIPAL > 0 and PRINCIPAL < 200000:
    if YEARS > 0 and YEARS <= 15:
        if PREQUALIFIED_BOOL:
            INTEREST = '0.0363'
        else:
            INTEREST = '0.0465'
    elif YEARS > 15 and YEARS <= 20:
        if PREQUALIFIED_BOOL:
            INTEREST = '0.0404'
        else:
            INTEREST = '0.0498'
    elif YEARS > 20 and YEARS <= 30:
        if PREQUALIFIED_BOOL:
            INTEREST = '0.0577'
        else:
            INTEREST = '0.0639'
if PRINCIPAL >= 200000 and PRINCIPAL <= 999999:
    if YEARS > 0 and YEARS <= 15:
        if PREQUALIFIED_BOOL:
            INTEREST = '0.0302'
        else:
            INTEREST = '0.0398'
    elif YEARS > 15 and YEARS <= 20:
        if PREQUALIFIED_BOOL:
            INTEREST = '0.0327'
        else:
            INTEREST = '0.0408'
    elif YEARS > 20 and YEARS <= 30:
        if PREQUALIFIED_BOOL:
            INTEREST = '0.0466'
if PRINCIPAL >= 1000000:
    if YEARS > 0 and YEARS <= 15:
        if PREQUALIFIED_BOOL:
            INTEREST = '0.0205'
    elif YEARS > 15 and YEARS <= 20:
        if PREQUALIFIED_BOOL:
            INTEREST = '0.0262'

if INTEREST:
    DEC_INTEREST = decimal.Decimal(INTEREST)
    TOTAL = PRINCIPAL * ((1 + DEC_INTEREST/12)**(12 * YEARS))
    TOTAL = int(round(TOTAL))
else:
    TOTAL = None

REPORT = 'Loan Report for: {0}\n'
REPORT += '-' * 80 +'\n'
REPORT += '  Principal: {1:>20}\n'
REPORT += '  Duration: {2:>21}\n'
REPORT += '  Pre-qualified?: {3:>15}\n\n'
REPORT += '  Total: {4:>24}\n'
REPORT = REPORT.format(NAME, PRINCIPAL, YEARS, QUALIFIED, TOTAL)

print REPORT
