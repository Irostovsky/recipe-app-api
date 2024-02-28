from django.test import SimpleTestCase

from app.calc import add


class AddTest(SimpleTestCase):

    def test_check_sum(self):
        self.assertEqual(3, add(1, 2))
