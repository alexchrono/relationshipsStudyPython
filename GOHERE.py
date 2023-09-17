# from sqlalchemy.orm import aliased
# from app.factory import create_app, db
# from app.models import Student, Course, Enrollment, Teacher

# # Create a Flask app context
# app = create_app()

# # Create a SQLAlchemy session within the app context
# with app.app_context():
#     # Create a SQLAlchemy session
#     session = db.session

#     def studentsWithCourses():
#         # Explicitly alias the Student and Course tables to avoid ambiguity
#         student = aliased(Student)
#         course = aliased(Course)

#         # Specify the left side of the join using select_from
#         query = session.query(student.name, course.title).select_from(student).join(Enrollment).join(course)
#         students_with_courses = query.all()

#         if students_with_courses:
#             return students_with_courses
#         else:
#             return "#4 failed. This tests the many-to-many relationship between students and courses."

#     def teachersWithCourses():
#         # Explicitly alias the Teacher and Course tables to avoid ambiguity
#         teacher = aliased(Teacher)
#         course = aliased(Course)

#         # Specify the left side of the join using select_from
#         query = session.query(teacher.name, course.title).select_from(teacher).join(Course)
#         teachers_with_courses = query.all()

#         if teachers_with_courses:
#             return teachers_with_courses
#         else:
#             return "#2 failed. This tests the one-to-many relationship between teachers and courses."

#     # Add your other functions as needed

#     if __name__ == "__main__":
#         print('Teachers with courses*****************', teachersWithCourses())
#         print('                       ')
#         print(' ')
#         print('Students with courses*******************', studentsWithCourses())
#         # Add calls to your other functions here as needed



from sqlalchemy.orm import aliased
from app.factory import create_app, db
from app.models import Student, Course, Enrollment, Teacher
import warnings
from sqlalchemy.exc import SAWarning
warnings.filterwarnings('ignore', category=SAWarning)

# Create a Flask app context
app = create_app()

# Create a SQLAlchemy session within the app context
with app.app_context():
    # Create a SQLAlchemy session
    session = db.session

    def studentsWithCourses():
        # Explicitly alias the Student and Course tables to avoid ambiguity
        student = aliased(Student)
        course = aliased(Course)

        # Specify the left side of the join using select_from
        query = session.query(student.name, course.title).select_from(student).join(Enrollment).join(course)
        students_with_courses = query.all()

        if students_with_courses:
            return students_with_courses
        else:
            return "#4 failed. This tests the many-to-many relationship between students and courses."

    def teachersWithCourses():
        # Explicitly alias the Teacher and Course tables to avoid ambiguity
        teacher = aliased(Teacher)
        course = aliased(Course)

        # Specify the left side of the join using select_from
        query = session.query(teacher.name, course.title).select_from(teacher).join(Course)
        teachers_with_courses = query.all()

        if teachers_with_courses:
            return teachers_with_courses
        else:
            return "#2 failed. This tests the one-to-many relationship between teachers and courses."

    def coursesTaughtByTeacher(teacher_name):
        """
        Find all the courses taught by a specific teacher.

        Args:
            teacher_name (str): The name of the teacher.

        Returns:
            List of tuples: Each tuple contains the course title taught by the teacher.
        """
        # Explicitly alias the Teacher and Course tables to avoid ambiguity
        teacher = aliased(Teacher)
        course = aliased(Course)


        # Specify the left side of the join using select_from and filter by teacher's name
        query = session.query(course.title).select_from(teacher).join(Course, Course.teacher_id == teacher.id).filter(teacher.name == teacher_name)
        courses_taught_by_teacher = query.all()

        if courses_taught_by_teacher:
            return courses_taught_by_teacher
        else:
            return f"No courses found for teacher: {teacher_name}"

    if __name__ == "__main__":
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

        # Test the one-to-many relationship between teacher and course
        teacher_name_to_query = 'Kelly Molina'  # Replace with the teacher's name you want to query
        teacher_courses = coursesTaughtByTeacher(teacher_name_to_query)
        print(f"Courses taught by {teacher_name_to_query}: {teacher_courses}")
