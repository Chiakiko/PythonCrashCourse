# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/10 15:03

import unittest
from Chapter_11 import get_formatted_name


class TestChpater11(unittest.TestCase):

    def test_get_formatted_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEquals(formatted_name, 'janis joplin')


if __name__ == '__main__':
    unittest.main()
