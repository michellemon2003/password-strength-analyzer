# Password Strength Analyzer

## Overview and problem

A local Python command-line tool that gives educational feedback on a sample password. The project explores how a strength rating can explain simple rules such as length and predictable patterns.

## Learning objectives

Practice converting security concepts into readable Python conditions and testing the boundaries of those conditions. This project focuses on basic password evaluation and educational security feedback.

## Technologies and features

Python 3.10+ and its standard library. The tool prompts for hidden input, counts four character groups, flags a small list of common passwords and simple patterns, and prints feedback. It has no storage, logging, or networking code.

## Repository structure

* `analyzer.py` contains the rating rules and terminal entry point.
* [Development notes](docs/development-notes.md) explain the design choices.
* [Concepts](docs/concepts.md) covers the security and Python basics.

## Installation and use

Install Python 3.10+ and open a terminal in the repository root. The standard library supplies every dependency.

```bash
python3 analyzer.py
```

Enter a made-up example at the prompt and get your feedback on your password strength.

## Results and observations

Checked passed four assertions covering the small common-password list, sequence and repetition checks, a longer example, and character-group counting. A run with unavailable hidden input stopped without reading the sample. Personal verification is pending.

|Test|Action|Result|
|-|-|-|
|Common|Enter `password123`|Weak and a common-list message|
|Sequence|Enter `abcdabcdabcdabcd`|Needs improvement and pattern feedback|
|Mixed|Enter `Velvet Otter! Cobalt 42`|Stronger by these checks, 4 of 4 groups|
|Blank|Press Enter immediately|Non-blank input message, then exit|

## Limitations

The rules use a tiny common-password list and simple character sequences. A predictable phrase can score well, and reused or leaked passwords can pass every check. A rating cannot guarantee password security.

## Learning reflection and next steps

The implementation illustrates how to separate a pure rating function from terminal input. Future improvements could expand the local pattern checks and add regression tests for Unicode and rule boundaries.

