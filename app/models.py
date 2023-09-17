from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Save your association tables for the end. They should be named 'enrollments' and 'teacher_student_association'

# *****************************association tables*************************************
# (Prompt: Define the 'enrollments' association table here)


# (Prompt: Define the 'teacher_student_association' association table here)




# STEP 1:
# Make a many-to-many relationship between students and courses. You will need to make an association table.
#delete the database. delete migration.  initiated db. make migration. upgrade.  seed.
# Then uncomment the first test in GOHERE.PY and test it

# STEP 2:
# Make a one-to-many relationship between teachers and courses.
# a course can only have one teacher (think philosophy 105 only taught at 7:am.)
# You will need to make an association table.
#delete the database. delete migration.  initiated db. make migration. upgrade.  seed.
# Then uncomment the second test in GOHERE.PY and test it


class Student(db.Model):
                        # Many-to-many relationship with courses
                        # Many-to-many relationship with teachers
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Course(db.Model):
    __tablename__ = 'courses'
                            # Many-to-Many relationship with students
                            # One-to-Many relationship with teacher
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)

class Teacher(db.Model):
    __tablename__ = 'teachers'

    # One-to-many relationship with courses
    # Many-to-many relationship with students
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

