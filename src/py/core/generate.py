import itertools
import string


PREFIX_CHARS = [u for u in string.ascii_uppercase if u not in ('I','Q','Z')]
SUFFIX_CHARS = PREFIX_CHARS + ['Z']
HEX_CHARS = ['A', 'B', 'C', 'D', 'E', 'F']
NXYR = 20
DEMI_YEARS = ['%02d' % y for y in list( range( 1, NXYR)) + list( range( 51, 50+NXYR))]


class Post2001RegistrationGenerator( object):
    def __init__(self, years=DEMI_YEARS):
        self.prefix_iter = itertools.product( PREFIX_CHARS, repeat=2)
        self.demi_year_iter = iter( years)
        self.suffix_iter = itertools.product( SUFFIX_CHARS, repeat=3)

    def __iter__(self):
        return itertools.product( self.prefix_iter, self.demi_year_iter, self.suffix_iter)


class HexRegistrationGenerator( object):
    def __init__(self, years=DEMI_YEARS):
        self.demi_year_iter = iter( years)
        self.suffix_iter = itertools.product( HEX_CHARS, repeat=3)

    def __iter__(self):
        return itertools.product( ['OX'], self.demi_year_iter, self.suffix_iter)
