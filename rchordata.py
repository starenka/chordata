#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
import argparse

from utils import render, build_diff_dict, get_instrument, INSTRUMENT_CHOICES

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find chords by giving me notes')
    parser.add_argument('notes', nargs='+',
                        help='space separated notes: start from 1st string (E on guitar). '
                             'Use "0" for open string and "x" for not played string.')
    parser.add_argument('-i', '--instrument', dest='instrument',
                        choices=INSTRUMENT_CHOICES.keys(), default='mando',
                        help='instrument/tuning to search')
    args = parser.parse_args()

    STRINGS, CHORDS = get_instrument(args.instrument)
    by_diff = build_diff_dict(CHORDS)

    if len(args.notes) != len(STRINGS):
        raise ValueError('You have provided less or more notes. %s has %d strings.' %
                         (args.instrument.capitalize(), len(STRINGS)))

    notes = tuple(map(lambda x: int(x) if x != 'x' else -1, args.notes))
    matches = [name for name, patt in CHORDS if notes == patt]

    if matches:
        render(notes, STRINGS)
        print('\nIs known as: %s\n' % ', '.join(matches))
