#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: mortgage calculator to calculate the
lifetime compound interest of a loan."""


import decimal

NAME = raw_input("What is your name? ")
PRINCIPAL = int(raw_input(
    "What is the amount of your principal (the amount being borrowed)? "))
DURATION = int(raw_input("For how many years is this loan being borrowed? "))
PREQUALIFIED = raw_input("Are you pre-qualified for this loan? ")

if PRINCIPAL > 0 and PRINCIPAL < 200000:
    if DURATION > 1 and DURATION <= 15:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 3.63
        elif PREQUALIFIED == "No" or PREQUALIFIED == "n":
            INTEREST = 4.65
    elif DURATION > 15 and DURATION <= 20:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 4.04
        elif PREQUALIFIED == "No" or PREQUALIFIED == "n":
            INTEREST = 4.98
    elif DURATION > 20 and DURATION <= 30:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 5.77
        elif PREQUALIFIED == "No" or PREQUALIFIED == "n":
            INTEREST = 6.39
elif PRINCIPAL >= 200000 and PRINCIPAL <= 999999:
    if DURATION > 1 and DURATION <= 15:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 3.02
        elif PREQUALIFIED == "No" or PREQUALIFIED == "n":
            INTEREST = 3.98
    elif DURATION > 15 and DURATION <= 20:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 3.27
        elif PREQUALIFIED == "No" or PREQUALIFIED == "n":
            INTEREST = 4.08
    elif DURATION > 20 and DURATION <= 30:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 4.66
elif PRINCIPAL > 1000000:
    if DURATION > 1 and DURATION <= 15:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 2.05
    elif DURATION > 15 and DURATION <= 20:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 2.62
else:
    TOTAL = None

INTEREST = decimal.Decimal(INTEREST)
TOTAL = round(PRINCIPAL * (1 + (INTEREST / 12)) ** (12 * DURATION))

print INTEREST

REPORT = ("Loan Report for: {}\n" +
          "----------------------------------------------\n"
          + "    Principal: ${}\n" + "    Duration: {}yrs\n" +
          "    Pre-Qualified?: {}\n\n" +
          "    Total: ${}").format(NAME, PRINCIPAL,
                                   DURATION, PREQUALIFIED, TOTAL)

print REPORT
