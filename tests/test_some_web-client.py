from some_web_client import SomeResourceClient
import responses
from datetime import datetime
import pytest

# https://github.com/getsentry/responses/blob/master/README.rst - ссылка на ридми


@responses.activate
def test_some_web_client():
    valid_json_answer = {
                      "lastActionTime": 1626615580,
                      "timeDiff": 16983
                  }
    responses.add(responses.GET, 'https://www.avito.ru/web/user/get-status/177068588',
                  json=valid_json_answer, status=200)
    some_resource_client = SomeResourceClient("https://www.avito.ru")
    res = some_resource_client.get_user_last_action_time(177068588)
    assert res == datetime.fromtimestamp(1626598597)


@responses.activate
def test_some_web_client_with_error():
    valid_json_data_with_error = {
        "errors": [
            "Not found"
        ]
    }
    responses.add(responses.GET, 'https://www.avito.ru/web/user/get-status/177068588-',
                  json=valid_json_data_with_error, status=404)
    with pytest.raises(KeyError):
        some_resource_client = SomeResourceClient("https://www.avito.ru")
        some_resource_client.get_user_last_action_time("177068588-")
