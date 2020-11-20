""" Name: Vaishnavi Gopalakrishnan
    CWID: 10444180
    Assignment: 10 """

from datetime import datetime, timedelta
from collections import defaultdict
import os
from prettytable import PrettyTable
from typing import Tuple, Iterator, List, Dict
from HW08_StudentRepository_Vaishnavi_Gopalakrishnan import file_reader


class Student:
    """
    Stores information about a SINGLE student with all of the relevant information including:
    CWID, name, major, courses with corresponding grades.
    """

    def __init__(self, person_info, major_info):
        """ CWID: str; name: str; major: str; courses: defaultdict(str) """
        if len(person_info) == 2 or any([item.isspace() for item in person_info]) or '' in person_info:
            raise ValueError("Missing basic information of students!")

        self.CWID, self.name, self.major = person_info
        self.major_info = major_info  # all major info including required and elective courses
        self.courses = defaultdict(str)

    def add_course(self, course, grade):
        """ Key: course, Value: grade
            Update courses each time finding a course info """
        self.courses[course] = grade

    def gpa(self) -> float:
        """Calculate the GPA using dictionary"""
        grades: Dict[str, float] = {'A': 4.0, 'A-': 3.75, 'B+': 3.25, 'B': 3.0, 'B-': 2.75,
                                    'C+': 2.25, 'C': 2.0, "C-": 0.00, "D+": 0.00, "D": 0.00, "D-": 0.00, "F": 0.00}
        try:
            total: float = sum(
                [grades[grade] for grade in self.courses.values()]) / len(self.courses.values())
            return round(total, 2)
        except ZeroDivisionError as e:
            print(e)

    def get_whole_info(self):
        """ return whole info of students including grades """
        return [self.CWID, self.name, self.major, self.courses, self.gpa]

    def get_student_info(self):
        """ return the details for a single student in a list
            Note: a student may just registered in the college having no course info """
        if not self.courses.items():
            return [self.CWID, self.name, self.major, None, None, None, None]
        else:
            return [self.CWID, self.name, self.major, sorted(list(self.courses.keys())), self.gpa()]


class Instructor:
    """
    Stores information about a single Instructor with all of the relevant information including:
    CWID, name, department, courses with corresponding students number
    """

    def __init__(self, person_info):
        """ CWID: str; name: str; department: str; courses: defaultdict(int) """
        if len(person_info) == 2 or any([item.isspace() for item in person_info]) or '' in person_info:
            raise ValueError("Missing basic information of instructors!")

        self.CWID, self.name, self.department = person_info
        self.courses = defaultdict(int)

    def add_course(self, course):
        """ Key: course, Value: nunber of students
            Update courses by adding 1 to its value each time found one person taking this course """

        self.courses[course] += 1

    def get_whole_info(self):
        """ return whole info of instructors """
        return [self.CWID, self.name, self.department, self.courses]

    def get_instructor_info(self):
        """ return the details for a single instructor in a list
            Note: for one instructor, there might be several courses and he might have no course info """
        info = list()
        if not self.courses.items():
            info.append([self.CWID, self.name, self.department, None, None])
        else:
            for course, student_num in self.courses.items():
                info.append(
                    [self.CWID, self.name, self.department, course, student_num])
        return info


class Major:
    """
    Store information about all majors.
    Major, Required course, Electives
    """

    def __init__(self, major):
        """ instance attributes: major, required courses, elective courses"""
        self.major = major

        self.required = set()
        self.elective = set()

    def update_major(self, flag, course):
        """ update the required courses('R') and the electives('E') """
        if flag == 'R':
            self.required.add(course)
        elif flag == 'E':
            self.elective.add(course)
        else:
            raise ValueError("Error! Unknown course flag!")

    def get_major_info(self):
        """ return the info for prettytable"""
        return [self.major, sorted(list(self.required)), sorted(list(self.elective))]

    def update_courses_info(self, courses):
        """ calculate the successfully completed courses, remaining required, elective courses"""
        passed_grades = ('A', 'A-', 'B+', 'B', 'B-', 'C+',
                         'C')  # the grades needed to pass the course

        completed_courses = set()
        for course, grade in courses.items():
            if grade == ' ':  # in case there is no grade for the course yet
                continue
            elif grade in passed_grades:
                completed_courses.add(course)

        remaining_required = self.left_required(completed_courses)
        remaining_electives = self.left_electives(completed_courses)

        return [sorted(list(completed_courses)), remaining_required, remaining_electives]

    def left_required(self, courses):
        """ return remaining required courses """
        if self.required.difference(courses) == set():  # no required course left
            return None
        else:
            return sorted(list(self.required.difference(courses)))

    def left_electives(self, courses):
        """ return remaining electives """
        left_courses = self.elective.difference(courses)
        if len(left_courses) < len(self.elective):  # at least one elective course is needed
            return None
        else:  # no elective courses has been completed
            return sorted(list(self.elective))

    def get_whole_info(self):
        """ return all info for the major """
        return [self.major, self.required, self.elective]


