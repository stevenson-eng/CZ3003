# from typing import Any, Dict

# from fastapi.testclient import TestClient
# from requests import Response


# def validate(response: Response, request_body: Dict[str, Any]) -> bool:
#     # 1st creation should raise 200 OK
#     assert response.status_code == 200
#     response_body = response.json()

#     # Ensure all fields in response and request are identical
#     return all(
#         [
#             response_body[field] == request_body[field]
#             for field in response_body
#             if field in request_body
#         ]
#     )


# def test_update_student(client: TestClient, student_updated: Dict[str, Any]):
#     assert validate(client.patch("/student/", json=student_updated), student_updated)


# def test_update_teacher(client: TestClient, teacher_updated: Dict[str, Any]):
#     assert validate(client.patch("/teacher/", json=teacher_updated), teacher_updated)


# def test_update_assignment(client: TestClient, assignment_updated: Dict[str, Any]):
#     assert validate(
#         client.patch("/assignment/", json=assignment_updated), assignment_updated
#     )


# def test_update_mail(client: TestClient, mail_updated: Dict[str, Any]):
#     assert validate(client.patch("/mail/", json=mail_updated), mail_updated)


# def test_update_category(client: TestClient, category_updated: Dict[str, Any]):
#     pass  # TODO: test


# def test_update_quest(client: TestClient, quest_updated: Dict[str, Any]):
#     pass  # TODO: test


# def test_update_subquest(client: TestClient, subquest_updated: Dict[str, Any]):
#     pass  # TODO: test


# def test_update_attempt(client: TestClient, attempt_updated: Dict[str, Any]):
#     pass  # TODO: test


# def test_update_question(client: TestClient, question_updated: Dict[str, Any]):
#     pass  # TODO: test


# def test_update_npc(client: TestClient, npc_updated: Dict[str, Any]):
#     pass  # TODO: test