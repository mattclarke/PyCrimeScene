from structure_generator import generate_structure


def test_given_one_file_get_simple_structure():
    files = [("test/src/file.java", 1.0, 10)]
    top_node = generate_structure(files)

    assert "root" == top_node["name"]
    child = top_node["children"][0]
    assert "test" == child["name"]
    child = child["children"][0]
    assert "src" == child["name"]
    child = child["children"][0]
    assert "file.java" == child["name"]


def test_given_two_file_in_different_directories():
    files = [("test/src/file.java", 1.0, 10), ("doc/rst/readme.txt", 1.0, 10)]
    top_node = generate_structure(files)

    assert "root" == top_node["name"]

    # First file
    child = top_node["children"][0]
    assert "test" == child["name"]
    child = child["children"][0]
    assert "src" == child["name"]
    child = child["children"][0]
    assert "file.java" == child["name"]

    # Second file
    child = top_node["children"][1]
    assert "doc" == child["name"]
    child = child["children"][0]
    assert "rst" == child["name"]
    child = child["children"][0]
    assert "readme.txt" == child["name"]


def test_given_two_file_in_same_directory():
    files = [("test/src/file1.java", 1.0, 10), ("test/src/file2.java", 1.0, 10)]
    top_node = generate_structure(files)

    assert "root" == top_node["name"]

    child = top_node["children"][0]
    assert "test" == child["name"]
    child = child["children"][0]
    assert "src" == child["name"]
    child1 = child["children"][0]
    child2 = child["children"][1]
    # First file
    assert "file1.java" == child1["name"]

    # Second file
    assert "file2.java" == child2["name"]


def test_given_two_file_in_same_directory_structure():
    files = [("test/src/file1.java", 1.0, 10), ("test/file2.java", 1.0, 10)]
    top_node = generate_structure(files)

    assert "root" == top_node["name"]

    child = top_node["children"][0]
    assert "test" == child["name"]
    child = child["children"][0]
    assert "src" == child["name"]
    child = child["children"][0]
    # First file
    assert "file1.java" == child["name"]

    # Second file
    child = top_node["children"][0]
    assert "test" == child["name"]
    child = child["children"][1]
    assert "file2.java" == child["name"]
