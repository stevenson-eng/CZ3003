# schemas/ document how the structure that request and response bodies must follow
from .assignment import Assignment, AssignmentCreate, AssignmentInDB, AssignmentUpdate
from .category import Category, CategoryCreate, CategoryInDB, CategoryUpdate
from .mail import Mail, MailCreate
from .npc import Npc, NpcCreate, NpcInDB, NpcUpdate
from .quest import Quest, QuestCreate, QuestInDB, QuestUpdate
from .student import Student, StudentCreate, StudentInDB, StudentUpdate
from .subquest import Subquest, SubquestCreate, SubquestInDB, SubquestUpdate
from .npc import Npc, NpcCreate, NpcInDB, NpcUpdate
from .question import Question, QuestionCreate, QuestionInDB, QuestionUpdate
from .teacher import Teacher, TeacherCreate, TeacherInDB, TeacherUpdate
# from .attempt import Attempt, AttemptCreate, AttemptInDB, AttemptUpdate

# TODO from .xxx import XXX, XXXCreate, XXXInDB, XXXUpdate
