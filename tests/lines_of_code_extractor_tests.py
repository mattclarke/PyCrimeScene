import unittest
from lines_of_code_extractor import LinesOfCodeExtractor as Loc


class LinesOfCodeExtractorTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_correctly_gets_number_of_lines_of_code_for_a_single_file(self):
        self.assertEqual(40, Loc.get_lines_of_code("test_data/example.java"))

    def test_get_number_of_lines_of_code_raises_if_file_does_not_exist(self):
        self.assertRaises(FileNotFoundError, Loc.get_lines_of_code, "test_data/does_not_exist.java")

    def test_correctly_get_number_of_lines_of_code_for_all_files_in_a_directory(self):
        ans = Loc.get_lines_of_code_for_directory("./test_data")
        print(ans)
        self.assertEqual(4, len(ans))
        self.assertEqual(40, ans["./test_data/example.java"])
        self.assertEqual(42, ans["./test_data/another_example.java"])
        self.assertEqual(0, ans["./test_data/maat_evo.log"])
        self.assertEqual(0, ans["./test_data/example.png"])

    def test_correctly_get_number_of_lines_of_code_for_code_files_only_in_a_directory(self):
        ans = Loc.get_lines_of_code_for_directory("./test_data")
        print(ans)
        self.assertEqual(2, len(ans))
        self.assertEqual(40, ans["./test_data/example.java"])
        self.assertEqual(42, ans["./test_data/another_example.java"])

