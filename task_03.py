#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Loans are great for studens!!"""

from decimal import Decimal
NAME = raw_input('What is your name? ')
LOAN = raw_input('What is the principal of the loan? ')
YEARS = raw_input('How many years is this loan being borrowed? ')
QUALIFIED = raw_input('Are you pre-qualified for this loan? ')

LOAN = int(LOAN)
YEARS = int(YEARS)
#RATE = None
#TOTAL = None

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
        elif QUALIFIED == 'No' or QUALIFIED == 'n':
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
elif LOAN <= 0:
    RATE = None
    TOTAL = None
    
Dec = Decimal(RATE)
NRATE = '{0:f}'.format(Dec)
N = 12
if RATE is not None:
    TOTAL = int(round(LOAN * (1 + Decimal(Decimal(NRATE))/N)**(N*YEARS)))
else:
    TOTAL = None
    RATE = None

RATE =Decimal(int(float(RATE)))
TOTAL = int(TOTAL)
LOAN = '{:0,d}'.format(LOAN)
STOTAL = '{:0,d}'.format(TOTAL)

REPORT = ('Loan report for: ' + NAME + ' \n'
          + '-------------------------------------------------' + '\n'
          + '       Principal:      ' + str(LOAN).rjust(21) + '\n'
          + '       Duration:      ' + str(YEARS).rjust(22) + '\n'
          + '       Pre-Qualified?:      ' + QUALIFIED.rjust(16) + '\n'
          + '\n'
          + '       Total:      ' + STOTAL.rjust(25))
print REPORT
# if RATE is not None:
   # RATE = decimal.Decimal(RATE)
   # TOTAL = int(LOAN * (1 + RATE/N)**(N*YEARS))
# else:
    # TOTAL = None

# LINE1 = 'Principal:'
# LINE2 = 'Duration:'
# LINE3 = 'Pre-Qualified?:'
# REPORT = ('Loan report for: {0} \n'
          # + '-------------------------------------------------' + '\n'
          # + '       Principal:      ' + '${1}'.rjust(21) + '\n'
          # + '       Duration:             ' + '{2}'.rjust(20) + '\n'
          # + '       Pre-Qualified?:        ' + '{3}'.rjust(20) + '\n'
          # + '\n'
          # + '       Total:                ' + '${4}'.rjust(15))


# LOAN = '{:0,d}'.format(LOAN)
# STOTAL = '{:0,d}'.format(TOTAL)
#TOTAL = int(TOTAL)
#LOAN = int(LOAN)

# STOTAL = '{:0,d}'.format(TOTAL)
# SLOAN = '{:0,d}'.format(LOAN)

# LOAN = float(LOAN)
# TOTAL = float(TOTAL)
# YEARS = float(YEARS)

#print REPORT.format(NAME, LOAN, YEARS, QUALIFIED, STOTAL)
