#!/usr/bin/env python
# coding=utf-8

import argparse

from utils import (render, build_diff_dict, with_same_pattern, get_instrument,
                   INSTRUMENT_CHOICES, ES_TO_IS)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A dummy chordbook')
    parser.add_argument('chords', nargs='+')
    parser.add_argument('-i', '--instrument', dest='instrument',
                        choices=INSTRUMENT_CHOICES, default='mando',
                        help='instrument/tuning to show')
    parser.add_argument('-s', '--same-shapes', dest='same_shapes',
                        action='store_true', help='show chords w/ same shape')
    parser.add_argument('-a', '--all', dest='with_inversions',
                        action='store_true', help='show all chord inversions')
    args = parser.parse_args()

    STRINGS, CHORDS = get_instrument(args.instrument)
    by_diff = build_diff_dict(CHORDS)
    padd = 10

    for one in args.chords:
        one = one.lower()
        one = ES_TO_IS.get(one, one)

        prev = None
        matches = [(n,p) for n,p in CHORDS if n[:2] in (one, one + '/')]

        for name, pattern in matches[:(1,-1)[args.with_inversions]]:
            name = '[ ' + name.capitalize() + ' ]'
            if name != prev:
                print '\n', name.center(40, '=')

            render(pattern, STRINGS)

            if args.same_shapes:
                shapes = with_same_pattern(pattern, by_diff)
                if shapes:
                    print '\n', ' ' * padd, 'w/ same shape:\n'
                for sname, spattern in shapes:
                    sname = '[ ' + sname.capitalize() + ' ]'
                    print ' ' * padd, sname.center(30, '~')
                    render(spattern, STRINGS, padd)
                    print '\n'

            prev = name
            print '\n'
