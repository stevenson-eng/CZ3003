"""
Ordering of CREATE tests must be enforced to prevent FK violations
"""
from typing import Any, Dict

import pytest
from fastapi.testclient import TestClient
from requests import Response


def validate(response: Response, request_body: Dict[str, Any]) -> bool:
    # 1st creation should raise 200 OK
    assert response.status_code == 200
    response_body = response.json()

    # Ensure all fields in response and request are identical
    return all(
        [
            response_body[field] == request_body[field]
            for field in response_body
            if field in request_body
        ]
    )


@pytest.mark.run(order=0)
def test_create_student(client: TestClient, student: Dict[str, Any]):
    assert validate(client.post("/student/", json=student), student)


@pytest.mark.run(order=1)
def test_create_teacher(client: TestClient, teacher: Dict[str, Any]):
    assert validate(client.post("/teacher/", json=teacher), teacher)


@pytest.mark.run(order=2)
def test_create_assignment(client: TestClient, assignment: Dict[str, Any]):
    assert validate(client.post("/assignment/", json=assignment), assignment)


@pytest.mark.run(order=3)
def test_create_mail(client: TestClient, mail: Dict[str, Any]):
    res = client.post("/mail/", json=mail)
    assert res.status_code == 200


# @pytest.mark.run(order=4)
# def test_create_category(client: TestClient, category: Dict[str, Any]):
#     pass  # TODO: test


# @pytest.mark.run(order=5)
# def test_create_quest(client: TestClient, quest: Dict[str, Any]):
#     pass  # TODO: test


# @pytest.mark.run(order=6)
# def test_create_subquest(client: TestClient, subquest: Dict[str, Any]):
#     pass  # TODO: test


# @pytest.mark.run(order=7)
# def test_create_attempt(client: TestClient, attempt: Dict[str, Any]):
#     pass  # TODO: test


# @pytest.mark.run(order=8)
# def test_create_question(client: TestClient, question: Dict[str, Any]):
#     pass  # TODO: test


# @pytest.mark.run(order=9)
# def test_create_npc(client: TestClient, npc: Dict[str, Any]):
#     pass  # TODO: test
