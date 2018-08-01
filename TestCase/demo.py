import unittest

class demo(unittest.TestCase):

    def setUp(self):
        print('Setup..')

    def tearDown(self):
        print('TearDown..')

    def test_print(self):
        print('print now..')

if __name__ == '__main__':
    unittest.main()
