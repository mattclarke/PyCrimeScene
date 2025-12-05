from src.weights_normaliser import normalise_weights


def create_hotspots(commits, loc):
    """
    Creates the hotspots.

    :param commits: a dict of file names and the number of commits
    :param lines_of_code: a dict of file names and the number of lines of code
    :return: a sorted list of tuple (name, changes, lines)
    """

    # Remove any files with no lines of code before normalisation
    remove_files_with_no_code(commits, loc)

    # Normalise the data into weights
    weights = normalise_weights(commits)

    # Compile hotspots
    return merge_raw_data(weights, loc)


def remove_files_with_no_code(commits, lines_of_code):
    """
    Removes files that either have no lines of code or no longer exist but are
    historically present in the commits list.

    :param commits: a dict of file names and the number of commits
    :param lines_of_code: a dict of file names and the number of lines of code
    """
    for k in list(commits.keys()):
        if k not in lines_of_code or lines_of_code[k] == 0:
            del commits[k]


def merge_raw_data(commits, lines_of_code):
    """
    Creates a list of the files sorted primarily by the number of changes
    and secondly by the number of lines of code.

    :param commits: a dict of file names and the number of commits
    :param lines_of_code: a dict of file names and the number of lines of code
    :return: a sorted list of tuple (name, changes, lines)
    """
    if not commits:
        return []

    data = []
    for k, v in commits.items():
        # File may not exist anymore but is still in log
        # Skip these files
        if k in lines_of_code:
            data.append((k, v, lines_of_code[k]))
    # Sort on secondary key
    data = sorted(data, key=lambda x: x[2], reverse=True)
    # Sort on primary key as this gives sorted by first value then by
    # second value
    return sorted(data, key=lambda x: x[1], reverse=True)
