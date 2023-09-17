from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Define one-to-many relationship with courses
    courses = db.relationship('Course', secondary='enrollments', back_populates='students')
    enrollments = db.relationship('Enrollment', back_populates='student')
    teachers = db.relationship('Teacher', secondary='teacher_student_association', back_populates='students')

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    # Define one-to-many relationship with teacher
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    teacher = db.relationship('Teacher', back_populates='courses')

    # Define many-to-many relationship with students
    students = db.relationship('Student', secondary='enrollments', back_populates='courses')
    enrollments = db.relationship('Enrollment', back_populates='course')

class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')

class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Define one-to-many relationship with courses
    courses = db.relationship('Course', back_populates='teacher')
    students = db.relationship('Student', secondary='teacher_student_association', back_populates='teachers')

# Define many-to-many relationship table between teachers and students
teacher_student_association = db.Table(
    'teacher_student_association',
    db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.id'), primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True)
)
