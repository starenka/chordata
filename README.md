##Chordata

ChorData. Beasts [with strings.] (http://es.wikipedia.org/wiki/Chordata) Get it, right? Okay, this is a dummy chordbook with a LOT of inversions for mandolin, ukulele and guitar using standard tuning. There's also drop-D for guitar as I grew up playing like that. You can also find a chord name by knowing notes you play.

##Features

    chordata.py -h

    usage: chordata [-h] [-i {mando,uke,guitar,guitardd}] [-s] [-a]
                    [-f MAX_FINGERS]
                    chords [chords ...]

    A dummy chordbook

    positional arguments:
      chords

    optional arguments:
      -h, --help            show this help message and exit
      -i {mando,uke,guitar,guitardd}, --instrument {mando,uke,guitar,guitardd}
                            instrument/tuning to show
      -s, --same-shapes     show chords w/ same shape
      -a, --all             show all chord inversions
      -f MAX_FINGERS, --max-fingers MAX_FINGERS
                            how many figers maximum you want to use


    rchordata.py -h
    usage: rchordata [-h] [-i {mando,uke,guitar,guitardd}] notes [notes ...]

    Find chords by giving me notes

    positional arguments:
      notes                 space separated notes: start from 1st string (E on
                            guitar). Use "0" for open string and "x" for not
                            played string.

    optional arguments:
      -h, --help            show this help message and exit
      -i {mando,uke,guitar,guitardd}, --instrument {mando,uke,guitar,guitardd}
                            instrument/tuning to search


###To get just some chords you need quick:


    chordata.py c f g

    =================[ C ]==================
        1   2   3   4   5   6
    E |---|---|---|---|---|---|
    A |---|---|-O-|---|---|---|
    D |---|---|---|---|-O-|---|
    G |---|---|---|---|-O-|---|



    =================[ F ]==================
        1   2   3   4   5   6
    E |---|---|---|---|-O-|---|
    A |---|---|-O-|---|---|---|
    D |---|---|-O-|---|---|---|
    G X---|---|---|---|---|---|



    =================[ G ]==================
        1   2   3   4
    E |---|---|-O-|---|
    A |---|-O-|---|---|
    D |---|---|---|---|
    G |---|---|---|---|



###In case you need to see all the inversions:


    chordata.py c --all --instrument uke

    =================[ C ]==================
        2   3   4   5   6
    A |---|-O-|---|---|---|
    E |---|-O-|---|---|---|
    C |---|---|-O-|---|---|
    G |---|---|---|-O-|---|


        1   2   3   4   5   6   7   8
    A |---|---|---|---|---|---|-O-|---|
    E |---|---|-O-|---|---|---|---|---|
    C |---|---|---|---|---|---|---|---|
    G X---|---|---|---|---|---|---|---|


        1   2   3   4   5   6   7   8
    A |---|---|---|---|---|---|-O-|---|
    E |---|---|---|---|---|---|---|---|
    C |---|---|---|---|---|---|-O-|---|
    G |---|---|---|---|-O-|---|---|---|


    ... (more) ...


###To see what other chords you can play with "this finger-pattern"*:

*Does not always mean same strings. Also considers chords with open strings and barre equal.


    chordata.py g7 --same-shape --instrument mando

    =================[ G7 ]=================
        1   2   3
    E |-O-|---|---|
    A |---|-O-|---|
    D |---|---|---|
    G |---|---|---|

               w/ same shape:

               ~~~~~~~~~~~~[ C7 ]~~~~~~~~~~~~
                  4   5   6   7   8
              E |---|---|-O-|---|---|
              A |---|---|---|-O-|---|
              D |---|-O-|---|---|---|
              G |---|-O-|---|---|---|


               ~~~~~~~~~~~[ C#7 ]~~~~~~~~~~~~
                  5   6   7   8   9
              E |---|---|-O-|---|---|
              A |---|---|---|-O-|---|
              D |---|-O-|---|---|---|
              G |---|-O-|---|---|---|


               ~~~~~~~~~~~~[ D7 ]~~~~~~~~~~~~
                  6   7   8   9   10
              E |---|---|-O-|---|---|
              A |---|---|---|-O-|---|
              D |---|-O-|---|---|---|
              G |---|-O-|---|---|---|

              ... (more) ...


###Know a pattern, but have no idea what chord is it?

    rchordata.py 1 2 3 4 --instrument mando

        1   2   3   4   5
    E |---|---|---|-O-|---|
    A |---|---|-O-|---|---|
    D |---|-O-|---|---|---|
    G |-O-|---|---|---|---|

    Is known as: Caug/G#, Eaug/G#, G#aug


###To lame? Specify how many max fingers you need for a G:

    chordata g --instrument mando --max-fingers 2 --all

    =================[ G ]==================
        1   2   3   4
    E |---|---|-O-|---|
    A |---|-O-|---|---|
    D |---|---|---|---|
    G |---|---|---|---|


        1   2   3   4   5   6   7   8
    E |---|---|---|---|---|---|-O-|---|
    A |---|---|---|---|-O-|---|---|---|
    D |---|---|---|---|---|---|---|---|
    G |---|---|---|---|---|---|---|---|


        1   2   3   4   5   6   7   8   9   10  11
    E |---|---|---|---|---|---|-O-|---|---|---|---|
    A |---|---|---|---|---|---|---|---|---|-O-|---|
    D |---|---|---|---|---|---|---|---|---|---|---|
    G |---|---|---|---|---|---|---|---|---|---|---|


        1   2   3
    E X---|---|---|
    A |---|-O-|---|
    D |---|---|---|
    G |---|---|---|



    ================[ G/d ]=================
        1   2   3   4
    E |---|---|-O-|---|
    A |---|-O-|---|---|
    D |---|---|---|---|
    G X---|---|---|---|



##PLANNED FEATURES

- better search
- nicer rendering (images?)
- web interface?
