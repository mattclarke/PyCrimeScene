import unittest
from data_miner import DataMiner

GITLOG_DATA = """
[f9f97a0] Matt Clarke 2017-07-10 Added png for testing purposes
-       -       tests/example.png

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


class DataMiningGitLogTests(unittest.TestCase):
    def test_correctly_extracts_number_of_commits_from_git_log(self):
        data_miner = DataMiner()
        self.assertEqual(5, data_miner.extract_number_commits(GITLOG_DATA))

    def test_if_commit_id_in_commit_message_number_of_commits_still_correct(self):
        # Stuff a commit id into a commit message - it might happen in real life
        modified_data = GITLOG_DATA.replace("Create README.md", "Create README.md [cef94a2]")
        data_miner = DataMiner()
        self.assertEqual(5, data_miner.extract_number_commits(modified_data))

    def test_correctly_extracts_number_of_authors(self):
        data_miner = DataMiner()
        self.assertEqual(3, data_miner.extract_number_authors(GITLOG_DATA))

    def test_correctly_extracts_number_of_entities_changed(self):
        data_miner = DataMiner()
        self.assertEqual(8, data_miner.extract_number_entities_changed(GITLOG_DATA))

    def test_data_miner_using_code_maat_data(self):
        maat_data = ""
        with open("maat_evo.log") as file:
            maat_data = file.read()

        data_miner = DataMiner()
        self.assertEqual(88, data_miner.extract_number_commits(maat_data))
        # TODO: Fails because of the space in the name
        self.assertEqual(2, data_miner.extract_number_authors(maat_data))
        self.assertEqual(283, data_miner.extract_number_entities_changed(maat_data))