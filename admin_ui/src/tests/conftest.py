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
        schemas.StudentCreate(email="student@e.ntu.edu.sg", name="student", points=0)
    )


@pytest.fixture
def student_updated() -> Dict[str, Any]:
    return vars(
        schemas.StudentUpdate(
            email="student@e.ntu.edu.sg",  # same PK to identify the object
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
            email="teacher@e.ntu.edu.sg",  # same PK to identify the object
            name="teacher_updated",
        )
    )


@pytest.fixture
def assignment() -> Dict[str, Any]:
    return vars(
        schemas.AssignmentCreate(
            assigner="teacher@e.ntu.edu.sg",
            assignee="student@e.ntu.edu.sg",
            description="text",
        )
    )


@pytest.fixture
def assignment_updated() -> Dict[str, Any]:
    return vars(
        schemas.AssignmentUpdate(
            assigner="teacher@e.ntu.edu.sg",  # same PK to identify the object
            assignee="student@e.ntu.edu.sg",  # same PK to identify the object
            description="updated_description",
            points_scored=100,
            time_to_complete_in_seconds=100,
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
def category() -> Dict[str, Any]:
    return vars(schemas.CategoryCreate(category_name="category"))


@pytest.fixture
def quest() -> Dict[str, Any]:
    return vars(schemas.QuestCreate(quest_name="quest", category_name="category"))


@pytest.fixture
def subquest() -> Dict[str, Any]:
    return vars(
        schemas.SubquestCreate(
            subquest_name="subquest",
            quest_name="quest",
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
def attempt() -> Dict[str, Any]:
    return vars(
        schemas.AttemptCreate(
            quest_name="quest",
            student_email="student@e.ntu.edu.sg",
            points_scored=100,
            time_to_complete_in_seconds=100,
        )
    )


@pytest.fixture
def attempt_updated() -> Dict[str, Any]:
    return vars(
        schemas.AttemptCreate(
            quest_name="quest",
            student_email="student@e.ntu.edu.sg",
            points_scored=500,
            time_to_complete_in_seconds=500,
        )
    )


def pysessionfinish(session, exitstatus):
    os.remove("test.db")
