#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03"""


import decimal
# A=P(1+\frac{r}{n})^{nt}

NAME = raw_input("What is your name? ")
PRINCIPAL = int(raw_input(
    "What is the amount of your principal (the amount being borrowed)? "))
DURATION = int(raw_input("For how many years is this loan being borrowed? "))
PREQUALIFIED = raw_input("Are you pre-qualified for this loan? ")

if PRINCIPAL > 0 and PRINCIPAL < 200000:
    if DURATION > 1 and DURATION <= 15:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 3.63
        if PREQUALIFIED == "No" or PREQUALIFIED == "n":
            INTEREST = 4.65
    if DURATION > 15 and DURATION <= 20:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 4.04
        if PREQUALIFIED == "No" or PREQUALIFIED == "n":
            INTEREST = 4.98
    if DURATION > 20 and DURATION <= 30:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 5.77
        if PREQUALIFIED == "No" or PREQUALIFIED == "n":
            INTEREST = 6.39
if PRINCIPAL >= 200000 and PRINCIPAL <= 999999:
    if DURATION > 1 and DURATION <= 15:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 3.02
        if PREQUALIFIED == "No" or PREQUALIFIED == "n":
            INTEREST = 3.98
    if DURATION > 15 and DURATION <= 20:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 3.27
        if PREQUALIFIED == "No" or PREQUALIFIED == "n":
            INTEREST = 4.08
    if DURATION > 20 and DURATION <= 30:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 4.66
if PRINCIPAL > 1000000:
    if DURATION > 1 and DURATION <= 15:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 2.05
    if DURATION > 15 and DURATION <= 20:
        if PREQUALIFIED == "Yes" or PREQUALIFIED == "y":
            INTEREST = 2.62
else:
    TOTAL = None


# A=P(1+\frac{r}{n})^{nt}
P = PRINCIPAL
r = INTEREST
n = 12
t = DURATION

TOTAL = P(1+(r)/(n)) ** (nt)
print round(TOTAL)

REPORT = ("Loan Report for: {}\n" +
          "----------------------------------------------\n"
          + "    Principal: ${}\n" + "    Duration: {}yrs\n" +
          "    Pre-Qualified?: {}\n\n" +
          "    Total: ${}").format(NAME, PRINCIPAL,
                               DURATION, PREQUALIFIED, TOTAL)

print REPORT
