import runpy
import unittest
from unittest.mock import patch
from io import StringIO
from src.package import module3


class TestModule3(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_function(self, mock_stdout):
        module3.test_unittest()
        self.assertEqual(mock_stdout.getvalue(), "This should be print.\n")


class TestPackageMain(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        runpy.run_module('src.package', run_name="__main__")
        output = (
            "A useful util\n"
            "module1 start:  src.package.module1\n"
            "module1 end\n"
            "module2 start:  src.package.module2\n"
            "module2 end\n"
            "Running a package!\n"
        )
        self.assertEqual(mock_stdout.getvalue(), output)


if __name__ == '__main__':
    unittest.main()
