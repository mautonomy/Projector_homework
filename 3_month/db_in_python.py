# #Task 1

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

student_subject = Table('student_subject', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('subject_id', Integer, ForeignKey('subjects.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    subjects = relationship('Subject', secondary=student_subject, back_populates='students')

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    students = relationship('Student', secondary=student_subject, back_populates='subjects')

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def example_usage():

    student1 = Student(name='John')
    student2 = Student(name='Dave')
    student3 = Student(name='Ann')

    subject1 = Subject(name='Math')
    subject2 = Subject(name='English')

    student1.subjects.append(subject1)
    student1.subjects.append(subject2)
    student2.subjects.append(subject1)
    student3.subjects.append(subject1)
    student3.subjects.append(subject2)

    session.add_all([student1, student2, student3, subject1, subject2])
    session.commit()

    students = session.query(Student).all()
    for student in students:
        print(f"Student: {student.name}")
        for subject in student.subjects:
            print(f"  Enrolled in: {subject.name}")

example_usage()


# Task 2

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

student_subject = Table('student_subject', Base.metadata,
                        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
                        Column('subject_id', Integer, ForeignKey('subjects.id'), primary_key=True)
                        )


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    subjects = relationship('Subject', secondary=student_subject, back_populates='students')


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    students = relationship('Student', secondary=student_subject, back_populates='subjects')


engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def example_usage():
    student1 = Student(name='John')
    student2 = Student(name='Dave')
    student3 = Student(name='Ann')


    subject1 = Subject(name='Math')
    subject2 = Subject(name='English')

    student1.subjects.append(subject1)
    student1.subjects.append(subject2)
    student2.subjects.append(subject1)
    student3.subjects.append(subject1)
    student3.subjects.append(subject2)

    session.add_all([student1, student2, student3, subject1, subject2])
    session.commit()

    english_students = session.query(Student).join(student_subject).join(Subject).filter(
        Subject.name == 'English').all()

    print("Students who visited 'English' classes:")
    for student in english_students:
        print(f"- {student.name}")


example_usage()
