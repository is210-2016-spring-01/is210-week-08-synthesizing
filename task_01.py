#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 1 file."""

BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"?: ')

if BASE == 'Seattle Gray':
    print """Which accent color, "Ceramic Glaze" or "Cumulus Nimbus"?: """,
    ACCENT = raw_input()
    if ACCENT == 'Ceramic Glaze':
        print """Which highlight color, "Basically White" or "White"?: """,
        HIGHLIGHT = raw_input()
    elif ACCENT == 'Cumulus Nimbus':
        print """Which highlight color, "Off-White" or "Paper White"?: """,
        HIGHLIGHT = raw_input()
elif BASE == 'Manatee':
    print """Which accent color, "Platinum Mist" or "Spartan Sage"?: """,
    ACCENT = raw_input()
    if ACCENT == 'Platinum Mist':
        print """Which highlight color, "Bone White" or "Just White"?: """,
        HIGHLIGHT = raw_input()
    elif ACCENT == 'Spartan Sage':
        print """Which highlight color, "Fractal White" or "Not White"?: """,
        HIGHLIGHT = raw_input()

print 'Your selected colors are {0}, {1}, and {2}.'.format(BASE, ACCENT,
                                                           HIGHLIGHT)
