import unittest
import sys
import os

PARENT_DIR = os.path.dirname(__file__)
sys.path.append(PARENT_DIR)

# Add the directory to the Python path, to eliminate import errors
TEST_DIR = os.path.join(PARENT_DIR, "expense_management")
sys.path.append(TEST_DIR)
TEST_DIR = os.path.join(PARENT_DIR, "reporting_tools")
sys.path.append(TEST_DIR)

from expense_management.test_expense_manager import TestExpenseManager
from expense_management.test_manager import TestManager
from expense_management.test_user_manager import TestUserManager


def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestExpenseManager('test_add_expense'))
    suite.addTest(TestExpenseManager('test_remove_expense'))
    suite.addTest(TestExpenseManager('test_list_expenses'))
    suite.addTest(TestExpenseManager('test_settle_debt'))

    suite.addTest(TestManager('test_manager_name'))
    suite.addTest(TestManager('test_str_method'))

    suite.addTest(TestUserManager('test_add_user'))
    suite.addTest(TestUserManager('test_remove_user'))
    suite.addTest(TestUserManager('test_list_users'))

    #add your code here


    return suite

if __name__ == "__main__":
    test_suite = suite()
    result = unittest.TestResult()
    print("Running Test Suite...")
    test_suite.run(result)

    print("\n--- Test Results ---")
    print(f"Tests Run: {result.testsRun}")
    print(f"Errors: {len(result.errors)}")
    print(f"Failures: {len(result.failures)}")

    #print errors
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"{test}: {traceback}")

    #print failures
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"{test}: {traceback}")


