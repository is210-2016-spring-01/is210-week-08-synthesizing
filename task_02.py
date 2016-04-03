#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 8 synthesizing task 2 that emulates an alarm clock"""

DAYS_LIST = ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY',
             'SUNDAY')


def day_found(dayname):
    """ Check the given day name against the defined list to see if valid

    ARGS:
        dayname (string): Name given for the day of week.

    RETURNS:
        string: The matching full name of the day of the week or None if not
                found

    EXAMPLES:
        >>> day_found('T')
        'TUESDAY'

        >>> day_found('WED')
        'WDNESDAY'

        >>> day_found('SU')
        'SUNDAY'

        >>> day_found('WEDS')
        None

        >>> day_found('DAY')
        None
    """

    for dow in DAYS_LIST:
        if dayname == dow[0:len(dayname)]:
            return dow

    return None

DAY_OKAY = False

while not DAY_OKAY:

    DAY_GIVEN = raw_input('Enter the day: ').upper()
    DAY_MATCH = day_found(DAY_GIVEN)

    if len(DAY_GIVEN) < 2 or not DAY_MATCH:
        print 'That is not a recognised day name'
    else:
        DAY_GIVEN = DAY_MATCH[0:3]
        DAY_OKAY = True

TIME24 = int(raw_input('Enter time of day as 24 hour time: '))

SNOOZE = True if DAY_GIVEN in ('SAT', 'SUN') or TIME24 < 600 else False

if not SNOOZE:
    print 'Beep! ' * 5
