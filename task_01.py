#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring to provide brnaching for decision trees."""


BASE = raw_input('Which base color: Seattle Grey or Manatee: ')
ACCENT = raw_input('Which accent color: Ceramic Glaze, Culumbus Nimbus,\
Platinum Mist, or Spartan Sage:')
HIGHLIGHT = raw_input('Which highlight color: Basically White, White, \
Off-White, Paper White, Bone White, Just White, Fractal White, Not White: ')
COLOR_CHOICE = '{}, {1}, {}'
print 'You chose: ' + Choices.format(BASE, ACCENT, HIGHIGHT)
