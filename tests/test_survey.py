# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/10 19:35

import unittest
from survey import AnonymousSurvey


class TestAnonmyousSurvey(unittest.TestCase):

    def test_store_single_response(self):
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)


if __name__ == '__main__':
    unittest.main()
