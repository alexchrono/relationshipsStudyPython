import os
from dotenv import load_dotenv
from app.factory import create_app, db
from app.models import Student, Course, Enrollment, Teacher
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

        # Define a list of common university courses as strings
        sample_courses = [
            "Philosophy",
            "Computer Science",
            "Psychology",
            "Biology",
            "History",
            "Mathematics",
            "Economics",
            "Physics",
            "Chemistry",
            "English Literature",
            "Political Science",
            "Sociology",
            "Art History",
            "Engineering",
            "Geology",
            "Music",
            "Foreign Languages",
            "Theater",
            "Education",
        ]

        # Create students with actual names
        students = [Student(name=fake.name()) for _ in range(20)]
        db.session.add_all(students)
        db.session.commit()

        # Create teachers with actual names
        teachers = [Teacher(name=fake.name()) for _ in range(10)]
        db.session.add_all(teachers)
        db.session.commit()

        # Create university courses with random titles and assign a teacher to each course
        for course_title in sample_courses:
            teacher = random.choice(teachers)
            course = Course(title=course_title, teacher=teacher)
            db.session.add(course)

        # Commit here to ensure that courses are in the database before enrolling students
        db.session.commit()

        # Enroll each student in at least one random course
        for student in students:
            num_enrollments = random.randint(1, 2)  # Enroll each student in 1 or 2 courses
            random_courses = random.sample(Course.query.all(), num_enrollments)
            for course in random_courses:
                enrollment = Enrollment(student=student, course=course)
                db.session.add(enrollment)

        db.session.commit()

if __name__ == "__main__":
    seed_database()
