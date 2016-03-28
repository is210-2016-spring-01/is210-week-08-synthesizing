#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week-08 Synthesizing Tasks"""

name = raw_input("What is your name? ")
principalam = int(raw_input("What is the principal of the loan? "))
dur = int(raw_input("For how long is this being borrowed? "))
prqual = raw_input("Are you pre-qualified?")

rate = 0.0
if prqual == "Yes" or prqual == "y":
    if principalam >= 0 and principalam <= 199999:
        if dur >= 1 and dur <= 15:
            rate = 3.63
        elif dur >= 16 and dur <= 20:
            rate = 4.04
        elif dur >= 21 and dur <= 30:
            rate = 5.77
    elif principalam >= 200000 and principalam <= 999999:
        if dur >= 1 and dur <= 15:
            rate = 3.02
        elif dur >= 16 and dur <= 20:
            rate = 3.27
        elif dur >= 21 and dur <= 30:
            rate = 4.66
    elif principalam >= 1000000:
        if dur >= 1 and dur <= 15:
            rate = 2.05
        elif dur >= 16 and dur <= 20:
            rate = 2.62
else:
    if principalam >= 0 and principalam <= 199999:
        if dur >= 1 and dur <= 15:
            rate = 4.65
        elif dur >= 16 and dur <= 20:
            rate = 4.98
        elif dur >= 21 and dur <= 30:
            rate = 6.39
    elif principalam >= 200000 and principalam <= 999999:
        if dur >= 1 and dur <= 15:
            rate = 3.98
        elif dur >= 16 and dur <= 20:
            rate = 4.08
if rate == 0.0:
    print "Invalid input"
    sys.exit(0)

n = 12
fracrate = rate/100

fact = 1+ fracrate/n

amount = principalam * (fact**(n*dur))

result = "Loan Report for: {0} \n".format(name)
result = result + "-----------------------------------------------\n"
result = result +"Principal:        $ {0} \n".format(principalam)
result = result + "Duration:             {0} yrs\n".format(dur)
result = result + "Pre-qualified?:         {0}\n\n\n".format(prqual)
result = result + "Total:             $ {0}\n".format(amount)

print result
