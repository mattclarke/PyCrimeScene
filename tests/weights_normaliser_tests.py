import unittest
from weights_normaliser import normalise_weights


class NormaliseWeightsTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_given_one_weight_then_weight_normalised_to_one(self):
        commits = {"File1": 5}
        weights = normalise_weights(commits)
        self.assertEqual(1.0, weights['File1'])

    def test_given_two_weights_then_both_weights_normalised(self):
        commits = {"File1": 5, "File2": 10}
        weights = normalise_weights(commits)
        self.assertEqual(0.5, weights['File1'])
        self.assertEqual(1.0, weights['File2'])

    def test_given_three_weights_then_all_weights_normalised(self):
        commits = {"File1": 5, "File2": 10, "File3": 20}
        weights = normalise_weights(commits)
        self.assertEqual(0.25, weights['File1'])
        self.assertEqual(0.5, weights['File2'])
        self.assertEqual(1.0, weights['File3'])
