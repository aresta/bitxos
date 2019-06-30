import unittest

from bitxos.olakease import olakease


class OlakeaseTestCase(unittest.TestCase):

    def test_olakease(self):
        self.assertEqual(
            olakease(),
            'olakease mon!'
        )
