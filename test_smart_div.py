import unittest
from io import StringIO
from unittest.mock import patch

# Import the functions from the main code
from decorator import div, smart_div


class TestSmartDiv(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        self.patcher = patch('sys.stdout', new=self.output)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_smart_div_greater(self):
        div1 = smart_div(div)
        div1(3, 4)
        self.assertEqual(self.output.getvalue(), '1.3333333333333333\n')

    def test_smart_div_smaller(self):
        div1 = smart_div(div)
        div1(4, 3)
        self.assertEqual(self.output.getvalue(), '1.3333333333333333\n')

    def test_smart_div_equalTo(self):
        divid = smart_div(div)
        divid(4,4)
        self.assertEqual(self.output.getvalue(), '1.0\n')

if __name__ == '__main__':
    unittest.main()