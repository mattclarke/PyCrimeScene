import argparse
import json
from data_miner import DataMiner
from lines_of_code_extractor import LinesOfCodeExtractor
from hotspot_compiler import create_hotspots
from structure_generator import generate_structure


def main(logfile, directory, output):
    print(f"File chosen for analysis: {logfile}")

    # Load the log
    with open(logfile, "r") as myfile:
        logdata = myfile.read()

    # Get the complexity
    loc = LinesOfCodeExtractor().get_lines_of_code_for_directory(directory)

    # Get the commits
    commits = DataMiner().extract_changes_per_file(logdata)

    # Generate the hotspots
    hotspots = create_hotspots(commits, loc)

    # Dump as CSV
    print(f"Generating CSV file: {output}.csv")
    with open(f"{output}.csv", "w") as outfile:
        for hs in hotspots:
            outfile.write(f"{hs[0]},{hs[1]},{hs[2]}\n")

    # Generate structure for d3
    structure = generate_structure(hotspots)

    # Dump structure as JSON
    print(f"Generating JSON file: {output}.json")
    with open(f"{output}.json", "w") as outfile:
        json.dump(structure, outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a git log file.")
    parser.add_argument("logfile")
    parser.add_argument("directory")
    parser.add_argument("output")
    args = parser.parse_args()
    main(args.logfile, args.directory, args.output)
