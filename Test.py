#!/usr/bin/python3
# Test case for adding 6 to elements of a list
import unittest

from SE_jenkins import add_6_to_list

class Testadd6(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add 6 to elements of a list
        """
        data = [1,2,3,4,5]
        result = add_6_to_list(data)
        self.assertEqual(result, [7,8,9,10,11])

if __name__ == '__main__':
    unittest.main()
