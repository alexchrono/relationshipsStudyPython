from sqlalchemy.orm import aliased
from app.factory import create_app, db
from app.models import Student, Course, Teacher
import warnings
from sqlalchemy.exc import SAWarning
import random
warnings.filterwarnings('ignore', category=SAWarning)

app = create_app()


'''WELCOME TO OUR EXERCISE.
step 1:  if you see a venv file to the side, delete it by entering
rm -r venv in the terminal. then pipenv install -r requirements.txt

step2:  open the app/models.py file.  it tells you what kind of relationship to establish for eacch one.
establish those relationships, then come back here and run python GOHERE.py.   if data is printed out,
you are successfull in establishing each relationship.  if you get an error message, you still need
to work on establishing it.

'''
# Test #1: Test many-to-many relationship between students and courses.
# This function will retrieve all students and all courses each student is enrolled in.
def studentsWithCourses():
    session = db.session
    student = aliased(Student)
    course = aliased(Course)

    query = session.query(student.name, course.title).select_from(student).join(student.courses).join(course)
    students_with_courses = query.all()

    if students_with_courses:
        return students_with_courses
    else:
        return "#1 failed. one to many relationship"

# Test #2: Test one-to-many relationship between teachers and courses.
# This function will retrieve all teachers and the courses they teach.
def teachersWithCourses():
    session = db.session
    teacher = aliased(Teacher)
    course = aliased(Course)

    query = session.query(teacher.name, course.title).select_from(teacher).join(Course)
    teachers_with_courses = query.all()

    if teachers_with_courses:
        return teachers_with_courses
    else:
        return "#2 failed. This tests the one-to-many relationship between teachers and courses."

# Test #3: Test one-to-many relationship between a specific teacher and courses.
# This function will retrieve all courses taught by a specific teacher.
def coursesTaughtByTeacher(teacher_name):
    session = db.session
    teacher = aliased(Teacher)
    course = aliased(Course)

    query = session.query(course.title).select_from(teacher).join(Course, Course.teacher_id == teacher.id).filter(teacher.name == teacher_name)
    courses_taught_by_teacher = query.all()

    if courses_taught_by_teacher:
        return courses_taught_by_teacher
    else:
        return f"No courses found for teacher: {teacher_name}"

if __name__ == "__main__":
    with app.app_context():  # Wrap your function calls with this
        print('Teachers with courses*****************')
        print(teachersWithCourses())
        print(' ')
        print(' ')
        print(' ')
        print('Students with courses*******************')
        print(studentsWithCourses())
        print(' ')
        print(' ')
        print(' ')

        # Get all teacher names from the database
        all_teachers = db.session.query(Teacher.name).all()

        # If there are no teachers, print an appropriate message
        if not all_teachers:
            print("No teachers found in the database.")
            exit(0)

        # Randomly choose a teacher's name
        teacher_name_to_query = random.choice(all_teachers)[0]

        # Test the one-to-many relationship between teacher and course
        teacher_courses = coursesTaughtByTeacher(teacher_name_to_query)
        print(f"Courses taught by {teacher_name_to_query}: {teacher_courses}")
