from typing import Any, Dict

from fastapi.testclient import TestClient


def test_read_student(client: TestClient, student: Dict[str, Any]):
    res = client.get(f"/student/{student['email']}")
    assert res.status_code == 200
    data = res.json()

    for field in student:
        if field in data:
            assert data[field] == student[field]


def test_read_teacher(client: TestClient, teacher: Dict[str, Any]):
    res = client.get(f"/teacher/{teacher['email']}")
    assert res.status_code == 200
    data = res.json()

    for field in teacher:
        if field in data:
            assert data[field] == teacher[field]


def test_read_all_assignments(client: TestClient, assignment: Dict[str, Any]):
    res = client.get(f"/assignment/")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, list) and len(data) == 1
    returned_test_assignment = data[0]

    for field in assignment:
        if field in returned_test_assignment:
            assert returned_test_assignment[field] == assignment[field]


def test_read_all_mails(client: TestClient, mail: Dict[str, Any]):
    res = client.get(f"/mail/")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, list) and len(data) == 1
    returned_test_mail = data[0]

    for field in mail:
        if field in returned_test_mail:
            assert returned_test_mail[field] == mail[field]


# def test_read_category(client: TestClient, category: Dict[str, Any]):
#     pass  # TODO: test


# def test_read_quest(client: TestClient, quest: Dict[str, Any]):
#     pass  # TODO: test


# def test_read_subquest(client: TestClient, subquest: Dict[str, Any]):
#     pass  # TODO: test


# def test_read_attempt(client: TestClient, attempt: Dict[str, Any]):
#     pass  # TODO: test


# def test_read_question(client: TestClient, question: Dict[str, Any]):
#     pass  # TODO: test


# def test_read_npc(client: TestClient, npc: Dict[str, Any]):
#     pass  # TODO: test