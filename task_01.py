#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""All the colors of the world!!"""

BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"?: ')
if BASE == 'Seattle Gray':
    ACCENT = raw_input('Which accent color, '
                       '"Ceramic Glaze" or "Cumulus Nimbus"?: ')
    if ACCENT == 'Ceramic Glaze':
        HIGHLIGHT = raw_input('Which highlight color'
                              ', "Basically White" or "White"?: ')
    elif ACCENT == 'Cumulus Nimbus':
        HIGHLIGHT = raw_input('Which highlight color'
                              ', "Off-White" or "PaperWhite"?: ')
elif BASE == 'Manatee':
    ACCENT = raw_input('Which accent color'
                       ', "Platinum Mist" or "Spartan Sage"?: ')
    if ACCENT == 'Platinume Mist':
        HIGHLIGHT = raw_input('Which highlight color'
                              ',"Bone White" or "Just White"?: ')
    elif ACCENT == 'Spartan Sage':
        HIGHLIGHT = raw_input('Which highlight color'
                              ',"Fractal White" or "Not White"?: ')

MYSTR = 'Your selected colors are, {0}, {1}, and {2}.'
print MYSTR.format(BASE, ACCENT, HIGHLIGHT)
