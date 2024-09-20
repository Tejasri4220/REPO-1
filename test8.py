def subtract (a,b):
    return (a-b)


import unittest


class loginclass(unittest.TestCase):
    def test1(self):

        result = subtract(10,7)
        self.assretEqual(result,3)
        
