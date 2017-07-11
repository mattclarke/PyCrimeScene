import unittest
from lines_of_code_extractor import LinesOfCodeExtractor as Loc


class LinesOfCodeExtractorTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_correctly_gets_number_of_lines_of_code_for_a_single_file(self):
        self.assertEqual(40, Loc.get_lines_of_code("example.java"))
