import os
from dotenv import load_dotenv
from app.factory import create_app, db
from app.models import Student, Course, Teacher
from faker import Faker
import random

# Load environment variables from .env
load_dotenv()

# Create a Flask app context
app = create_app()

def seed_database():
    with app.app_context():
        # Initialize the database tables
        db.create_all()

        # Create a Faker instance for generating names
        fake = Faker()

        # Define a list of common university courses as strings with added random integers
        sample_courses = [
            "Philosophy 109",
            "Computer Science 253",
            "Psychology 475",
            "Biology 301",
            "History 214",
            "Mathematics 102",
            "Economics 399",
            "Physics 202",
            "Chemistry 508",
            "English Literature 311",
            "Political Science 220",
            "Sociology 150",
            "Art History 425",
            "Engineering 777",
            "Geology 204",
            "Music 632",
            "Foreign Languages 412",
            "Theater 115",
            "Education 198",
        ]

        # Create students with actual names
        students = [Student(name=fake.name()) for _ in range(20)]
        db.session.add_all(students)
        db.session.commit()

        # Create teachers with actual names (limit to 5 teachers)
        teachers = [Teacher(name=fake.name()) for _ in range(5)]
        db.session.add_all(teachers)
        db.session.commit()

        # Initially assign at least 2 courses to each teacher
        for i in range(len(teachers)):
            full_course_title = sample_courses[i]
            course1 = Course(title=f"{full_course_title} (1)", teacher=teachers[i])
            course2 = Course(title=f"{full_course_title} (2)", teacher=teachers[i])
            db.session.add_all([course1, course2])
        db.session.commit()

        # Assign the remaining courses to random teachers
        remaining_courses = [
            course_title
            for course_title in sample_courses[len(teachers) * 2 :]  # At least 2 courses per teacher
        ]
        for course_title in remaining_courses:
            teacher = random.choice(teachers)
            course = Course(title=course_title, teacher=teacher)
            db.session.add(course)
        db.session.commit()

        # Enroll each student in at least 4 random courses
        for student in students:
            num_enrollments = random.randint(4, 5)  # Enroll each student in 4 or 5 courses
            random_courses = random.sample(Course.query.all(), num_enrollments)
            student.courses.extend(random_courses)

        db.session.commit()

if __name__ == "__main__":
    seed_database()
