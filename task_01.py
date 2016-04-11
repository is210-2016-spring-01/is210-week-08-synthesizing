#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Chosing base, accent, and highlight paint colors"""

BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"?: ')

if BASE == 'Seattle Gray':
    ACCENT = raw_input('Which accent color, "Ceramic  Glaze" or'
                       '"Cumulus Nimbus"?: ')
    if ACCENT == 'Ceramic Glaze':
        HIGHLIGHT = raw_input('Which highlight color,'
                              '"Basically White" or "White"?: ')
    else:
        HIGHLIGHT = raw_input('Which highlight color, '
                              '"Off-White" or "Paper White"?: ')
else:
    ACCENT = raw_input('Which accent color, '
                       '"Platinum Mist" or "Spartan Sage"?: ')
    if ACCENT == 'Platinum Mist':
        HIGHLIGHT = raw_input('Which highlight color, '
                              '"Bone White" or "Just White"?: ')
    else:
        HIGHLIGHT = raw_input('Which highlight color, '
                              '"Fractical White" or "Not White"?: ')

COLORS = 'Your selected colors are, {}, {}, and {}.'
SELECTION = COLORS.format(BASE, ACCENT, HIGHLIGHT)
