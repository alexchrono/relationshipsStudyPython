from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# *****************************association tables*************************************
# Association table for many-to-many relationship between students and courses
enrollments = db.Table(
    'enrollments',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True)
)

# Association table for many-to-many relationship between teachers and students
teacher_student_association = db.Table(
    'teacher_student_association',
    db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.id'), primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True)
)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    courses = db.relationship('Course', secondary=enrollments, back_populates='students')
    teachers = db.relationship('Teacher', secondary=teacher_student_association, back_populates='students')

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
    teacher = db.relationship('Teacher', back_populates='courses')
    students = db.relationship('Student', enrollments, back_populates='courses')

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    courses = db.relationship('Course', back_populates='teacher')
    students = db.relationship('Student', teacher_student_association, back_populates='teachers')
