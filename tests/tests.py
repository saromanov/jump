from jump.jump import jump
import unittest


class TestBasic(unittest.TestCase):
    def test_basic(self):
        assert jump(856332222999, 8) == 1

if __name__ == '__main__':
    unittest.main()