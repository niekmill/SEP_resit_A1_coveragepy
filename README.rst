Report for Assignment 1 Resit
==============================

Project Chosen:
--------------------------

- **Name:** Coveragepy
- **URL:** `https://github.com/nedbat/coveragepy/tree/master`
- **Number of lines of code and the tool used to count it:** 971593 lines with lizard
- **Programming language:** Python

Coverage Measurement with Existing Tool
----------------------------------------

- **Tool Used:** Coverage.py
- **Execution Method:** `<How the tool was executed>`
- **Coverage Results:**

  .. image:: https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/coverageresultOG.png
     :width: 600
     :align: center

  *Add a brief description of the coverage results if needed.*

Coverage Improvement
---------------------

Individual Tests
----------------

Function 1: patch_multiprocessing
---------------------------------

- **Patch or Commit Link:** :github:`1d78fd554ae6ee0c42273c9e5d0fba5d88dd70e7`
- **Old Coverage Results:** 

  .. image:: https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/multiproccovresult.png
     :width: 400
     :align: center

- **New Coverage Results:** 

  .. image:: https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/newmultiprocresult.png
     :width: 400
     :align: center

- **Coverage Improvement:** 100%
- **Elaboration:** Added test cases to cover all cases of input, resulting in better branch coverage

Function 2: current
--------------------

- **Patch or Commit Link:** :github:`66104fb0c920de9b044fcbed525c0efa6da1c08c`
- **Old Coverage Results:** 

  .. image:: https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/currentcovresult.png
     :width: 400
     :align: center

- **New Coverage Results:** 

  .. image:: https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/newcurrentresult.png
     :width: 400
     :align: center

- **Coverage Improvement:** 100%
- **Elaboration:** Added test cases to cover all cases of input, resulting in better branch coverage

Overall
-------

- **Old Coverage Results:** 

  .. image:: https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/coverageresultOG.png
     :width: 600
     :align: center

- **New Coverage Results:** 

  .. image:: https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/coverageresultNEW.png
     :width: 600
     :align: center
