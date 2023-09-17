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

        # Initially assign one course to each teacher
        for i in range(len(teachers)):
            random_number = random.randint(100, 999)
            full_course_title = f"{sample_courses[i]} {random_number}"
            course = Course(title=full_course_title, teacher=teachers[i])
            db.session.add(course)
        db.session.commit()

        # Assign the remaining courses to random teachers
        for course_title in sample_courses[len(teachers):]:
            random_number = random.randint(100, 999)
            full_course_title = f"{course_title} {random_number}"
            teacher = random.choice(teachers)
            course = Course(title=full_course_title, teacher=teacher)
            db.session.add(course)
        db.session.commit()

        # Enroll each student in at least one random course
        for student in students:
            num_enrollments = random.randint(1, 2)  # Enroll each student in 1 or 2 courses
            random_courses = random.sample(Course.query.all(), num_enrollments)
            student.courses.extend(random_courses)

        db.session.commit()

if __name__ == "__main__":
    seed_database()
