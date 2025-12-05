# PyCrimeScene
A Python-based implementation of "Your Code as a Crime Scene" by Adam Tornhill.

## Generate a git log file

Clone a repo you are interested in and run:
```
git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat > repo_evo.log
```

It is also possible to specify date ranges:
```
git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat --before=2018-10-01 --after=2018-08-01 > repo_evo.log
```

## Run PyCrimeScene
From the PyCrimeScene directory:

```
python main.py <path to generated log file> <path to local copy of git repo> <name for output files>
```
There is also an optional `-f` flag for filtering on file extension.

For example:
```
python main.py -f .py repo_evo.log /Code/Repos/DMSC/forward-epics-to-kafka/ output
```

This will produce the files `output.csv` and `output.json`.

## Displaying the data
The `display` folder contains a D3 base webpage for showing the data.

Copy the JSON output generated above into the `display` directory and rename it to `input.json`.

Start the built-in Python webserver:
```
python -m http.server 8080
```
The data can then be viewed at `http://localhost:8080/display.html`.

## For developers
Ruff is used to take care of all the formatting and linting.

To format the code:
```
ruff format
```

To run the linter:
```
ruff check
```

To sort the imports:
```
ruff check --select I --fix
```

