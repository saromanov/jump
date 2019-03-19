from jump.jump import jump, InputException
import unittest


class TestBasic(unittest.TestCase):
    def test_basic(self):
        assert jump(856332222999, 8) == 1
        assert jump(8, 25) == 4
        assert jump(800000, 1) == 0
        with self.assertRaises(InputException):
            jump(10,-1)
            jump(-1,10)

if __name__ == '__main__':
    unittest.main()