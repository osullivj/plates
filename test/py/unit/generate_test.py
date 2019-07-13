import unittest

from core.generate import Post2001RegistrationGenerator

PLATE1 = (('A', 'A'), '01', ('A', 'A', 'A'))

class GenerateTests( unittest.TestCase):
    def setUp( self):
        self.gen = Post2001RegistrationGenerator( )
        self.iter = iter( self.gen)

    def test_plate1( self):
        p1 = next( self.iter)
        self.assertEqual( p1, PLATE1)


if __name__ == '__main__':
    unittest.main()
