import itertools
import string


PREFIX_CHARS = [u for u in string.ascii_uppercase if u not in ('I','Q','Z')]
SUFFIX_CHARS = PREFIX_CHARS + ['Z']
HEX_CHARS = ['A', 'B', 'C', 'D', 'E', 'F']
# All the good plates are gone. Let's focus on looking for good ones in the forthcoming
# plates eg 2021-03-01 21 plate, and 2021-09-01 71 plate.
BASE_YEAR = 20
END_YEAR = 22
DEMI_YEARS = ['%02d' % y for y in list( range( BASE_YEAR, END_YEAR)) + list( range( BASE_YEAR+50, END_YEAR+50))]


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
