from cicadad.core.decorators import scenario
from cicadad.core.engine import Engine
from cicadad.core.decorators import scenario, load_model, user_loop
from cicadad.core.scenario import n_seconds, iterations_per_second_limited
import requests

engine = Engine()

base_url = "https://0kftyn.deta.dev"

def generate_url(path)
    return base_url + path

@scenario(engine)
def create_user_for_load_test(context):
    response = requests.post(
        url=generate_url('/student/'),
        json={
          "email": "loadtest@gmail.com",
          "name": "loadtest",
          "points": 0,
          "password": "loadtest"
        },
    )
    assert response.status_code == 200


@scenario(engine)
@load_model(n_seconds(180, 30))
@user_loop(iterations_per_second_limited(4))
def base_api_test(context):
    response = requests.get(base_url)
    assert response.status_code == 200
    return "Passed!"


if __name__ == "__main__":
    engine.start()
