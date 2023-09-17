from sqlalchemy.orm import aliased
from dotenv import load_dotenv
from app.factory import create_app, db
from app.models import Student, Course, Teacher
import warnings
from sqlalchemy.exc import SAWarning
import random
warnings.filterwarnings('ignore', category=SAWarning)

load_dotenv()

app = create_app()

'''WELCOME TO OUR EXERCISE.
STEP 0:  if you see a venv file to the side, delete it by entering
rm -r venv in the terminal. then pipenv install -r requirements.txt

STEP 1:  go to app/models.py Make a many to many relationship between students and courses.  you will need to
make an association table.
then, init a database.  make a migration.  upgrade.  and run python seeder.py
then uncomment the first test in GOHERE.PY.  run python GOHERE.PY to test
'''
# ************ Test #1: many-to-many relationship between students and courses.********************
# This function will retrieve two students and all the courses each student is enrolled
# in.
# this tests the many-to-many relationship between students and courses. uncomment all below


# def studentsWithCourses():
#     session = db.session
#     student = aliased(Student)
#     course = aliased(Course)

#     query = session.query(student.name, course.title).select_from(student).join(student.courses).join(course)
#     students_with_courses = query.limit(2).all()

#     if students_with_courses:
#         return students_with_courses
#     else:
#         return "#1 failed. one to many relationship between students and courses failed"


# with app.app_context():

#     print('Students with courses*******************')
#     print('many to many relationship between students and courses is operational')
#     print(studentsWithCourses())
#     print(' ')
#     print(' ')
#     print(' ')

# # STEP 2:  go to app/models.py Make a one to many relationship between teachers and courses.
# # think of a course as philosophy 101 taught at 9.am.  one teacher per course.
# # you will need to make an association table. then uncomment the below test.  run python GOHERE.PY to test

# ****************Test #2: one-to-many relationship between teacher and courses.**********
# This function will retrieve all courses taught by a specific teacher.
# def coursesTaughtByTeacher(teacher_name):
#     session = db.session
#     teacher = aliased(Teacher)
#     course = aliased(Course)
#     query = session.query(course.title).select_from(teacher).join(Course, Course.teacher_id == teacher.id).filter(
#         teacher.name == teacher_name)
#     courses_taught_by_teacher = query.all()
#     if courses_taught_by_teacher:
#         return courses_taught_by_teacher
#     else:
#         return f"No courses found for teacher: {teacher_name}"


# with app.app_context():
#     all_teachers = db.session.query(Teacher.name).all()
#     if not all_teachers:
#         print("No teachers found in the database.")
#         exit(0)
#     teacher_name_to_query = random.choice(all_teachers)[0]
#     teacher_courses = coursesTaughtByTeacher(teacher_name_to_query)
#     print(' ')
#     print(' ')
#     print('*************#2  courses taught by teacher**************')
#     print('one to many relationship between courses and students is operational')
#     print(f"Courses taught by {teacher_name_to_query}: {teacher_courses}")

# # STEP 3:  Go to models.py and make a many to many relationship between teachers and
# # students. upgrade the db. uncomment all below asterisks to test.
# # ****************Test #3: many-to-many relationship between teachers and students.**********
# # This function will retrieve all the students that one teacher has.

# def studentsTaughtByTeacher(teacher_name, all_teachers):
#     with app.app_context():
#         teacher = Teacher.query.filter_by(name=teacher_name).first()

#         if teacher:
#             students_taught_by_teacher = teacher.students
#             return [teacher_name, students_taught_by_teacher]
#         else:
#             return f"No students found for teacher: {teacher_name}"

# # Get a random teacher name from all_teachers
# teacher_name_to_query = random.choice(all_teachers)[0]

# goal = studentsTaughtByTeacher(teacher_name_to_query, all_teachers)
# print(' ')
# print(' ')
# print('*************#3  students taught by teacher**************')
# print('many-to-many relationship between teachers and students is operational')
# print(f"Students taught by {goal[0]}: {goal[1]}")
