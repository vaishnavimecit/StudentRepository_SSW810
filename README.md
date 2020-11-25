# StudentRepository_SSW810

SSW810 Fall 2020 Stevens Database

I have been hired by Stevens Institute of Technology to create a data repository of courses, students, and instructors.  
The system will be used to help students track their required courses, the courses they have successfully completed, their grades, GPA, etc.  
The system will also be used by faculty advisors to help students to create study plans.

New features will be added to the solution every week.

## Iteration 1:

First iteration is to begin the framework for the project and summarize student and instructor data. Given are three ASCII, tab separated, data files:

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

## Iteration 2:

1. Add the new functionality to compute the student's GPA

2. Add new functionality to read the majors file and calculate the remaining required and elective classes for each student

3. Add a new Majors prettytable

4. Update the Student prettytable to include the student's GPA and remaining classes and electives for each student

5. Implement automated tests to verify that the data in the prettytables matches the data from the input data files.

## Iteration 3
1. Create a new SQLite database
2. Import input files into your database
3. Use DataGrip to open your new SQLite database and import the four files into your database as separate tables. 
4. Run queries to answer the following questions.  Submit screen dumps of DataGRIP to show your query and results for each of the following queries:
What is the name of the student with CWID='10115'   (NOTE: if you don't find any matching records then verify that the CWID has type TEXT in all four tables.   Integers don't match strings in SQL or Python.)
What is the total number of students by major?  Hint:  you'll need count(*) and 'group by'.  See the slide on "Aggregate functions and GROUP BY".
What is the most frequent grade for SSW 810 across all students?
Display the name and cwid of each student along with the total number of courses taken by the student.   Hint: You'll need to join the students and grades tables on StudentCWID and CWID.
Display each student's name,  CWID, course, grade, and the instructor's name  for all students and grades.  The result should be sorted by the student's name. Hint: You'll need to join the grades and students tables on StudentCWID and CWID and join the instructors table using the instructor's CWID.  E.g. Bezos, J, CWID 10115, earned an 'A' in SSW 810 taught by Rowland.
5. Create a new branch in your GitHub repository for HW11 from your HW10 assignment and add the following new features to your code:
Update your code to use the new data files that use '\t' to separate the fields and each file has a header record
Add a new student_grades_table_db(self, db_path) method to your Repository class to create a new student grades PrettyTable that retrieves the data for the table from the database you created above using 'db_path' to specify the path of your SQLite database file.  Use Python calls to execute the student grades summary query you defined above and use the data from executing the query to generate and display a student grades PrettyTable with the results.
Add a new automated test to verify that the data retrieved from the database matches the expected rows.
6. Add your database file to your GitHub repository. 

## Iteration 4
Build a new web page to display the new student grades prettytable from HW11 as a web page.

Install Flask along with the database created for Homework 11.  

1. Create a directory structure for your solution with a 'templates' subdirectory, and a base.html template.
2. Define a query using your SQLite database from Homework 11 that calculates the Student's name, CWID, the name of the course, grade earned, and the instructor's name.
3. Create a new template file for your new web page.  Create an HTML with static data to test your HTML.
4. Update the static HTML to include Jinja2 variables and statements to use data passed with the render_template() call.
5. Create a Flask Python application to run your application.
6. Demonstrate that your code works properly by submitting a .zip file with all of the files from your solution plus a screen dump of your browser showing the output.
7. Update your GitHub repository to include a new branch with the web solution. 
8. After that, celebrate the fact that you've completed your last homework assignment for SSW 810!
