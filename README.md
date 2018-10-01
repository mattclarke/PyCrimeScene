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