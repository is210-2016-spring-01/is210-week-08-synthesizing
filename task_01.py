#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a color output"""

BASE = raw_input('Which base color, \"Seattle Gray\" or \"Manatee\"?: ')
ACCENT = ''
HIGHLIGHT = ''
COLORS = 'Your selected colors are, {0}, {1}, and {2}.'

if BASE == 'Seattle Gray':
    ACCENT = raw_input('Which accent color,'
                       '\"Ceramic Glaze\" or \"Cumulus Nimbus\"?: ')
    if ACCENT == 'Ceramic Glaze':
        HIGHLIGHT = raw_input('Which highlight color,'
                              '\"Fractal White\" or \"Not White\": ')
    elif ACCENT == 'Cumulus Nimbus':
        HIGHLIGHT = raw_input('Which highlight color,'
                              '\"Off-White\" or \"Paper White\": ')
    else:
        pass
elif BASE == 'Manatee':
    ACCENT = raw_input('Which accent color, '
                       '\"Platinum Mist\" or \"Spartan Sage\"?: ')
    if ACCENT == 'Platinum Mist':
        HIGHLIGHT = raw_input('Which highlight color,'
                              '\"Bone White\" or \"Just White\": ')
    elif ACCENT == 'Spartan Sage':
        HIGHLIGHT = raw_input('Which highlight color,'
                              '\"Fractal White\" or \"Not White\": ')
    else:
        pass

print COLORS.format(BASE, ACCENT, HIGHLIGHT)
