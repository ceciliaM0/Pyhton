import unittest
import main

class TestEx8(unittest.TestCase):
    file3 = "C:\\Users\\EBOLOTTI5\\Downloads\\test.txt"
    def test_ex1(self):
        info2 = main.read_log_file(self.file3)
        a = main.ex1(info2)
        self.assertEqual(a, {'BackendApp': {'ERROR': 3, 'DEBUG': 0, 'INFO': 1.5},
                             'FrontendApp': {'ERROR': 1, 'DEBUG': 1, 'INFO': 2.0},
                             'API': {'ERROR': 0, 'DEBUG': 1, 'INFO': 0.5},
                             'SYSTEM': {'ERROR': 0, 'DEBUG': 1, 'INFO': 0}})

    def test_ex3(self):
        info = main.read_log_file(self.file3)
        a = main.ex3(info)
        self.assertEqual(a, {'BackendApp': 3, 'FrontendApp': 1, 'API': 0, 'SYSTEM': 0})

    def test_ex4(self):
        info = main.read_log_file(self.file3)
        a = main.ex4(info)
        self.assertEqual(a, ('BackendApp', 3))

    def test_ex5(self):
        info = main.read_log_file(self.file3)
        a = main.ex5(info)
        self.assertEqual(a, ('FrontendApp', 2.0))

    def teste_ex8(self):
        expected_output = [
            "BackendApp had the most activities at hour 1 with a total of 2 activities",
            "API had the most activities at hour 17 with a total of 2 activities",
            "FrontendApp had the most activities at hour 14 with a total of 3 activities"
        ]
        result = main.ex8("C:\\Users\\EMUSTECJN\\Documents\\python\\test.txt")
        self.assertEqual(result, expected_output)

    def test_ex9(self):
        expected_output = [
            "Failure rate for BackendApp: 50.00%",
            "Failure rate for API: 0.00%",
            "Failure rate for SYSTEM: 0.00%",
            "Failure rate for FrontendApp: 16.67%"
        ]
        result = main.ex9("C:\\Users\\EMUSTECJN\\Documents\\python\\test.txt")
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()