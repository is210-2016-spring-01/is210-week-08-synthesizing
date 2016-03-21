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
            RATE = decimal.Decimal(3.63) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
        elif PREQUALIFIED == "No" or PREQUALIFIED == "n":
            RATE = decimal.Decimal(4.65) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
    elif DURATION > 15 and DURATION <= 20:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            RATE = decimal.Decimal(4.04) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
        elif PREQUALIFIED == "No" or PREQUALIFIED == "n":
            RATE = decimal.Decimal(4.98) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
    elif DURATION > 20 and DURATION <= 30:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            RATE = decimal.Decimal(5.77) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
        elif PREQUALIFIED == "No" or PREQUALIFIED == "n":
            RATE = decimal.Decimal(6.39) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
elif PRINCIPAL >= 200000 and PRINCIPAL <= 999999:
    if DURATION > 1 and DURATION <= 15:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            RATE = decimal.Decimal(3.02) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
        elif PREQUALIFIED == "No" or PREQUALIFIED == "n":
            RATE = decimal.Decimal(3.98) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
    elif DURATION > 15 and DURATION <= 20:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            RATE = decimal.Decimal(3.27) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
        elif PREQUALIFIED == "No" or PREQUALIFIED == "n":
            RATE = decimal.Decimal(4.08) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
    elif DURATION > 20 and DURATION <= 30:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            RATE = decimal.Decimal(4.66) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
elif PRINCIPAL > 1000000:
    if DURATION > 1 and DURATION <= 15:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            RATE = decimal.Decimal(2.05) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
    elif DURATION > 15 and DURATION <= 20:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            RATE = decimal.Decimal(2.62) / 100
            TOTAL = int(round(PRINCIPAL * ((1 + (RATE / 12)) ** (
                12 * DURATION))))
else:
    TOTAL = None


REPORT = ("Loan Report for: {}\n" +
          "----------------------------------------------\n"
          + "    Principal: ${}\n" + "    Duration: {}yrs\n"
          "    Pre-Qualified?: {}\n\n" +
          "    Total: ${}").format(NAME, PRINCIPAL,
                                   DURATION, PREQUALIFIED, TOTAL)

print REPORT
