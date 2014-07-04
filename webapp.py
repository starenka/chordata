#!/usr/bin/env python
# coding=utf-8
import json

from bottle import (get, request, run, route, default_app, app, static_file,
            TEMPLATE_PATH, jinja2_template as template)

from utils import (build_diff_dict, with_same_pattern, get_instrument,
                   INSTRUMENT_CHOICES, FLATS_TO_SHARPS)

TEMPLATE_PATH.append('./templates')
STATIC_DIR = './static'


@get('/')
def search():
    return template('search.html', title='Chord search', instruments=INSTRUMENT_CHOICES)

@get('/reverse')
def reverse():
    return template('rsearch.html', title='Reverse search', instruments=INSTRUMENT_CHOICES)

@get('/links')
def links():
    return template('links.html', title='Useful links')

@get('/search')
def search():
    instrument, chord = request.query.get('instrument'), request.query.get('chord').strip()
    max_fingers = request.query.get('max_fingers', None)

    nchord = chord.lower()
    nchord = FLATS_TO_SHARPS.get(chord, nchord)

    STRINGS, CHORDS = get_instrument(instrument)
    by_diff = build_diff_dict(CHORDS)

    matches = [(n,p) for n,p in CHORDS if any([n.lower()==nchord, n[:len(chord)+1].lower()==nchord+'/'])]
    if max_fingers:
        matches = [(n,p) for n,p in matches if len(filter(lambda x: x > 0, p)) <= int(max_fingers)]

    matches = [(n,p,with_same_pattern(p, by_diff)) for n,p in matches]

    return template('sresults.html', title='Chord search',
                    instrument=instrument, instruments=INSTRUMENT_CHOICES,
                    query=chord, max_fingers=max_fingers,
                    matches_json=json.dumps(matches), matches=matches,
                    strings_json=json.dumps(STRINGS)
    )

@get('/rsearch')
def rsearch():
    instrument, pattern = request.query.get('instrument'), request.query.get('pattern','').strip()

    STRINGS, CHORDS = get_instrument(instrument)
    by_diff = build_diff_dict(CHORDS)

    notes = tuple(map(lambda x: int(x) if x not in 'xX' else -1, pattern.split()))

    matches = []
    if len(notes) == len(STRINGS):
        matches = [(name, patt) for name, patt in CHORDS if notes == patt]
        matches = [(n,p,with_same_pattern(p, by_diff)) for n,p in matches]

    return template('rresults.html', title='Reverse search',
                    instrument=instrument, instruments=INSTRUMENT_CHOICES,
                    query=pattern,
                    matches_json=json.dumps(matches), matches=matches,
                    strings_json=json.dumps(STRINGS)
    )


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=STATIC_DIR)

if __name__ == '__main__':
    from werkzeug.debug import DebuggedApplication
    app = app()
    app.catchall = False
    application = DebuggedApplication(app, evalex=True)
    run(app=application, host='localhost', port=8080, reloader=True, debug=True)
else:
    application = default_app()
