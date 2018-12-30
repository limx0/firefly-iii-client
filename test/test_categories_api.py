# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    OpenAPI spec version: 0.9.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import firefly_iii_client
from firefly_iii_client.api.categories_api import CategoriesApi  # noqa: E501
from firefly_iii_client.rest import ApiException


class TestCategoriesApi(unittest.TestCase):
    """CategoriesApi unit test stubs"""

    def setUp(self):
        self.api = firefly_iii_client.api.categories_api.CategoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_category(self):
        """Test case for delete_category

        Delete a category.  # noqa: E501
        """
        pass

    def test_get_categories(self):
        """Test case for get_categories

        List all categories.  # noqa: E501
        """
        pass

    def test_get_category(self):
        """Test case for get_category

        Get a single category.  # noqa: E501
        """
        pass

    def test_get_transactions_by_category(self):
        """Test case for get_transactions_by_category

        List all transactions in a category.  # noqa: E501
        """
        pass

    def test_store_category(self):
        """Test case for store_category

        Store a new category  # noqa: E501
        """
        pass

    def test_update_category(self):
        """Test case for update_category

        Update existing category.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()