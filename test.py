import unittest
import main

class tests(unittest.TestCase):

    def test_readtext(self):
        """
        test whether readtext() open file before check existed
        :return: no return value
        """
        self.assertEqual(main.readtext('dsrfws'),False)

    def test_showImg(self):
        """
        test whether showImg() display image before check existed
        :return:
        """
        self.assertEqual(main.showImg('sdads'),False)

if __name__=='__main__':
    unittest.main()