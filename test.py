import unittest
from os import path, getcwd


class TestPackage(unittest.TestCase):
    def test_build(self):
        ROOT = getcwd()
        print(ROOT)
        # Log file will be created if app ran
        log_path = path.join(ROOT, 'dist', 'error.log')
        print(log_path)
        self.assertTrue(path.exists(log_path))

        # Log file will be empty if app ran without any error
        if path.exists(log_path):
            with open(log_path, 'r') as log:
                lines = log.readlines()
                self.assertEqual(len(lines), 0)


if __name__ == '__main__':
    unittest.main()
