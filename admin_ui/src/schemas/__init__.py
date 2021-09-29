# schemas/ document how the structure that request and response bodies must follow
from .assignment import Assignment, AssignmentCreate, AssignmentInDB, AssignmentUpdate
from .mail import Body, Mail, MailCreate
from .student import Student, StudentCreate, StudentInDB, StudentUpdate
from .teacher import Teacher, TeacherCreate, TeacherInDB, TeacherUpdate
from .category import Category, CategoryCreate, CategoryInDB, CategoryUpdate
from .quest import Quest, QuestCreate, QuestInDB, QuestUpdate
from .subquest import Subquest, SubquestCreate, SubquestInDB, SubquestUpdate
from .npc import Npc, NpcCreate, NpcInDB, NpcUpdate

# TODO from .xxx import XXX, XXXCreate, XXXInDB, XXXUpdate
