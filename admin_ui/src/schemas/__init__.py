# schemas/ document how the structure that request and response bodies must follow
from .assignment import Assignment, AssignmentCreate, AssignmentInDB, AssignmentUpdate
from .mail import Body, Mail, MailCreate
from .student import Student, StudentCreate, StudentInDB, StudentUpdate
from .teacher import Teacher, TeacherCreate, TeacherInDB, TeacherUpdate
from .category import Category, CategoryCreate, CategoryInDB, CategoryUpdate

# TODO from .xxx import XXX, XXXCreate, XXXInDB, XXXUpdate
