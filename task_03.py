#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 8 synthesizing task 3 that will calculate the total amount
   paid over the course of a given loan"""

from decimal import Decimal as Dec

INTEREST_TABLE = ((0, 199999, 1, 15, True, '3.63'),
                  (0, 199999, 1, 15, False, '4.65'),
                  (0, 199999, 16, 20, True, '4.04'),
                  (0, 199999, 16, 20, False, '4.98'),
                  (0, 199999, 21, 30, True, '5.77'),
                  (0, 199999, 21, 30, False, '6.39'),
                  (200000, 999999, 1, 15, True, '3.02'),
                  (200000, 999999, 1, 15, False, '3.98'),
                  (200000, 999999, 16, 20, True, '3.27'),
                  (200000, 999999, 16, 20, False, '4.08'),
                  (200000, 999999, 21, 30, True, '4.66'),
                  (1000000, 0, 1, 15, True, '2.05'),
                  (1000000, 0, 16, 20, True, '2.62'))

REPORT_TEMPLATE = ' Loan Report for: {name}\n ' + \
                  '-' * 40 + '\n' + \
                  '   Principal:    ${pv:,}\n' + \
                  '   Duration:{dur:>8}yrs\n' + \
                  '   Pre-qualified?:{pre:>6}\n\n' + \
                  '   Total:{tot:>14}'


def find_intrate(prin, dur, prequal):
    """ Scans the Interest table and returns the appropriate interest rate for
        the specified principle, duration, and prequalification status.  If no
        matching options are found, None is returned.

    ARGS:
        prin (int): The amount of principle for the loan.
        dur  (int): The duration (in years) for the loan.
        prequal (boolean): Indicates if the person has been prequalified (True)
                           or not (False) for the loan.

    RETURNS:
        decimal: The interest rate for those loan terms, or None if not found.

    EXAMPLE:
        >>> find_intrate(200000, 30, True)
        Decimal('4.66')

        >>> find_intrate(190000, 15, False)
        Decimal('4.65')

        >>> find_intrate(1100000, 20, False)
        None
    """

    for inttab in INTEREST_TABLE:
        minprin, maxprin, mindur, maxdur, preq, intrate = inttab[0:]

        if prin >= minprin and (maxprin == 0 or prin <= maxprin) and \
           dur >= mindur and dur <= maxdur and prequal is preq:
            return Dec(intrate)

    return None


def get_int(prompt):
    """ Prompts for input of an integer (with provided prompt string) and
        verify the input is an integer.

    ARGS:
        prompt (string): The text of the input prompt for the value.

    RETURNS:
        integer: The integer value of the input

    EXAMPLE:
        >>> get_int('Enter an integer: ')
        Enter an integer: abc
        Not a valid and positive integer
        Enter an integer: -42
        Not a valid and positive integer
        Enter an integer: 42.2
        Not a valid and positive integer
        Enter an integer: 42
        42
    """

    validint = False

    while not validint:

        entered = raw_input(prompt)

        if not entered.isdigit() and __name__ == '__main__':
            print 'Not a valid and positive integer'
        else:
            validint = True

    return int(entered)


def get_yn(prompt):
    """ Prompts for input of a Yes or No reply.

    ARGS:
        prompt (string): The text of the input prompt for the value.

    RETURNS:
        string: The responce (YES or NO)

    EXAMPLE:
        >>> get_yn('Enter Yes or No: ')
        Enter Yes or No: nope
        Not a valid response
        Enter an integer: n
        'NO'

        >>> get_yn('Enter Yes or No: ')
        Enter Yes or No: yess
        Not a valid response
        Enter an integer: Ye
        'YES'
    """

    validyn = False
    yorn = ''

    while not validyn:

        resp = raw_input(prompt)
        resplen = len(resp)

        for yorn in ('NO', 'YES'):

            if resplen > 0 and resplen <= len(yorn):

                if resp.upper() == yorn[0:resplen]:
                    validyn = True
                    break
        else:
            print 'Not a valid response'

    return yorn

BORROW_NAME = raw_input('What is your name? ')

LOAN_AMT = get_int('What is the amount of your principal ' +
                   '(the amount being borrowed)? ')

LOAN_DURATION = get_int(' For how many years is this loan being borrowed? ')

LOAN_PREQUALIFIED = True if get_yn('Are you pre-qualified for this loan? ') \
                    == 'YES' else False

INTRATE = find_intrate(LOAN_AMT, LOAN_DURATION, LOAN_PREQUALIFIED)

if INTRATE is None:
    LOAN_TOTAL = TOTAL = None
else:
    INTRATE /= 100
    TOTAL = Dec(round(LOAN_AMT * ((1 + INTRATE / 12) ** (LOAN_DURATION * 12)),
                      0))
    LOAN_TOTAL = '${0:,}'.format(TOTAL)

REPORT = REPORT_TEMPLATE.format(name=BORROW_NAME, pv=LOAN_AMT,
                                dur=LOAN_DURATION,
                                pre='Yes' if LOAN_PREQUALIFIED else 'No',
                                tot=LOAN_TOTAL)
print REPORT
