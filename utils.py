#!/usr/bin/env python
# coding=utf-8

import collections, importlib

INSTRUMENT_CHOICES = collections.OrderedDict((
    ('mando','mandolin'),
    ('uke','ukulele'),
    ('guitar','guitar'),
    ('guitardd','guitar drop-d')))
FLATS_TO_SHARPS = {'db':'c#', 'eb':'d#', 'gb':'f#', 'bb': 'a#'}

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
    ret = filter(lambda x: x[1]!=pattern, by_diff.get(shape_to_diff_id(pattern)))
    return ret or []

def render(pattern, strings, padd=0):
    DIM, DIM_RESET = '\033[2m', '\033[22m'
    BAR = '|-%s-'

    min_, max_ = min(pattern), max(pattern)+1
    bars = range(min_-1 if min_ > 1 else 1, max_+1)
    print ' ' * padd + ' ' * 3, ' '.join([str(i).ljust(3, ' ') for i in bars])
    for string, note in zip(reversed(strings), reversed(pattern)):
        muted = note < 0
        line = [BAR % 'O' if note == i else BAR % '-' for i in bars]
        line = ''.join(line)
        line = ('X' if muted else '|') + line[1:]
        print ' ' * padd + '%s%s %s|%s' % (('',DIM)[muted], string,
                                           ''.join(line), ('',DIM_RESET)[muted])

def get_instrument(instrument):
    instrument = importlib.import_module(instrument)
    return instrument.STRINGS, instrument.CHORDS
