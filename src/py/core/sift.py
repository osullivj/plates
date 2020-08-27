import pprint
import json
import sys
from core.generate import Post2001RegistrationGenerator, HexRegistrationGenerator


CHAR_PAIRS = {
    '01':['OI'],
    '06':['OG'],
    '08':['OB'],
    '10':['IO','LO'],
    '11':['II','LL'],
    '15':['IS','LS'],
    '16':['IG','LG'],
    '18':['IB','LB'],
    '51':['SI','SL'],
    '55':['SS'],
    '56':['SG'],
    '58':['SB'],
    '60':['GO'],
    '61':['GI','GL'],
    '65':['GS'],
    '66':['GG'],
    '68':['GB'],
}

class WordSifter( object):
    def __init__( self, wpath, hpath):
        self.words = dict( )
        # Post2001RegistrationGenerator will generate tuples like this...
        # (('A', 'A'), '01', ('A', 'A', 'A'))
        self.gen = Post2001RegistrationGenerator( CHAR_PAIRS.keys( ))
        with open( wpath, 'rt') as wf:
            self.words = json.load( wf)
        self.hits = dict( )
        self.hits_path = hpath

    def sift( self):
        for pfx, dyr, sfx in self.gen:
            for sub in CHAR_PAIRS.get( dyr, []):
                plate = '%s%s%s %s%s%s' % ( pfx[0], pfx[1], dyr, sfx[0], sfx[1], sfx[2])
                cw = '%s%s%s%s%s%s' % ( pfx[0], pfx[1], sub, sfx[0], sfx[1], sfx[2])
                candidate_word = cw.lower( )
                print( "%s %s" % ( plate, candidate_word))
                if candidate_word in self.words:
                    print( "HIT %s %s" % ( plate, candidate_word))
                    self.hits[plate] = candidate_word
        with open( self.hits_path, 'wt') as hitf:
            pprint.pprint( self.hits, hitf, indent=4)


class HexSifter( object):
    def __init__( self, hpath):
        self.gen = HexRegistrationGenerator( CHAR_PAIRS.keys( ))
        self.hits = set( )
        self.hits_path = hpath

    def sift( self):
        for pfx, dyr, sfx in self.gen:
            for sub in CHAR_PAIRS.get( dyr, []):
                plate = '%s%s%s %s%s%s' % ( pfx[0], pfx[1], dyr, sfx[0], sfx[1], sfx[2])
                print( plate)
                self.hits.add( plate)
        with open( self.hits_path, 'wt') as hitf:
            for hplate in self.hits:
                hitf.write( '%s\n' % hplate)


if __name__ == "__main__":
    sifter_class_name = sys.argv[1]
    sifter_class = globals( )[sifter_class_name]
    ctor_params = sys.argv[2:]
    sifter = sifter_class( *ctor_params)
    sifter.sift( )
    print( str( sifter.hits))
