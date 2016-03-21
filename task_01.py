#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"?: ')

if BASE == "Seattle Gray":
    ACCENT = raw_input(
        'Which accent color, "Ceramic Glaze" or "Cumulus Nimbus"?: ')
    if ACCENT == "Ceramic Glaze":
        HIGHLIGHT = raw_input(
            'Which highlight color, "Basically White" or "White"?: ')
    if ACCENT == "Cumulus Nimbus":
        HIGHLIGHT = raw_input(
            'Which highlight color, "Off-White" or "Paper White"?: ')
elif BASE == "Manatee":
    ACCENT = raw_input(
        'Which accent color, "Platinum Mist" or "Spartan Sage"?: ')
    if ACCENT == "Platinum Mist":
        HIGHLIGHT = raw_input(
            'Which highlight color, "Bone White" or "Just White"?: ')
    if ACCENT == "Spartan Sage":
        HIGHLIGHT = raw_input(
            'Which highlight color, "Fractal White" or "Not White"?: ')

print "Your selected colors are, {}, {},and {}.".format(BASE, ACCENT, HIGHLIGHT)
