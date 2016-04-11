#!usr/bin/env python
# -*- codging: utf-8 -*-
"""Creating a mortgage calculator"""

import decimal

NAME = raw_input('What is your name? ')
PRINCIPAL = raw_input('What is the amount of your principal? ')
PRINCIPAL = int(PRINCIPAL)
LOAN_DURATION = raw_input('For how many years is this loan being borrowed? ')
LOAN_DURATION = int(LOAN_DURATION)
QUALIFIED = raw_input('Are you pre-qualified for this loan? ')
QUALIFIED = QUALIFIED[0:1]
COMPOUND = 12

if PRINCIPAL <= 199999:
    
    if LOAN_DURATION <= 15 and QUALIFIED:'yes'
    INTEREST = 0.0363
    QUALIFIED = 'yes'
    if LOAN_DURATION > 15 and LOAN_DURATION <= 20:
        INTEREST = 0.0404
        QUALIFIED = 'yes'
    else:
        INTEREST = 0.0498
        QUALIFIED = 'no'
        if LOAN_DURATION > 20 and LOAN_DURATION <= 30:
            INTEREST = 0.0577
            QUALIFIED = 'yes'
        else:
            INTEREST = 0.639
            QUALIFIED = 'no'
            
elif PRINCIPAL > 200000 and PRINCIPAL <= 999999:
    if LOAN_DURATION <= 15 and QUALIFIED:
        INTEREST = 0.0363
        QUALIFIED = 'yes'
    if LOAN_DURATION > 15 and LOAN_DURATION <= 20:
        INTEREST = 0.0404
        QUALIFIED = 'yes'
    else:
        INTEREST = 0.0498
        QUALIFIED = 'no'
        if LOAN_DURATION > 20 and LOAN_DURATION <= 30:
            INTEREST = 0.0577
            QUALIFIED = 'yes'
        else:
            INTEREST = 0.639
            QUALIFIED = 'no'


else:
    LOAN_DURATION <= 15
    INTEREST = 0.0465
    QUALIFIED = 'no'
       
TOTAL = PRINCIPAL(INTEREST / COMPOUND) ^ (COMPOUND * LOAN_DURATION)

print TOTAL
