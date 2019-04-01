import pytest
import requests
import responses
import base64

from client import RestfulClient


def test_restful_client_init():
    client = RestfulClient()

    assert client.base_url == None
    assert client.headers == {'content-type': 'application/json'}
    assert type(client.session) is requests.Session


@responses.activate
def test_restful_client_get():
    responses.add(responses.GET, 'http://woot.com/users',
                  json={'data': 'success'},
                  status=200,
                  content_type='application/json')

    client = RestfulClient()
    client.base_url = 'http://woot.com'

    results = client.get('/users')

    assert results.json() == {'data': 'success'}
    assert results.status_code == 200


@responses.activate
def test_restful_client_get_with_id():
    responses.add(responses.GET, 'http://woot.com/users/1',
                  json={'data': 'success'},
                  status=200,
                  content_type='application/json')

    client = RestfulClient()
    client.base_url = 'http://woot.com'

    user_id = 1
    results = client.get('/users/{}'.format(user_id))

    assert results.json() == {'data': 'success'}
    assert results.status_code == 200


@responses.activate
def test_restful_client_post():
    responses.add(responses.POST, 'http://woot.com/users',
                  json={'data': 'success'},
                  status=200,
                  content_type='application/json')

    client = RestfulClient()
    client.base_url = 'http://woot.com'

    data = {'firstname': 'luis'}
    results = client.post('/users', data)

    assert results.json() == {'data': 'success'}
    assert results.status_code == 200


@responses.activate
def test_restful_client_put():
    responses.add(responses.PUT, 'http://woot.com/users/1',
                  json={'data': 'success'},
                  status=200,
                  content_type='application/json')

    client = RestfulClient()
    client.base_url = 'http://woot.com'

    user_id = 1
    data = {'firstname': 'luis'}
    results = client.put('/users/{}'.format(user_id), data)

    assert results.json() == {'data': 'success'}
    assert results.status_code == 200


@responses.activate
def test_restful_client_put_with_auth():
    username = 'cthulhu'
    password = '<c667^Fmz=M,BWn;^DJFe)'
    basic_auth_encoded = base64.encodestring('{}:{}'.format(username, password).encode())

    responses.add(responses.PUT, 'http://woot.com/users/1',
                  json={'data': 'success'},
                  status=200,
                  headers={'Authorization': 'Basic {}'.format(basic_auth_encoded) },
                  content_type='application/json')

    client = RestfulClient()
    client.base_url = 'http://woot.com'

    user_id = 1
    data = {'firstname': 'luis'}
    results = client.put('/users/{}'.format(user_id), data)

    assert results.json() == {'data': 'success'}
    assert results.status_code == 200


@responses.activate
def test_restful_client_delete():
    responses.add(responses.DELETE, 'http://woot.com/users/1',
                  json={'data': 'success'},
                  status=200,
                  content_type='application/json')

    client = RestfulClient()
    client.base_url = 'http://woot.com'

    user_id = 1
    results = client.delete('/users/{}'.format(user_id))

    assert results.json() == {'data': 'success'}
    assert results.status_code == 200


@responses.activate
def test_restful_client_patch():
    responses.add(responses.PATCH, 'http://woot.com/posts/123',
                  json={'data': 'success'},
                  status=200,
                  content_type='application/json')

    client = RestfulClient()
    client.base_url = 'http://woot.com'

    post_id = 123
    data = {'title': 'I did it for Pee Wee'}
    results = client.patch('/posts/{}'.format(post_id), data)

    assert results.json() == {'data': 'success'}
    assert results.status_code == 200
