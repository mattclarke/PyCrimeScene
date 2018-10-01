import argparse
from data_miner import DataMiner
from lines_of_code_extractor import LinesOfCodeExtractor
from hotspot_compiler import HotSpotCompiler
from weights_normaliser import normalise_weights


def main(logfile, directory, output):
    print(f"File chosen for analysis: {logfile}")

    # Load the log
    with open(logfile, "r") as myfile:
        logdata = myfile.read()

    # Get the commits
    commits = DataMiner().extract_changes_per_file(logdata)
    # Normalise the data into weights
    weights = normalise_weights(commits)

    # Get the complexity
    loc = LinesOfCodeExtractor().get_lines_of_code_for_directory(directory)

    # Compile hotspots
    hotspots = HotSpotCompiler.merge_raw_data(weights, loc)

    # with open(output, 'w') as myfile:
    for hs in hotspots:
        print("%s %s %s" % hs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a git log file.')
    parser.add_argument("logfile")
    parser.add_argument("directory")
    parser.add_argument("output")
    args = parser.parse_args()
    main(args.logfile, args.directory, args.output)
    # main('/Users/mattclarke/Code/Repos/Others/code-maat/maat_evo.log', '/Users/mattclarke/Code/Repos/Others/code-maat')