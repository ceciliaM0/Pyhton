import unittest
import final
class MyTestCase(unittest.TestCase):
    file3="C:\\Users\\EBOLOTTI5\\Downloads\\test.txt"
    def test_ex1(self):
        info2=final.read_log_file(self.file3)
        a=final.ex1(info2)
        self.assertEqual(a, {'BackendApp': {'ERROR': 3, 'DEBUG': 0, 'INFO': 1.5}, 'FrontendApp': {'ERROR': 1, 'DEBUG': 1, 'INFO': 2.0}, 'API': {'ERROR': 0, 'DEBUG': 1, 'INFO': 0.5}, 'SYSTEM': {'ERROR': 0, 'DEBUG': 1, 'INFO': 0} })
    def test_ex3(self):
        info=final.read_log_file(self.file3)
        a=final.ex3(info)
        self.assertEqual(a, {'BackendApp': 3, 'FrontendApp': 1, 'API': 0, 'SYSTEM': 0})
    def test_ex5(self):
        info=final.read_log_file(self.file3)
        a=final.ex5(info)
        self.assertEqual(a, ('FrontendApp', 2.0))
    def test_ex4(self):
        info=final.read_log_file(self.file3)
        a=final.ex4(info)
        self.assertEqual(a, ('BackendApp', 3))
if __name__ == '__main__':
    unittest.main()
