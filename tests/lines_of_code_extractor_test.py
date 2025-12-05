import os
import pytest
import tests
from lines_of_code_extractor import LinesOfCodeExtractor as Loc

# Trick to get path of test data
path = os.path.join(os.path.dirname(tests.__file__), "test_data")


def test_correctly_gets_number_of_lines_of_code_for_a_single_file():
    assert Loc.get_lines_of_code(f"{path}/example.java") == 40


def test_get_number_of_lines_of_code_raises_if_file_does_not_exist():
    with pytest.raises(FileNotFoundError):
        Loc.get_lines_of_code("does_not_exist.java")


def test_correctly_get_number_of_lines_of_code_for_all_files_in_a_directory():
    ans = Loc.get_lines_of_code_for_directory(f"{path}")

    assert len(ans) == 5
    assert ans["example.java"] == 40
    assert ans["another_example.java"] == 42
    assert ans["maat_evo.log"] == 0
    assert ans["example.png"] == 0
    assert ans["sub_directory/yet_another_example.java"] == 7


# TODO: reinstate this test
# def test_correctly_get_number_of_lines_of_code_for_code_files_only_in_a_directory():
#     ans = Loc.get_lines_of_code_for_directory("./test_data", filter=True)
#
#     self.assertEqual(2, len(ans))
#     self.assertEqual(40, ans["./test_data/example.java"])
#     self.assertEqual(42, ans["./test_data/another_example.java"])


def test_get_lines_of_code_for_directory_raises_if_does_not_exist():
    with pytest.raises(NotADirectoryError):
        Loc.get_lines_of_code_for_directory("does_not_exist")
