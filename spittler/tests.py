# -*- coding: utf-8 -*-

"""
 Spittler app tests
"""

from django.test import TestCase
from spittler.settings.settings import Settings
from spittler.templatetags.calculate_position import calculate_tag_position_vertically, calculate_tag_position_horizontally


class SimpleTest(TestCase):
    def test_calculate_tag_position_vertically(self):
        """
            Calculation of spittle tag top attribute test
        """
        self.assertLessEqual(calculate_tag_position_vertically(0, 100), 50)
        self.assertLessEqual(calculate_tag_position_vertically(1, 100), 150)
        self.assertLessEqual(calculate_tag_position_vertically(Settings.VERTICAL_SCALE, 100), 50)

    def test_calculate_tag_position_vertically(self):
        """
            Calculation of spittle tag left attribute test
        """
        self.assertLessEqual(calculate_tag_position_horizontally(0, 150), 25)
        self.assertLessEqual(calculate_tag_position_horizontally(1, 150), 25)
        self.assertLessEqual(calculate_tag_position_horizontally(Settings.VERTICAL_SCALE, 100), 125)
