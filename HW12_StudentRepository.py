"""Build a new web page to display the student grades prettytable from HW11 as a web page"""


import os
import sqlite3
from flask import Flask, render_template, redirect
from typing import Dict

app: Flask = Flask(__name__)


@app.route('/')
def index() -> str:
    """Redirect index to students page"""
    return redirect('/repo')


@app.route('/repo')
def student_summary() -> str:
    """ Query for Student Course Grade """
    db_path: str = "G:/Stevens/Courses/Sem4/Assignment/SSW810_Python/StudentRepository_SSW810/input_12/810_startup.db"

    try:
        db: sqlite3.Connection = sqlite3.connect(db_path)
    except sqlite3.OperationalError:
        return f'Error: Unable to open database at path {db_path}'
    else:
        query: str = 'select s.Name, s.CWID, g.Course, g.Grade, i.Name from "students.txt" as s join "grades.txt" as g on s.CWID = g.StudentCWID join "instructors.txt" as i on i.CWID = g.InstructorCWID order by s.Name'
        data: Dict[str, str] = [{'Name': name, 'CWID': cwid, 'Course': course, 'Grade': grade,
                                 'Instructor': instructor} for name, cwid, course, grade, instructor in db.execute(query)]

        db.close()

        return render_template(
            'repo.html',
            title='Stevens Repository',
            table_title='Student, Course, Grade, and Instructor',
            students=data)


app.run(debug=True)
