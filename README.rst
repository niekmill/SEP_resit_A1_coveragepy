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
- **Execution Method:** The existing tool was used through my mac terminal after fixing many failures and errors. I ran it with coverage run -m pytest and then coverage report to see the results.
- **Coverage Results:**

  .. image:: https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/coverageresultOG.png
     :width: 1200
     :align: center


Coverage Improvement
---------------------


Function 1: patch_multiprocessing
---------------------------------

- **Patch or Commit Link:** 
    Test creation commit: https://github.com/niekmill/SEP_resit_A1_coveragepy/commit/49a3c9b1b7844a8bcffed5fcf8202833976d442b

- **Old Coverage Results:** 

  .. image:: https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/oldpatchmultiprocessing.png
     :width: 1200
     :align: center

- **New Coverage Results:** 

  .. image:: https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/improvedcovresult.png
     :width: 1200
     :align: center

- **Coverage Improvement:** 29.5%
- **Elaboration:** Added test cases to cover all cases of input, resulting in better branch coverage

Function 2: current
--------------------

- **Patch or Commit Link:** 
    Test creation commit: https://github.com/niekmill/SEP_resit_A1_coveragepy/commit/5a68a2143c837d61b23139c86f10df6cd119f101

- **Old Coverage Results:** 

  .. image:: https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/oldcurrent.png
     :width: 1200
     :align: center

- **New Coverage Results:** 

  .. image:: https://github.com/niekmill/SEP_resit_A1_coveragepy/raw/main/images/improvedcovresult2.png
     :width: 1200
     :align: center

- **Coverage Improvement:** 40%
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
