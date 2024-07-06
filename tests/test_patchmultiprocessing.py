import unittest
import multiprocessing
from io import StringIO
import sys
from coverage.multiproc import (
    patch_multiprocessing, 
    PATCHED_MARKER, 
    ProcessWithCoverage, 
    original_bootstrap, 
    print_coverage, 
    branch_coverage_multiproc
)

class TestPatchMultiprocessing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rcfile = "dummy_path"
        cls.reset_coverage() 

    @classmethod
    def tearDownClass(cls):
        print("\n\nPrinting Coverage Summary for Multiprocessing Patch:")
        print_coverage() 

    @classmethod
    def reset_coverage(cls):
        for key in branch_coverage_multiproc:
            branch_coverage_multiproc[key] = False

    def setUp(self):
        if hasattr(multiprocessing, PATCHED_MARKER):
            delattr(multiprocessing, PATCHED_MARKER)

    def test_patch_multiprocessing_not_patched(self):
        self.assertFalse(hasattr(multiprocessing, PATCHED_MARKER))
        patch_multiprocessing(self.rcfile)
        self.assertTrue(branch_coverage_multiproc["branch_else"])
        self.assertTrue(hasattr(multiprocessing, PATCHED_MARKER))

    def test_patch_multiprocessing_already_patched(self):
        setattr(multiprocessing, PATCHED_MARKER, True)
        self.assertTrue(hasattr(multiprocessing, PATCHED_MARKER))
        patch_multiprocessing(self.rcfile)
        self.assertTrue(branch_coverage_multiproc["branch_if"])

if __name__ == '__main__':
    unittest.main()