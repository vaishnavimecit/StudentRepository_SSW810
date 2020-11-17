""" This is a test file for Assignment 9 """

import unittest
from HW09_StudentRepository_Vaishnavi_Gopalakrishnan import University


class TestModule(unittest.TestCase):
    """This is a test class """

    def test_correct_student(self) -> None:
        """This is used to test the student pretty table values """
        cwd: str = "G:/Stevens/Courses/Sem4/Assignment/SSW810_Python/StudentRepository_SSW810/input/"
        lis = []
        repo: University = University(cwd)
        for key in repo._students:
            lis.append(repo._students[key].get_student())
        result: list = [['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
                        ['10115', 'Wyatt, X', [
                            'CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
                        ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']],
                        ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']],
                        ['10183', 'Chapman, O', ['SSW 689']],
                        ['11399', 'Cordova, I', ['SSW 540']],
                        ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']],
                        ['11658', 'Kelly, P', ['SSW 540']],
                        ['11714', 'Morton, A', ['SYS 611', 'SYS 645']],
                        ['11788', 'Fuller, E', ['SSW 540']]]
        self.assertEqual(lis, result)

    def test_correct_instructor(self) -> None:
        """This is used to test the instructor pretty table"""
        cwd: str = "G:/Stevens/Courses/Sem4/Assignment/SSW810_Python/StudentRepository_SSW810/input/"
        lis_instructor = []
        repo: University = University(cwd)
        for key in repo._instructors:
            for i in repo._instructors[key].get_instructor():
                lis_instructor.append(i)

        res: list = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4],
                     ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3],
                     ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3],
                     ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3],
                     ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1],
                     ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1],
                     ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1],
                     ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1],
                     ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1],
                     ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1],
                     ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2],
                     ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]

        self.assertEqual(lis_instructor, res)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
