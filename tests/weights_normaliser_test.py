from weights_normaliser import normalise_weights


def test_given_one_weight_then_weight_normalised_to_one():
    commits = {"File1": 5}
    weights = normalise_weights(commits)

    assert weights["File1"] == 1.0


def test_given_two_weights_then_both_weights_normalised():
    commits = {"File1": 5, "File2": 10}
    weights = normalise_weights(commits)

    assert weights["File1"] == 0.5
    assert weights["File2"] == 1.0


def test_given_three_weights_then_all_weights_normalised():
    commits = {"File1": 5, "File2": 10, "File3": 20}
    weights = normalise_weights(commits)

    assert weights["File1"] == 0.25
    assert weights["File2"] == 0.5
    assert weights["File3"] == 1.0
