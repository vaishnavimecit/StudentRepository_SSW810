""" Name: Vaishnavi Gopalakrishnan
    CWID: 10444180
    Assignment: 9 """

from datetime import datetime, timedelta
from collections import defaultdict
import os
from prettytable import PrettyTable
from typing import Tuple, Iterator, List, Dict
from HW08_StudentRepository_Vaishnavi_Gopalakrishnan import file_reader


class Student:
    """This is Student class with the Pretty Table fields"""
<<<<<<< Updated upstream
    PT_FIELD = ['CWID', 'Name', 'Completed Course']

    def __init__(self, id, name, dept):
        """This is Student class which stores CWID,Name,Completed Course and a dictionary"""
        self._cwid = id
        self._name = name
        self._dept = dept
        self._course_dict = defaultdict(str)

    def set_grades(self, course, grade):
        """setting the _course_dict with {course: grade}"""
        self._course_dict[course] = grade

    def get_student(self):
=======
    PT_FIELD: list = ['CWID', 'Name', 'Completed Course']

    def __init__(self, id: str, name: str, dept: str) -> None:
        """This is Student class which stores CWID,Name,Completed Course and a dictionary"""
        self._cwid: str = id
        self._name: str = name
        self._dept: str = dept
        self._course_dict = defaultdict(str)

    def set_grades(self, course: str, grade: str) -> None:
        """setting the _course_dict with {course: grade}"""
        self._course_dict[course] = grade

    def get_student(self) -> list:
>>>>>>> Stashed changes
        """returns cwid,name,_course_dict.keys (sorted)"""
        return [self._cwid, self._name, sorted(self._course_dict.keys())]


class Instructor:
    """This is Instructor class with a variable to with the Pretty Table fields"""
<<<<<<< Updated upstream
    PT_FIELD = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, id, name, dept):
        """This initializes the cwid,name,dept and a default dict(int) of the instructor"""
        self._cwid = id
        self._name = name
        self._dept = dept
        self._student_dict = defaultdict(int)

    def set_students(self, course):
        """increments the count of the student associated with the grade """
        self._student_dict[course] += 1

    def get_instructor(self):
=======
    PT_FIELD: list = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, id: str, name: str, dept: str) -> None:
        """This initializes the cwid,name,dept and a default dict(int) of the instructor"""
        self._cwid: str = id
        self._name: str = name
        self._dept: str = dept
        self._student_dict = defaultdict(int)

    def set_students(self, course: str) -> None:
        """increments the count of the student associated with the grade """
        self._student_dict[course] += 1

    def get_instructor(self) -> list:
>>>>>>> Stashed changes
        """returns cwid,name,dept and _student_dict"""
        for key, value in self._student_dict.items():
            yield ([self._cwid, self._name, self._dept, key, value])


class University:
    """This the University class"""

<<<<<<< Updated upstream
    def __init__(self, dir_path, ptable=False):
=======
    def __init__(self, dir_path: str, ptable: bool = False) -> None:
>>>>>>> Stashed changes
        """This initializes the student dict , instructor dict and opens these three files"""
        self._students = {}
        self._instructors = {}
        self._get_students(os.path.join(dir_path, "students.txt"))
        self._get_instructors(os.path.join(dir_path, "instructors.txt"))
        self._get_grades(os.path.join(dir_path, "grades.txt"))
        if ptable:
            self.student_prettytable()
            self.instructor_prettytable()

<<<<<<< Updated upstream
    def _get_students(self, path):
=======
    def _get_students(self, path: str) -> None:
>>>>>>> Stashed changes
        """this function reads the students.txt file and stores it in a dict{cwid:Student}"""
        try:
            for cwid, name, major in file_reader(path, 3, sep='\t', header=False):
                # print(cwid)
                self._students[cwid] = Student(cwid, name, major)
        except FileNotFoundError as fnfe:
            print(fnfe)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)

<<<<<<< Updated upstream
    def _get_instructors(self, path):
=======
    def _get_instructors(self, path: str) -> None:
>>>>>>> Stashed changes
        """this function reads the instructors.txt file and stores it in a dict{cwid:Instructor}"""
        try:
            for cwid, name, dept in file_reader(path, 3, sep='\t', header=False):
                # print(cwid)
                self._instructors[cwid] = Instructor(cwid, name, dept)
        except FileNotFoundError as fnfe:
            print(fnfe)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)

<<<<<<< Updated upstream
    def _get_grades(self, path):
=======
    def _get_grades(self, path: str) -> None:
>>>>>>> Stashed changes
        """This function reads the grade.txt and adds the items in the Student and teh Instructor instance"""
        try:
            for student_cwid, course, grade, instructor_cwid in file_reader(path, 4, sep='\t', header=False):
                # print(student_cwid, instructor_cwid)
                if student_cwid in self._students:
                    self._students[student_cwid].set_grades(course, grade)
                else:
                    print(f"Found grade for an unknown student {student_cwid}")
                if instructor_cwid in self._instructors:
                    self._instructors[instructor_cwid].set_students(course)
                else:
                    print(
                        f"Found grade for unknown instructor {instructor_cwid}")
        except FileNotFoundError as fnfe:
            print(fnfe)
        except ValueError as ve:
            print(ve)

<<<<<<< Updated upstream
    def student_prettytable(self):
=======
    def student_prettytable(self) -> None:
>>>>>>> Stashed changes
        """prints the student pretty table"""
        print("Student Summary")
        pt_student = PrettyTable(Student.PT_FIELD)
        for key in self._students:
            pt_student.add_row(self._students[key].get_student())
        print(pt_student)

<<<<<<< Updated upstream
    def instructor_prettytable(self):
=======
    def instructor_prettytable(self) -> None:
>>>>>>> Stashed changes
        """prints the instructor pretty table"""
        print("Instructor Summary")
        pt_instructor = PrettyTable(Instructor.PT_FIELD)
        for key in self._instructors:
            for i in self._instructors[key].get_instructor():
                pt_instructor.add_row(i)
        print(pt_instructor)


<<<<<<< Updated upstream
def main():
    cwd = "G:/Stevens/Courses/Sem4/Assignment/SSW810_Python/StudentRepository_SSW810/input/"
=======
def main() -> None:
    cwd: str = "G:/Stevens/Courses/Sem4/Assignment/SSW810_Python/StudentRepository_SSW810/input/"
>>>>>>> Stashed changes
    University(cwd, ptable=True)


if __name__ == "__main__":
    main()
