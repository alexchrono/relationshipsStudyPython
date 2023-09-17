from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#SAVE THESE TOP TWO TABLES FOR LAST
# Many-to-Many association table between students and courses
enrollments = db.Table('enrollments',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True)
)

# Many-to-Many association table between teachers and students
teacher_student_association = db.Table('teacher_student_association',
    db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.id'), primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True)
)

class Student(db.Model):
    #should have a many to many relationship with courses.
    #should have a 
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Many-to-Many relationship with courses
    courses = db.relationship('Course', secondary=enrollments, back_populates='students')

    # Many-to-Many relationship with teachers
    teachers = db.relationship('Teacher', secondary=teacher_student_association, back_populates='students')

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    # One-to-Many relationship with teacher (a course can only be taught by one teacher)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
    teacher = db.relationship('Teacher', back_populates='courses')

    # Many-to-Many relationship with students
    students = db.relationship('Student', secondary=enrollments, back_populates='courses')

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # One-to-Many relationship with courses
    courses = db.relationship('Course', back_populates='teacher')

    # Many-to-Many relationship with students
    students = db.relationship('Student', secondary=teacher_student_association, back_populates='teachers')

# Notes:
# For Enrollment: Opted for a many-to-many relationship between students and courses using an association table called 'enrollments'.
# This allows students to enroll in multiple courses and courses to have multiple students.
