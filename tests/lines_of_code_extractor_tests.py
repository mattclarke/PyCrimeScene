import unittest
from lines_of_code_extractor import LinesOfCodeExtractor as Loc


class LinesOfCodeExtractorTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_correctly_gets_number_of_lines_of_code_for_a_single_file(self):
        self.assertEqual(40, Loc.get_lines_of_code("test_data/example.java"))

    def test_get_number_of_lines_of_code_raises_if_file_does_not_exist(self):
        self.assertRaises(
            FileNotFoundError, Loc.get_lines_of_code, "test_data/does_not_exist.java"
        )

    def test_correctly_get_number_of_lines_of_code_for_all_files_in_a_directory(self):
        ans = Loc.get_lines_of_code_for_directory("./test_data")

        self.assertEqual(5, len(ans))
        self.assertEqual(40, ans["./test_data/example.java"])
        self.assertEqual(42, ans["./test_data/another_example.java"])
        self.assertEqual(0, ans["./test_data/maat_evo.log"])
        self.assertEqual(0, ans["./test_data/example.png"])
        self.assertEqual(7, ans["./test_data/sub_directory/yet_another_example.java"])

    # Not sure it is important to filter - leave this test commented out for now
    # def test_correctly_get_number_of_lines_of_code_for_code_files_only_in_a_directory(self):
    #     ans = Loc.get_lines_of_code_for_directory("./test_data", filter=True)
    #
    #     self.assertEqual(2, len(ans))
    #     self.assertEqual(40, ans["./test_data/example.java"])
    #     self.assertEqual(42, ans["./test_data/another_example.java"])

    def test_get_lines_of_code_for_directory_raises_if_does_not_exist(self):
        self.assertRaises(
            NotADirectoryError, Loc.get_lines_of_code_for_directory, "./does_not_exist"
        )
