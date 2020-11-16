# StudentRepository_SSW810
SSW810 Fall 2020 Stevens Database

I have been hired by Stevens Institute of Technology to create a data repository of courses, students, and instructors.  
The system will be used to help students track their required courses, the courses they have successfully completed, their grades,  GPA, etc.  
The system will also be used by faculty advisors to help students to create study plans.  

New features will be added to the solution every week.  

## Iteration 1:
First iteration is to begin the framework for the project and summarize student and instructor data.  Given are three ASCII, tab separated,  data files:

### 1. students.txt
Provides information about each student
Each line has the format: CWID\tName\tMajor (where \t is the <tab> character)

### 2. instructors.txt
Provides information about each instructor
Each line has the format: CWID\tName\tDepartment (where \t is the <tab> character)

### 3. grades.txt (available from Canvas)
Specifies the student CWID, course, and grade for that course, and the instructor CWID
Each line has the format: Student CWID\tCourse\tLetterGrade\tInstructor CWID

#### Read the data from each of the three files and store it in a collection of classes. Create Student and Instructor summary tables. Note that the completed courses are sorted alphabetically. Use CRC Cards with all of the major functionality.
