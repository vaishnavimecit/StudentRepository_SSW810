""" This is the test file for Assignment 8 """
import unittest
from StudentRepository_Vaishnavi_Gopalakrishnan import date_arithmetic, file_reader, FileAnalyzer


class TestModuleGeneratorFile(unittest.TestCase):
    def test_date_arithmetic(self) -> None:
        """ This function is used to test date_arithmetic function """
        result1 = date_arithmetic()
        result2 = date_arithmetic()
        self.assertEqual(result1, result2)

    def test_file_reader(self) -> None:
        """ This function is used to test file_reader function """
        path = "G:/Stevens/Courses/Sem4/Assignment/SSW810_Python/Assignment8/input/student_majors.txt"

        file = file_reader(path, 3, '|', header=True)

        self.assertTrue(next(file) == (
            '123', 'Jin He', 'Computer Science'))
        self.assertTrue(next(file) == (
            '234', 'Nanda Koka', 'Software Engineering'))
        self.assertTrue(next(file) == (
            '345', 'Benji Cai', 'Software Engineering'))

    def test_analyze_files(self) -> None:
        """ This function is used to test_analyze_files function """

        directory = "G:/Stevens/Courses/Sem4/Assignment/SSW810_Python/Assignment8/input"

        expect = {'0_defs_in_this_file.py':
                  {'class': 0, 'function': 0, 'line': 3, 'char': 56},
                  'file1.py':
                  {'class': 2, 'function': 4, 'line': 28, 'char': 274}}

        fa = FileAnalyzer(directory)
        self.assertEqual(fa.files_summary, expect)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
