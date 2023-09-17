from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#SAVE your association tables for the end.  put them  up top.  they should be named
#'enrollments',and 'teacher_student_association'


# Many-to-Many association table between students and courses named enrollments
#name your columns 'student_id'  and 'course_id'

      ##your code here....

# Many-to-Many association table between teachers and students named teacher_student_association
# name your columns teacher_id   and student_id

         ##your code here....

class Student(db.Model):
    #****many to many relationship with courses*****
    #***many to many relationship with teachers.****
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Course(db.Model):

 ''' ***One-to-Many relationship with teacher***
 (a specific course can only be taught by one teacher,
but a teacher can teach multiple courses)

   ***Many-to-Many relationship with students***
  '''
__tablename__ = 'courses'
id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(100), nullable=False)
teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)


class Teacher(db.Model):
    '''one to many relationship with courses.
    (one teacher can teach many courses.each course only taught by one teacher)
    many to many relationship with students.
    '''
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
