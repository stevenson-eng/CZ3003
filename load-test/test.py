from cicadad.core.decorators import scenario
from cicadad.core.engine import Engine
from cicadad.core.decorators import scenario, load_model, user_loop, dependency
from cicadad.core.scenario import n_seconds, iterations_per_second_limited
from utils import id_generator, generate_url
import requests
import json
import datetime

engine = Engine()
BASE_URL = "https://fastapi-ernestang98.cloud.okteto.net"
REQUESTS_PER_SECOND = 2
NUMBER_OF_USERS = 10
DURATION_OF_LOAD_TEST = 60
WAIT_PERIOD = 2
LOAD_TEST_EMAIL = "{id}_loadtest@gmail.com".format(id=id_generator())
LOAD_TEST_NAME = "loadtest"
LOAD_TESTNEW_NAME = "loadtest2"


# @scenario(engine)
# def my_first_test(context):
#     response = requests.get("https://www.google.com")
#     assert response.status_code == 200


@scenario(engine)
@load_model(n_seconds(DURATION_OF_LOAD_TEST, NUMBER_OF_USERS))
@user_loop(iterations_per_second_limited(REQUESTS_PER_SECOND))
def base_api_test(context):
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    return "Root API Test Passed!"


@scenario(engine)
@load_model(n_seconds(DURATION_OF_LOAD_TEST, NUMBER_OF_USERS, WAIT_PERIOD))
@user_loop(iterations_per_second_limited(REQUESTS_PER_SECOND))
def read_all_users(context):
    response = requests.get(
        url=generate_url("/student/", BASE_URL)
    )
    assert response.status_code == 200
    return "READ ALL Student API Test Passed!"


@scenario(engine)
def create_user_for_load_test(context):
    response = requests.post(
        url=generate_url('/student/', BASE_URL),
        json={
          "email": LOAD_TEST_EMAIL,
          "name": LOAD_TEST_NAME
        }
    )
    assert response.status_code == 200
    body = response.json()
    return {"email": body["email"],"name": body["name"]}


@scenario(engine)
@load_model(n_seconds(DURATION_OF_LOAD_TEST, NUMBER_OF_USERS))
@user_loop(iterations_per_second_limited(REQUESTS_PER_SECOND))
@dependency(create_user_for_load_test)
def read_created_user_valid_test(context):
    response = requests.get(
        url=generate_url("/student/{email}".format(email = context["create_user_for_load_test"]["output"]["email"]), BASE_URL)
    )
    assert response.status_code == 200
    return "READ created student {} from database API Test Passed!".format(context["create_user_for_load_test"]["output"]["name"])  


@scenario(engine)
@load_model(n_seconds(DURATION_OF_LOAD_TEST, NUMBER_OF_USERS))
@user_loop(iterations_per_second_limited(REQUESTS_PER_SECOND))
@dependency(create_user_for_load_test)
def read_created_user_test_invalid_test(context):
    response = requests.get(
        url=generate_url("/student/{email}1".format(email = context["create_user_for_load_test"]["output"]["email"]), BASE_URL)
    )
    assert response.status_code == 200
    assert response.json() == None
    return "READ student {} that does not exists in database API Test Passed!".format(context["create_user_for_load_test"]["output"]["name"] + str(1))  


@scenario(engine)
@load_model(n_seconds(DURATION_OF_LOAD_TEST, NUMBER_OF_USERS))
@user_loop(iterations_per_second_limited(REQUESTS_PER_SECOND))
@dependency(create_user_for_load_test)
def update_user_for_load_test(context):
    response = requests.put(
        url=generate_url('/student/', BASE_URL),
        json={
          "email": context["create_user_for_load_test"]["output"]["email"],
          "name": LOAD_TEST_NEW_NAME
        },
    )
    assert response.status_code == 200
    body = response.json()
    return {"email": body["email"],"name": body["name"]}


@scenario(engine)
@dependency(create_user_for_load_test)
def delete_user_for_load_test(context):
    response = requests.delete(
        url=generate_url('/student/?email={email}'.format(email = context["create_user_for_load_test"]["output"]["email"]), BASE_URL)
    )
    assert response.status_code == 200
    return "DELETE created student {} from database API Test Passed!".format(context["create_user_for_load_test"]["output"]["name"])


@scenario(engine)
@dependency(create_user_for_load_test)
def verify_delete_user_for_load_test(context):
    response = requests.get(
        url=generate_url("/student/{email}".format(email = context["create_user_for_load_test"]["output"]["email"]), BASE_URL)
    )
    assert response.status_code == 200
    assert response.json() == None
    return "Verify DELETE created student {} from database API Test Passed! (timeout error from running 2 requests under one scenario hence, one request per scenario)".format(context["create_user_for_load_test"]["output"]["name"])




if __name__ == "__main__":
    engine.start()

