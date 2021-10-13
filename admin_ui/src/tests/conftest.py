import os
from typing import Any, Dict

import pytest
import schemas
from db.database import Base, get_db
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture
def client() -> TestClient:
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)


@pytest.fixture
def student() -> Dict[str, Any]:
    return vars(
        schemas.StudentCreate(
            email="student@e.ntu.edu.sg", name="student", points=0
        )
    )


@pytest.fixture
def student_updated() -> Dict[str, Any]:
    return vars(
        schemas.StudentUpdate(
            email="student_updated@e.ntu.edu.sg",
            name="student_updated",
            points=1000,
        )
    )


@pytest.fixture
def teacher() -> Dict[str, Any]:
    return vars(schemas.TeacherCreate(email="teacher@e.ntu.edu.sg", name="teacher"))


@pytest.fixture
def teacher_updated() -> Dict[str, Any]:
    return vars(
        schemas.TeacherUpdate(
            email="teacher_updated@e.ntu.edu.sg",
            name="teacher_updated",
        )
    )


@pytest.fixture
def assignment() -> Dict[str, Any]:
    return vars(
        schemas.AssignmentCreate(
            assigner="teacher@e.ntu.edu.sg", assignee="student@e.ntu.edu.sg", description="text",
        )
    )


@pytest.fixture
def assignment_updated() -> Dict[str, Any]:
    return vars(
        schemas.AssignmentUpdate(
            assigner="updated_teacher@e.ntu.edu.sg",
            assignee="updated_student@e.ntu.edu.sg",
            description="updated_text",
        )
    )


@pytest.fixture
def mail() -> Dict[str, Any]:
    return vars(
        schemas.MailCreate(
            subject="subject",
            body_heading="heading",
            body_text="text",
            sender="teacher@e.ntu.edu.sg",
            recipients=["student@e.ntu.edu.sg"],
        )
    )


@pytest.fixture
def mail_updated() -> Dict[str, Any]:
    return vars(
        schemas.MailCreate(
            subject="updated_subject",
            body_heading="updated_heading",
            body_text="updated_text",
            sender="updated_teacher@e.ntu.edu.sg",
            recipients=["updated_student@e.ntu.edu.sg"],
        )
    )


@pytest.fixture
def category() -> Dict[str, Any]:
    return vars(
        schemas.CategoryCreate(
            category_name="category"
        )
    )


@pytest.fixture
def category_updated() -> Dict[str, Any]:
    return vars(
        schemas.CategoryUpdate(
            category_name="category_updated",
        )
    )


@pytest.fixture
def quest() -> Dict[str, Any]:
    return vars(
        schemas.QuestCreate(
            quest_name="quest",
            category_name="category"
        )
    )

@pytest.fixture
def quest_updated() -> Dict[str, Any]:
    return vars(
        schemas.QuestUpdate(
            quest_name="quest_updated",
            category_name="category_updated",
        )
    )


@pytest.fixture
def subquest() -> Dict[str, Any]:
    return vars(
        schemas.SubquestCreate(
            subquest_name="subquest",
            quest_name="quest",
        )
    )

@pytest.fixture
def subquest_updated() -> Dict[str, Any]:
    return vars(
        schemas.SubquestUpdate(
            subquest_name="subquest_updated",
            quest_name="quest_updated",
        )
    )

@pytest.fixture
def npc() -> Dict[str, Any]:
    return vars(
        schemas.NpcCreate(
            npc_name="npc", 
            subquest_name="subquest",
        )
    )


@pytest.fixture
def npc_updated() -> Dict[str, Any]:
    return vars(
        schemas.NpcUpdate(
            npc_name="npc_updated",
            subquest_name="subquest_updated",
        )
    )


def pysessionfinish(session, exitstatus):
    os.remove("test.db")
