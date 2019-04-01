import requests

from client.settings import API_TIMEOUT


class RestfulClient(object):
    def __init__(self):
        self.base_url = None
        self.headers = {'content-type': 'application/json'}
        self.session = requests.Session()

    def get(self, path, params=None, auth=None):
        return self.request('GET', path, params=params, auth=auth)

    def post(self, path, data=None, auth=None):
        return self.request('POST', path, data=data, auth=auth)

    def delete(self, path, auth=None):
        return self.request('DELETE', path, auth=auth)

    def patch(self, path, data=None, auth=None):
        return self.request('PATCH', path, data=data, auth=auth)

    def put(self, path, data=None, auth=None):
        return self.request('PUT', path, data=data, auth=auth)

    def url(self, path):
        return self.base_url + path

    def request(self, method, path, data=None, params=None, auth=None):
        response = self.session.request(
            method,
            self.url(path),
            auth=auth,
            json=data,
            params=params,
            headers=self.headers,
            timeout=API_TIMEOUT
        )

        return response
