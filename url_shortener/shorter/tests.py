from django.test import TestCase

from .models import Url


class UrlSplitTestCase(TestCase):
    def setUp(self):
        self.test_cases_good = [
            'http://techcrunch.com/2012/12/28/pinterest-lawsuit/',
            'https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/',
        ]
        self.test_cases_wrong = [
            '+=-!@#$%^&*(',
            '//',
            '',
        ]

    def test_split_returns_list(self):
        """test if return is list"""
        for test_case in self.test_cases_good:
            response = Url.split_url_into_words(test_case)
            self.assertIsInstance(response, list)

    def test_split_good_length(self):
        """test if return more than one"""
        for test_case in self.test_cases_good:
            response = Url.split_url_into_words(test_case)
            self.assertGreaterEqual(len(response), 0)

    def test_specification_url(self):
        test_case = 'http://techcrunch.com/2012/12/28/pinterest-lawsuit/'
        response = Url.split_url_into_words(test_case)
        self.assertEqual(response, ['http', 'techcrunch', 'com', '2012', '12', '28', 'pinterest', 'lawsuit'])

    def test_lawsuit_in_first_test_case(self):
        """test for lawsuit in url"""
        test_case = 'http://techcrunch.com/2012/12/28/pinterest-lawsuit/'
        response = Url.split_url_into_words(test_case)
        self.assertIn('lawsuit', response)

    def test_pinterest_in_first_test_case(self):
        test_case = 'http://techcrunch.com/2012/12/28/pinterest-lawsuit/'
        response = Url.split_url_into_words(test_case)
        self.assertIn('pinterest', response)

    def test_wrong_urls_return_empty(self):
        for test_case in self.test_cases_wrong:
            response = Url.split_url_into_words(test_case)
            self.assertEqual(len(response), 0)