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


def test_read_category(client: TestClient, category: Dict[str, Any]):
    res = client.get(f"/category/{category['category_name']}")
    assert res.status_code == 200
    data = res.json()

    for field in category:
        if field in data:
            assert data[field] == category[field]


def test_read_quest(client: TestClient, quest: Dict[str, Any]):
    res = client.get(f"/quest/{quest['quest_name']}")
    assert res.status_code == 200
    data = res.json()

    for field in quest:
        if field in data:
            assert data[field] == quest[field]


def test_read_subquest(client: TestClient, subquest: Dict[str, Any]):
    res = client.get(f"/subquest/{subquest['subquest_name']}")
    assert res.status_code == 200
    data = res.json()

    for field in subquest:
        if field in data:
            assert data[field] == subquest[field]


def test_read_attempt(client: TestClient, attempt: Dict[str, Any]):
    res = client.get(f"/attempt/")
    assert res.status_code == 200
    data = res.json()

    for field in attempt:
        if field in data:
            assert data[field] == attempt[field]


def test_read_question(client: TestClient, question: Dict[str, Any]):
    res = client.get(f"/question")
    assert res.status_code == 200
    data = res.json()

    for field in question:
        if field in data:
            assert data[field] == question[field]


def test_read_npc(client: TestClient, npc: Dict[str, Any]):
    res = client.get(f"/npc/{npc['npc_name']}")
    assert res.status_code == 200
    data = res.json()

    for field in npc:
        if field in data:
            assert data[field] == npc[field]


def test_read_assignmentQuestion(
    client: TestClient, assignmentQuestion: Dict[str, Any]
):
    res = client.get(f"/assignmentQuestion/")
    assert res.status_code == 200
    data = res.json()

    for field in assignmentQuestion:
        if field in data:
            assert data[field] == assignmentQuestion[field]


def test_read_challenge(client: TestClient, challenge: Dict[str, Any]):
    res = client.get(f"/challenge/")
    assert res.status_code == 200
    data = res.json()

    for field in challenge:
        if field in data:
            assert data[field] == challenge[field]

def test_read_student_stats(client: TestClient, student_stats: Dict[str, Any]):
    res = client.get(f"/attempt/{student_stats['student_email']}")
    assert res.status_code == 200
    data = res.json()

    for field in student_stats:
        if field in data:
            assert data[field] == student_stats[field]
