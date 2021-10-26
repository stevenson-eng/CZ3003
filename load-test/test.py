from cicadad.core.decorators import scenario
from cicadad.core.engine import Engine
from cicadad.core.decorators import scenario, load_model, user_loop
from cicadad.core.scenario import n_seconds, iterations_per_second_limited
import requests

engine = Engine()

base_url = "https://fastapi-ernestang98.cloud.okteto.net"

REQUESTS_PER_SECOND = 4
NUMBER_OF_USERS = 10
DURATION_OF_LOAD_TEST = 30
LOAD_TEST_EMAIL = id_generator() + "loadtest@gmail.com"
LOAD_TEST_NAME = "loadtest"


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_url(path)
    return base_url + path


@scenario(engine)
def create_user_for_load_test(context):
    response = requests.post(
        url=generate_url('/student/'),
        json={
          "email": LOAD_TEST_EMAIL,
          "name": LOAD_TEST_NAME,
          "points": 0,
          "password": "loadtest"
        },
    )
    assert response.status_code == 200

    body = response.json()

    return {
        "email": body["email"],
        "name": body["name"]
    }


@scenario(engine)
@load_model(n_seconds(DURATION_OF_LOAD_TEST, NUMBER_OF_USERS))
@user_loop(iterations_per_second_limited(REQUESTS_PER_SECOND))
def base_api_test(context):
    response = requests.get(base_url)
    assert response.status_code == 307
    return "Passed!"


@scenario(engine)
@load_model(n_seconds(DURATION_OF_LOAD_TEST, NUMBER_OF_USERS))
@user_loop(iterations_per_second_limited(REQUESTS_PER_SECOND))
@dependency(read_all_user_for_load_test)
def read_created_user_valid_test(context):
    response = requests.get(
        url=generate_url("/student/")
    )
    assert response.status_code == 200


@scenario(engine)
@load_model(n_seconds(DURATION_OF_LOAD_TEST, NUMBER_OF_USERS))
@user_loop(iterations_per_second_limited(REQUESTS_PER_SECOND))
@dependency(create_user_for_load_test)
def read_created_user_valid_test(context):
    response = requests.get(
        url=generate_url("/student/{email}".format(email = context["create_user_for_load_test"]["output"]["email"]))
    )
    assert response.status_code == 200


@scenario(engine)
@load_model(n_seconds(DURATION_OF_LOAD_TEST, NUMBER_OF_USERS))
@user_loop(iterations_per_second_limited(REQUESTS_PER_SECOND))
@dependency(create_user_for_load_test)
def read_created_user_test_invalid_test(context):
    response = requests.get(
        url=generate_url("/student/{email}1".format(email = context["create_user_for_load_test"]["output"]["email"]))
    )
    assert response.status_code == 200
    assert response.json() == []


if __name__ == "__main__":
    engine.start()
