import unittest
from coverage.control import Coverage, branch_coverage_current, print_coverage

class TestCoverageCurrent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reset_coverage()

    @classmethod
    def tearDownClass(cls):
        print("\n\nPrinting Coverage Summary for Coverage Current Function:")
        print_coverage()

    @classmethod
    def reset_coverage(cls):
        for key in branch_coverage_current:
            branch_coverage_current[key] = False

    def test_current_no_instances(self):
        self.assertIsNone(Coverage.current())
        self.assertTrue(branch_coverage_current["branch_else_current"])

    def test_current_with_instances(self):
        instance = Coverage()
        Coverage._instances.append(instance)
        self.assertEqual(Coverage.current(), instance)
        self.assertTrue(branch_coverage_current["branch_if_current"])

    def tearDown(self):
        Coverage._instances.clear()

if __name__ == '__main__':
    unittest.main()