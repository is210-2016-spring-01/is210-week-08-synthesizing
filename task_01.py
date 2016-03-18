#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 8 synthesizing task 1 that prompts for colors, accents, and
   highlights based on the compatibility table"""

COLOR_SEQUENCE = ('Base', 'Accent', 'Highlight')
COLOR_TABLE = (('Seattle Gray', 'Base', None),
               ('Manatee', 'Base', None),
               ('Ceramic Glaze', 'Accent', 'Seattle Gray'),
               ('Cumulus Nimbus', 'Accent', 'Seattle Gray'),
               ('Platinum Mist', 'Accent', 'Manatee'),
               ('Spartan Sage', 'Accent', 'Manatee'),
               ('Basically White', 'Highlight', 'Ceramic Glaze'),
               ('White', 'Highlight', 'Ceramic Glaze'),
               ('Off-White', 'Highlight', 'Cumulus Nimbus'),
               ('Paper White', 'Highlight', 'Cumulus Nimbus'),
               ('Bone White', 'Highlight', 'Platinum Mist'),
               ('Just White', 'Highlight', 'Platinum Mist'),
               ('Fractal White', 'Highlight', 'Spartan Sage'),
               ('Not White', 'Highlight', 'Spartan Sage'))

COLOR_PROMPT = 'Which {0} color, {1}?:'
COLOR_CHOICES = []


def gen_color_list(ctype, higher_color):
    """ This function returns a tuple of the colors associated with a given
        level and higher level color (None for base level)

    Args:
        ctype (string): The color type of the colors.
        higher_color (string): The name of the color from the higher type
                                level these colors are associated to
                                (Note: for level Base this should be None)

    Returns:
        tuple: The list of colors that are assigned to the type and higher
               level color

    Examples:
        >>> gen_color_list('Base', None)
        ('Seattle Gray', 'Manatee')

        >>> gen_color_list('Accent', 'Seattle Gray')
        ('Ceramic Glaze', 'Cumulus Nimbus')

        >>> gen_color_list('Highlight', 'Platinum Mist')
        ('Fractal White', 'Not White')
    """
    choices = ()

    for centry in COLOR_TABLE:

        if centry[1] == ctype and centry[2] == higher_color:
            choices += (centry[0],)

    return choices


def get_color_choice(ctype, prevchoice):
    """ Prompts for the color choice for the given type and higher color

    Args:
        ctype (string): The color type of the colors.
        prevchoice (string): The name of the color from the higher type
                             level these colors are associated to
                             (Note: for level Base this should be None)

    Returns:
        string: The name of the color chosen

    Examples:
        >>> get_color_choice('Base', None)
        'Seattle Gray'

        >>> get_color_choice('Accent', 'Seattle Gray')
        'Cumulus Nimbus'

        >>> get_color_choice('Highlight', 'Platinum Mist')
        'Not White'
    """

    current_choices = gen_color_list(ctype, prevchoice)
    cprompt = 'Which {} color, {}' + ' or {}' * (len(current_choices)-1) + '?:'
    color_set = False

    while not color_set:
        cchoice = raw_input(cprompt.format(ctype, *current_choices))

        if cchoice not in current_choices:
            print 'That is not a valid option'
        else:
            color_set = True

    return cchoice

PREV_CHOICE = None

for clevel in COLOR_SEQUENCE:

    PREV_CHOICE = get_color_choice(clevel, PREV_CHOICE)
    COLOR_CHOICES.append(PREV_CHOICE)

print 'Your selected colors are, {0}, {1}, and {2}.'.format(*COLOR_CHOICES)

BASE = COLOR_CHOICES[0]
ACCENT = COLOR_CHOICES[1]
HIGHLIGHT = COLOR_CHOICES[2]
