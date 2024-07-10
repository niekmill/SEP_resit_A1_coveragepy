Report for Assignment 1 Resit
==============================

## Project Chosen

- **Name:** Coveragepy
- **URL:** `https://github.com/nedbat/coveragepy/tree/master`
- **Number of lines of code and the tool used to count it:** 971,593 lines with lizard
- **Programming language:** Python

## Coverage Measurement with Existing Tool

- **Tool Used:** Coverage.py
- **Execution Method:** The Coverage.py tool was executed using the command `coverage run -m unittest discover` to run all the unit tests and then `coverage report` to generate the initial coverage report.
- **Coverage Results:**

  ![Coverage Results](https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/coverageresultOG.png)

## Coverage Improvement

### Individual Tests

#### Function 1: `patch_multiprocessing`

- **Patch or Commit Link:** 
  - Instrumentation commit: [Commit Link](https://github.com/niekmill/SEP_resit_A1_coveragepy/commit/1d78fd554ae6ee0c42273c9e5d0fba5d88dd70e7)
  - Test creation commit: [Commit Link](https://github.com/niekmill/SEP_resit_A1_coveragepy/commit/49a3c9b1b7844a8bcffed5fcf8202833976d442b)

- **Old Coverage Results:** 

  ![Old Coverage Results](https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/multiproccovresult.png)

- **New Coverage Results:** 

  ![New Coverage Results](https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/newmultiprocresult.png)

- **Coverage Improvement:** From X% to 100%
- **Elaboration:** Added test cases to cover all cases of input, resulting in better branch coverage.

#### Function 2: `current`

- **Patch or Commit Link:** 
  - Instrumentation commit: [Commit Link](https://github.com/niekmill/SEP_resit_A1_coveragepy/commit/66104fb0c920de9b044fcbed525c0efa6da1c08c)
  - Test creation commit: [Commit Link](https://github.com/niekmill/SEP_resit_A1_coveragepy/commit/5a68a2143c837d61b23139c86f10df6cd119f101)

- **Old Coverage Results:** 

  ![Old Coverage Results](https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/currentcovresult.png)

- **New Coverage Results:** 

  ![New Coverage Results](https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/newcurrentresult.png)

- **Coverage Improvement:** From X% to 100%
- **Elaboration:** Added test cases to cover all cases of input, resulting in better branch coverage.

### Overall

- **Old Coverage Results:** 

  ![Old Coverage Results](https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/coverageresultOG.png)

- **New Coverage Results:** 

  ![New Coverage Results](https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/coverageresultNEW.png)
