import unittest
import u1

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))

    def test1(self):
        '''
        5/10 should simplify to 1/2
        '''
        a,b = u1.simplify(5,10)
        assert (a==1) # test 1 fails - wrong numerator
        assert (b==2) # test 1 fails - wrong denominator

   

if __name__ == '__main__':
    unittest.main()