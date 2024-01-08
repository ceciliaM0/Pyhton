import unittest
import final
class MyTestCase(unittest.TestCase):
    file3="C:\\Users\\EBOLOTTI5\\PycharmProjects\\P1\\t3.txt"
    def test_ex1(self):
        info2=final.read_log_file(self.file3)
        a=final.ex1(info2)
        self.assertEqual(a, {'BackendApp': {'ERROR': 1, 'DEBUG': 3, 'INFO': 1.0}, 'FrontendApp': {'ERROR': 2, 'DEBUG': 5, 'INFO': 2.0}, 'API': {'ERROR': 1, 'DEBUG': 2, 'INFO': 1}, 'SYSTEM': {'ERROR': 1, 'DEBUG': 1, 'INFO': 2} })
    def test_ex3(self):
        info=final.read_log_file(self.file3)
        a=final.ex3(info)
        self.assertEqual(a, {'BackendApp': 1, 'FrontendApp': 2, 'API': 1, 'SYSTEM': 1})
    def test_ex5(self):
        info=final.read_log_file(self.file3)
        a=final.ex5(info)
        self.assertEqual(a, ('FrontendApp', 2.0))
    def test_ex4(self):
        info=final.read_log_file(self.file3)
        a=final.ex4(info)
        self.assertEqual(a, ('FrontendApp', 2.0))
if __name__ == '__main__':
    unittest.main()
