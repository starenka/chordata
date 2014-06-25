#!/usr/bin/env python
# coding=utf-8

import importlib, argparse

from utils import render, build_diff_dict, INSTRUMENTS

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find chords by giving me notes')
    parser.add_argument('notes', nargs='+',
                        help='space separated notes: start from 1st string (E on guitar). Use "0" for open string and "x" for not played string.')
    parser.add_argument('-i', '--instrument', dest='instrument',
                        choices=INSTRUMENTS, default='mando',
                        help='instrument/tuning to search')
    args = parser.parse_args()

    instrument = importlib.import_module(args.instrument)
    by_diff = build_diff_dict(instrument.CHORDS)

    if len(args.notes) != len(instrument.STRINGS):
        raise ValueError('You have provided less or more notes. %s has %d strings' %
                         (args.instrument.capitalize(), len(instrument.STRINGS)))

    notes = tuple(map(lambda x: int(x) if x!= 'x' else -1, args.notes))
    for name, pattern in instrument.CHORDS:
        if notes == pattern:
            name = '[ ' + name.capitalize() + ' ]'
            print '\n', name.center(40, '=')
            render(pattern, instrument.STRINGS)
