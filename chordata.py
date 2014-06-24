#!/usr/bin/env python
# coding=utf-8

import collections, importlib, argparse

def diffs(items): #-1 for X
    items = [i for i in items if i > -1]
    return [j-i for i, j in zip(items[:-1], items[1:])]

def shape_to_diff_id(pattern):
    return ''.join(map(str, diffs(pattern)))

def build_diff_dict(chords):
    diff = collections.defaultdict(list)
    for chord, pattern in chords:
        diff[shape_to_diff_id(pattern)].append((chord, pattern))
    return diff

def with_same_pattern(pattern, by_diff):
    return filter(lambda x: x[1]!=pattern, by_diff.get(shape_to_diff_id(pattern)))

def render(pattern, strings, padd=0):
    bar = '|-%s-'
    min_, max_ = min(pattern), max(pattern)+1
    bars = range(min_-1 if min_ > 0 else 1, max_+1)
    print ' ' * padd + ' ' * 3, ' '.join([str(i).ljust(3, ' ') for i in bars])
    for string, note in zip(reversed(strings), reversed(pattern)):
        line = [bar % 'O' if note == i else bar % '-' for i in bars]
        line = ''.join(line)
        line = ('X' if note < 0 else '|') + line[1:]
        print ' ' * padd + '%s %s|' % (string.upper(), ''.join(line))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A dummy chordbook')
    parser.add_argument('chords', nargs='+')
    parser.add_argument('-i', '--instrument', dest='instrument',
                        choices=('mando', 'uke', 'guitar', 'guitardd'),
                        default='mando', help='instrument/tuning to show')
    parser.add_argument('-s', '--same-shapes', dest='same_shapes',
                        action='store_true', help='show chords w/ same shape')
    parser.add_argument('-a', '--all', dest='with_inversions',
                        action='store_true', help='show all chord inversions')
    args = parser.parse_args()

    instrument = importlib.import_module(args.instrument)
    by_diff = build_diff_dict(instrument.CHORDS)
    padd = 10

    for one in args.chords:
        one = one.lower()
        prev = None
        matches = [(n,p) for n,p in instrument.CHORDS if n[:2] in (one, one + '/')]

        for name, pattern in matches[:(1,-1)[args.with_inversions]]:
            name = '[ ' + name.capitalize() + ' ]'
            if name != prev:
                print '\n', name.center(40, '=')

            render(pattern, instrument.STRINGS)

            if args.same_shapes:
                shapes = with_same_pattern(pattern, by_diff)
                if shapes:
                    print '\n', ' ' * padd, 'w/ same shape:\n'
                for sname, spattern in shapes:
                    sname = '[ ' + sname.capitalize() + ' ]'
                    print ' ' * padd, sname.center(30, '~')
                    render(spattern, instrument.STRINGS, padd)
                    print '\n'

            prev = name
            print '\n'