class University:
    """ Store all the information for all students and instructors """

    def __init__(self, dir_path):
        """ Specifies a directory path where to find the students.txt, instructors.txt, and grades.txt files """
        self.students_path = os.path.join(dir_path, 'students.txt')
        self.instructors_path = os.path.join(dir_path, 'instructors.txt')
        self.grades_path = os.path.join(dir_path, 'grades.txt')
        self.majors_path = os.path.join(dir_path, 'majors.txt')

        # initialize the students DB, key is CWID, value is instance of Student
        self.students = dict()
        # initialize the instructors DB, key is CWID, value is instance of Instructor
        self.instructors = dict()
        self.majors = dict()  # key is major, value is instance of Major

        # run methods to generate majors DB, students DB and instructors DB and print the table of them
        self.majors_DB()
        self.students_DB()
        self.instructors_DB()
        self.grades_DB()

        self.print_major_table()
        self.print_student_table()
        self.print_instructor_table()

    def students_DB(self):
        """ Structure: CWID, Name, Major
            reading in the students.txt file line by line, updating the basic info for one student
            also for each instance of students, passing in major info
        """
        for person_info in file_reader(self.students_path, 3, sep=';', header=True):
            CWID, name, major = person_info

            if major not in self.majors:
                raise ValueError(
                    'Error! Missing major {} information.'.format(major))

            if CWID not in self.students:
                self.students[CWID] = Student(person_info, self.majors[major])

    def instructors_DB(self):
        """ Structure: CWID, Name, Department
            reading in the instructors.txt file line by line, updating the basic info for one instructor
        """
        for person_info in file_reader(self.instructors_path, 3, sep='|', header=True):
            self.instructors[person_info[0]] = Instructor(person_info)

    def grades_DB(self):
        """ Structure: CWID_student, Course, Grade, CWID_instructor """
        for CWID_stu, course, grade, CWID_ins in file_reader(self.grades_path, 4, sep='|', header=True):
            if CWID_stu not in self.students.keys():  # course info in grades.txt but no corresponding student is found
                raise ValueError(
                    'Student CWID {} is not in the student system.'.format(CWID_stu))

            # course info in grades.txt but no corresponding instructor is found
            if CWID_ins not in self.instructors.keys():
                raise ValueError(
                    'Instructor CWID {} is not in the instructor system.'.format(CWID_stu))

            # add a course and grade to the student containers
            self.students[CWID_stu].add_course(course, grade)
            # add a course and increment the number of students by 1 to the instructor containers
            self.instructors[CWID_ins].add_course(course)

    def majors_DB(self):
        """ Structure: Department, Flag, Course
            Method:
                If major is already in the dict, then ignore, just update info.
                As each time declare an instance, the required and electives would be an emplty set,
                this would avoid clean the set by mistake.
        """
        for major, flag, course in file_reader(self.majors_path, 3, sep='\t', header=True):
            if major not in self.majors:
                self.majors[major] = Major(major)

            self.majors[major].update_major(flag, course)

    def print_student_table(self):
        """ generate the prettytable for students summary """
        pt = PrettyTable(field_names=[
                         'CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives', 'GPA'])
        for person in self.students.values():
            # calculating remaining required and elective courses
            courses = self.majors[person.major].update_courses_info(
                person.courses)

            CWID, name, major, c, GPA = person.get_student_info()

            person_info = [CWID, name, major, GPA]
            for item in courses:
                person_info.append(item)

            pt.add_row(person_info)
        print('Students Summary')
        print(pt)

    def print_instructor_table(self):
        """ generate the prettytable for instructors summary """
        pt = PrettyTable(
            field_names=['CWID', 'Name', 'Department', 'Courses', 'Student Num'])
        for person in self.instructors.values():
            for item in person.get_instructor_info():
                pt.add_row(item)
        print('Instructors Summary')
        print(pt)

    def print_major_table(self):
        """ generate the prettytable for majors summary """
        pt = PrettyTable(
            field_names=['Major', 'Required Courses', 'Electives'])
        for major in self.majors.values():
            pt.add_row(major.get_major_info())

        print('Majors Summary')
        print(pt)


def main() -> None:
    cwd: str = "G:/Stevens/Courses/Sem4/Assignment/SSW810_Python/StudentRepository_SSW810/input_10/"
    University(cwd)


if __name__ == "__main__":
    main()
