import pytest
import requests
import responses

from client.api_client import ApiClient


def test_api_client_init():
    client = ApiClient()

    assert client.base_url == None
    assert client.headers == { 'content-type': 'application/json' }
    assert client.service_name == None
    assert type(client.session) is requests.Session
    assert client.url == None


def test_api_client__getattr__():
    client = ApiClient()
    client.base_url = 'http://woot.com'

    results = client.__getattr__('search')

    assert client.url == 'http://woot.com/search'
    assert type(results) is ApiClient


@responses.activate
def test_api_client_get():
    responses.add(responses.GET, 'http://woot.com/users',
                  json={ 'data': 'success' }, status=200,
                  content_type='application/json')

    client = ApiClient()
    client.base_url = 'http://woot.com'

    results = client.users.get()
    print(client.url)

    assert results.json() == { 'data': 'success' }
    assert results.status_code == 200

@responses.activate
def test_api_client_get_with_id():
    responses.add(responses.GET, 'http://woot.com/users/1',
                  json={ 'data': 'success' }, status=200,
                  content_type='application/json')

    client = ApiClient()
    client.base_url = 'http://woot.com'

    results = client.users(1).get()

    assert results.json() == { 'data': 'success' }
    assert results.status_code == 200

@responses.activate
def test_api_client_post():
    responses.add(responses.POST, 'http://woot.com/users',
                  json={ 'data': 'success' }, status=200,
                  content_type='application/json')

    client = ApiClient()
    client.base_url = 'http://woot.com'

    data = { 'firstname': 'luis' }
    results = client.users.post(**data)

    assert results.json() == { 'data': 'success' }
    assert results.status_code == 200


@responses.activate
def test_api_client_delete():
    responses.add(responses.DELETE, 'http://woot.com/users/1',
                  json={ 'data': 'success' }, status=200,
                  content_type='application/json')

    client = ApiClient()
    client.base_url = 'http://woot.com'

    results = client.users(1).delete()

    assert results.json() == { 'data': 'success' }
    assert results.status_code == 200


@responses.activate
def test_api_client_patch():
    responses.add(responses.PATCH, 'http://woot.com/posts/123',
                  json={ 'data': 'success' }, status=200,
                  content_type='application/json')

    client = ApiClient()
    client.base_url = 'http://woot.com'

    data = { 'title': 'I did it for Pee Wee' }
    results = client.posts(123).patch(**data)

    assert results.json() == { 'data': 'success' }
    assert results.status_code == 200


@responses.activate
def test_api_client_request_success():
    responses.add(responses.POST, 'http://woot.com/users',
                  json={ 'id': '123' }, status=200,
                  content_type='application/json')

    client = ApiClient()
    client.url = 'http://woot.com/users'

    data = { 'first_name': 'luis' }
    results = client.request('POST', data)

    assert results.json() == { 'id': '123' }
    assert results.status_code == 200


@responses.activate
def test_api_client_request_404():
    responses.add(responses.POST, 'http://woot.com/dwarf_tossing',
                  json={ 'message': 'not found' }, status=404,
                  content_type='application/json')

    client = ApiClient()
    client.base_url = 'http://woot.com'
    client.url = 'http://woot.com/dwarf_tossing'

    data = { 'battle': 'helms_deep' }
    results = client.request('POST', data)

    assert results.status_code == 404
    assert results.json() == {
        'errors': {
            'status': 404,
            'source': 'http://woot.com/dwarf_tossing',
            'message': '{"message": "not found"}',
            'detail': {
                'method': 'POST',
                'params': {},
                'base_url': 'http://woot.com',
                'data': { 'battle': 'helms_deep' }
            }
        }
    }


@responses.activate
def test_api_client_request_exception():
    exception = requests.exceptions.RequestException('Womp womp womp')

    responses.add(responses.POST, 'http://woot.com/naughty_endpoint',
                  body=exception, status=503,
                  content_type='application/json')

    client = ApiClient()
    client.base_url = 'http://woot.com'

    data = {}
    results = client.naughty_endpoint.post(**data)

    assert results.status_code == 503
    assert results.json() == {
        'errors': {
            'status': 503,
            'source': 'http://woot.com/naughty_endpoint',
            'message': 'Womp womp womp',
            'detail': {
                'method': 'POST',
                'params': {},
                'data': {},
                'base_url': 'http://woot.com'
            }
        }
    }

def test_api_client_set_errors():
    client = ApiClient()
    client.base_url = 'http://woot.com'
    client.url = 'http://woot.com/dwarf_tossing'

    errors = client.set_errors(status=503,
                               message='some error',
                               method='POST',
                               params=None,
                               data={ 'foo': 'bar' })

    assert errors == {
        'errors': {
            'status': 503,
            'source': 'http://woot.com/dwarf_tossing',
            'message': 'some error',
            'detail': {
                'method': 'POST',
                'params': {},
                'data': { 'foo': 'bar' },
                'base_url': 'http://woot.com'
            }
        }
    }
