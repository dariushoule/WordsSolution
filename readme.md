Words Test Solution
===================================

### Description of problem

https://gist.github.com/seanthehead/11180933

### Usage

```
python words_solution.py [-h] [-n N] file_in directory_out

An n-length unique sequence generator.

positional arguments:
  file_in
  directory_out

optional arguments:
  -h, --help     show this help message and exit  
  -n N           Sequence length, defaults to 4
```


### Approach

The main component of this solution is a map that associates a sequence of characters to its source word and uniqueness. The UniqueSequenceGenerator is a utility class that facilitates this by accepting whole words and splitting them into N length sequences. At any time the map can be filtered to exclusively unique sequences. 


![Image](class.png?raw=true)

### Structure

```
├── classes
│   ├── UniqueSequenceGenerator.py
│   └── __init__.py
├── inputs
│   ├── dictionary.txt
│   ├── short.txt
│   └── unix_dict.txt
├── outputs
│   ├── dictionary
│   │   ├── sequences
│   │   └── words
│   ├── short
│   │   ├── sequences
│   │   └── words
│   └── unix_dict
│       ├── sequences
│       └── words
├── readme.md
├── tests
│   ├── __init__.py
│   ├── outputs
│   │   └── unix_dict
│   └── test_words.py
└── words_solution.py
```

#### classes 
This module contains the UniqueSequenceGenerator.

#### inputs 
This folder contains sample inputs that can be run against the program.

#### outputs 
This folder contains the sample outputs used to verify the correct behavior of the application.

#### tests 
This module contains the applications unit tests.

#### words_solution.py 
This is the main application entrypoint.


### Testing

Tests can be run from the main project directory using 
``` python -m unittest discover ``` A standard set of tests for the UniqueSequenceGenerator class is available as well as a functionality test for words_solution.py.

The tests include coverage for important and unspecified behavior in the problem description.

#### Unspecified behavior accounted for

- Non alpha characters are stripped from input.
- Input characters are lowercased to prevent duplicate sequences with varying case.


### Whats next?

If I had more time to work on this project these are some of the things I'd look at. 

- Ensuring that the word entry in the map was a reference rather than a copy would prevent widescale duplication of words in the the dictionary. I think this would have the most noticable reduction in memory usage with the least amount of work.
- The memory footprint of the application could probably be reduced further by using a smaller immutable structure over a dict for retaining source word and uniqueness in the map.
- The amount of time spent updating a sequence to flag it as non-unique had much higher processor overhead than inserting a completely new entry. Again, it may be worth investigating a smaller immutable strucuture and overwriting the entry completely rather than updating the dict. 
- When a sequence is flagged as non-unique we no longer need to keep track of the word it was retrieved from. This can lower our memory impact further.

A full breakdown of where the application is spending the majority of its time is available [here](perf-CPU.txt). These performance tests were run on the ``` unix_dict ``` input. Peak memory usage can be examined using ``` python -m memory_profiler words_solution.py inputs/<input> outputs/<output> -n 4 ```. 