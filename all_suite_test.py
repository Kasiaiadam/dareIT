import unittest

from unittest.loader import makeSuite

from test_cases.fill_in_player_form import TestFillForm
from test_cases.framework import Test
from test_cases.add_a_new_player import TestAddPlayer
from test_cases.change_language import TestChangeLanguage
from test_cases.clear_player_form import TestClearForm
from test_cases.download_csv import TestDownloadCSV
from test_cases.login_to_the_system import TestLoginPage
from test_cases.logout_from_the_system import TestLogoutPage


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestFillForm))
    test_suite.addTest(makeSuite(Test))
    test_suite.addTest(makeSuite(TestAddPlayer))
    test_suite.addTest(makeSuite(TestChangeLanguage))
    test_suite.addTest(makeSuite(TestClearForm))
    test_suite.addTest(makeSuite(TestDownloadCSV))
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestLogoutPage))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
