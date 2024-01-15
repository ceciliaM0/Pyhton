import unittest
import main

class TestEx8(unittest.TestCase):
    file3 = "output.txt"

    def test_ex1(self):
        info2 = main.read_log_file()
        a = main.ex1(info2)
        self.assertEqual(a, {'BackendApp': {'ERROR': 3, 'DEBUG': 0, 'INFO': 1.5},
                             'FrontendApp': {'ERROR': 1, 'DEBUG': 1, 'INFO': 2.0},
                             'API': {'ERROR': 0, 'DEBUG': 1, 'INFO': 0.5},
                             'SYSTEM': {'ERROR': 0, 'DEBUG': 1, 'INFO': 0}})

    def test_ex2(self):
        result = main.ex2()
        self.assertIn("Average successful runtime for BackendApp: 16.00 ms", result)
        self.assertIn("Average successful runtime for API: 14.00 ms", result)
        self.assertIn("Average successful runtime for FrontendApp: 19.50 ms", result)

    def test_ex3(self):
        info = main.read_log_file()
        a = main.ex3(info)
        self.assertEqual(a, {'BackendApp': 3, 'FrontendApp': 1, 'API': 0, 'SYSTEM': 0})

    def test_ex4(self):
        info = main.read_log_file()
        a = main.ex4(info)
        self.assertEqual(a, ('BackendApp', 3))

    def test_ex5(self):
        info = main.read_log_file()
        a = main.ex5(info)
        self.assertEqual(a, ('FrontendApp', 2.0))

    def test_ex6(self):
        result = main.ex6()
        self.assertEqual(result, 'The part of the day with the most errors: evening')

    def test_ex7(self):
        result = main.ex7()
        expected_result = [
            "BackendApp - Longest successful run time: 16 ms at timestamp 01:46:48\nBackendApp - Shortest successful run time: 16 ms at timestamp 01:46:48\n\n",
            "API - Longest successful run time: 14 ms at timestamp 17:23:35\nAPI - Shortest successful run time: 14 ms at timestamp 17:23:35\n\n",
            "FrontendApp - Longest successful run time: 25 ms at timestamp 14:40:31\nFrontendApp - Shortest successful run time: 14 ms at timestamp 11:03:29\n\n"
        ]
        self.assertEqual(result, expected_result)

    def teste_ex8(self):
        expected_output = [
            "BackendApp had the most activities at hour 1 with a total of 2 activities",
            "API had the most activities at hour 17 with a total of 1 activities",
            "FrontendApp had the most activities at hour 14 with a total of 2 activities"
        ]
        result = main.ex8("output.txt")
        self.assertEqual(result, expected_output)

    def test_ex9(self):
        expected_output = [
            "Failure rate for BackendApp: 50.00%",
            "Failure rate for API: 0.00%",
            "Failure rate for SYSTEM: 0.00%",
            "Failure rate for FrontendApp: 16.67%"
        ]
        result = main.ex9("output.txt")
        self.assertEqual(result, expected_output)
if __name__ == "__main__":
    unittest.main()
