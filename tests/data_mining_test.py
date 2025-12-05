import os

import pytest

import tests
from data_miner import DataMiner

GITLOG_DATA = """
[f9f97a0] Matt Clarke 2017-07-10 Added png for testing purposes
-       -       tests/example.png
12      0       tests/DataMiningTests.py
25      25      tests/data_mining_tests.py

[cef94a2] mjc23 2017-07-10 Added DataMiner class
3       0       data_miner.py
0       12      tests/DataMiningTests.py
25      0       tests/data_mining_tests.py

[74f6bbf] mjc23 2017-07-10 Added first unit test
12      0       tests/data_mining_tests.py

[1dbf879] mjclarke01 2017-07-10 Create README.md
2       0       README.md

[9d18261] mjclarke01 2017-07-10 Initial commit
101     0       .gitignore
29      0       LICENSE
"""


class TestDataMiner:
    @pytest.fixture(autouse=True)
    def prepare(self):
        # Trick to get path of test data
        path = os.path.join(os.path.dirname(tests.__file__), "test_data/repo_evo.log")
        with open(path) as file:
            self.repo_data = file.read()

    def test_correctly_extracts_number_of_commits(self):
        data_miner = DataMiner()
        assert data_miner.extract_number_commits(GITLOG_DATA) == 5

    def test_correctly_extracts_number_of_commits_from_code_log(self):
        data_miner = DataMiner()
        assert data_miner.extract_number_commits(self.repo_data) == 54

    def test_if_commit_id_in_commit_message_number_of_commits_still_correct(self):
        # Stuff a commit id into a commit message - it might happen in real life
        modified_data = GITLOG_DATA.replace(
            "Create README.md", "Create README.md [cef94a2]"
        )
        data_miner = DataMiner()
        assert data_miner.extract_number_commits(modified_data) == 5

    def test_correctly_extracts_number_of_authors(self):
        data_miner = DataMiner()
        assert data_miner.extract_number_authors(GITLOG_DATA) == 3

    def test_correctly_extracts_number_of_authors_from_code_log(self):
        data_miner = DataMiner()
        assert data_miner.extract_number_authors(self.repo_data) == 3

    def test_correctly_extracts_number_of_entities_changed(self):
        data_miner = DataMiner()
        assert data_miner.extract_number_entities_changed(GITLOG_DATA) == 10

    def test_correctly_extracts_number_of_entities_changed_from_code_log(self):
        data_miner = DataMiner()
        assert data_miner.extract_number_entities_changed(self.repo_data) == 102

    def test_correctly_extracts_number_of_entities_from_code__log(self):
        data_miner = DataMiner()
        assert data_miner.extract_number_entities(self.repo_data) == 44

    def test_correctly_extracts_dict_of_filenames_with_number_of_changes(self):
        data_miner = DataMiner()
        ans = data_miner.extract_changes_per_file(GITLOG_DATA)
        assert ans["LICENSE"] == 1
        assert ans["data_miner.py"] == 1
        assert ans["tests/DataMiningTests.py"] == 2
        assert ans["tests/data_mining_tests.py"] == 3
