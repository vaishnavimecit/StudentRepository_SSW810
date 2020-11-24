import unittest
from HW11_StudentRepository import Student, Instructor, University, Major


class TestUniversity(unittest.TestCase):
    """ Tests all the methods in Student Repository """

    def test_Major(self) -> None:
        """ Tests the Major University """
        cwd = "G:/Stevens/Courses/Sem4/Assignment/SSW810_Python/StudentRepository_SSW810/input_11/"
        data: University = University(cwd)
        major_data = {major: maj.get_whole_info()
                      for major, maj in data.majors.items()}
        expected = {
            'SFEN': ['SFEN', {'SSW 540', 'SSW 555', 'SSW 810'}, {'CS 501', 'CS 546'}],
            'CS': ['CS', {'CS 546', 'CS 570'}, {'SSW 565', 'SSW 810'}]}
        self.assertEqual(expected, major_data)

    def test_Instructor(self) -> None:
        """ Tests the instructor """
        cwd = "G:/Stevens/Courses/Sem4/Assignment/SSW810_Python/StudentRepository_SSW810/input_11/"
        data: University = University(cwd)
        instructor_data = {tuple(each_instructor) for inst in data.instructors.values(
        ) for each_instructor in inst.get_instructor_info()}
        expected = {('98764', 'Cohen, R', 'SFEN', 'CS 546', 1),
                    ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4),
                    ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
                    ('98762', 'Hawking, S', 'CS', 'CS 501', 1),
                    ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
                    ('98762', 'Hawking, S', 'CS', 'CS 570', 1)
                    }
        self.assertEqual(instructor_data, expected)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
