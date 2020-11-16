""" Name: Vaishnavi Gopalakrishnan
    CWID: 10444180
    Assignment: 8 """

from datetime import datetime, timedelta
import os
from prettytable import PrettyTable
from typing import Tuple
from typing import Iterator, List, Dict


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ This function is used to calculate 
    what is the date after 3 days is given 
    and the differences between two given dates """

    date1: str = "Feb 27, 2020"
    date_2020: datetime = datetime.strptime(
        date1, "%b %d, %Y") + timedelta(3)

    date2: str = "Feb 27, 2019"
    date_2019: datetime = datetime.strptime(
        date2, "%b %d, %Y") + timedelta(3)

    date3: str = "Feb 1, 2019"
    date4: str = "Sep 30, 2019"
    days_passed: int = datetime.strptime(
        date3, "%b %d, %Y") - datetime.strptime(date4, "%b %d, %Y")

    three_days_after_02272020: datetime = date_2020.strftime("%b %d, %Y")
    three_days_after_02272019: datetime = date_2019.strftime("%b %d, %Y")

    days_passed_02012019_09302019: int = abs(days_passed.days)

    return three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019


def file_reader(path: str, fields: int, sep: str = ',', header: bool = 'False') -> Iterator[List[str]]:
    """ This function is used to read file generator """

    try:
        filename = open(path, "r")
    except FileNotFoundError:
        print("Can't open", path)
        raise FileNotFoundError("File not found")
    else:
        line_num: int = 0
        header: bool = True
        with filename:
            for line in filename:
                line_num += 1
                try:
                    sep_line = tuple(line.strip('\n').split(sep))
                    if len(sep_line) != fields:
                        raise ValueError

                except ValueError:
                    print("{} has {} fields on line {}, but expected {} fields.".format(
                        path, len(sep_line), line_num, fields))

                else:
                    if header == True:
                        header = False
                        continue
                    else:
                        yield sep_line


class FileAnalyzer():
    """ This class has two function; one is to read the file and 
    analyze the number of chracters, lines, functions, and classes in a directory
    and other to print the output in a prettytable """

    def __init__(self, directory: str) -> None:
        """ This is the constructor which takes a directory as a parameter """

        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.directory: str = directory
        self.analyze_files()

    def analyze_files(self) -> None:
        """ This function is used to read count each character, 
        line, function, class in a file inside a directory """

        os.chdir(self.directory)

        for fname in os.listdir(self.directory):
            if fname.endswith(".py"):
                try:
                    fp = open(fname, "r")
                except FileNotFoundError:
                    raise FileNotFoundError("File is not there  ")
                else:
                    with fp:
                        linecount: int = 0
                        funcount: int = 0
                        clascount: int = 0
                        chrcount: int = 0

                        for line in fp:
                            chrcount += len(line)
                            line = line.strip()
                            linecount = linecount + 1

                            if line.startswith("def "):
                                funcount = funcount + 1
                            if line.startswith("class "):
                                clascount = clascount + 1

                        self.files_summary[fname] = {
                            "line": linecount, "char": chrcount, "function": funcount, "class": clascount}

                        self.pretty_print()

    def pretty_print(self) -> None:
        """ This function is used to print 
        the result of file summary in pretty table """

        pt: PrettyTable = PrettyTable(
            field_names=["File Name", "Classes", "Functions", "Lines", "Characters"])
        for filename, counting in self.files_summary.items():
            pt.add_row([filename, counting['class'],
                        counting['function'], counting['line'], counting['char']])
        print("\n")
        print(pt)
        return pt
