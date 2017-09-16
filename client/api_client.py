import requests
from rest_framework import status

from client.settings.constants import API_TIMEOUT
from client.responses.error import ErrorResponse


class ApiClient(object):
    def __init__(self):
        self.base_url = None
        self.headers = {'content-type': 'application/json'}
        self.service_name = None
        self.session = requests.Session()
        self.url = None

    def __getattr__(self, name):
        self.url = self.base_url + '/{}'.format(name)

        return self

    def __call__(self, id=None):
        if id:
            self.url = self.url + '/{}'.format(id)

        return self

    def get(self, **kwargs):
        return self.request('GET', params=kwargs)

    def post(self, **kwargs):
        return self.request('POST', data=kwargs)

    def delete(self, **kwargs):
        return self.request('DELETE', params=kwargs)

    def patch(self, **kwargs):
        return self.request('PATCH', data=kwargs)

    def request(self, method, data=None, params=None):
        try:
            response = self.session.request(method,
                                            self.url,
                                            json=data,
                                            params=params,
                                            headers=self.headers,
                                            timeout=API_TIMEOUT)

            if not status.is_success(response.status_code):
                errors = self.set_errors(status=response.status_code,
                                         message=response.text,
                                         method=method,
                                         params=params,
                                         data=data)

                response = ErrorResponse(errors, response.status_code)
        except requests.exceptions.RequestException as err:
            status_code = 503
            errors = self.set_errors(status=status_code,
                                     message=str(err),
                                     method=method,
                                     params=params,
                                     data=data)

            response = ErrorResponse(errors, status_code)

        return response

    def set_errors(self, **kwargs):
        return {
            'errors': {
                'status': kwargs['status'],
                'source': self.url,
                'message': kwargs['message'],
                'detail': {
                    'method': kwargs['method'],
                    'params': kwargs.get('params') if kwargs.get('params') else {},
                    'data': kwargs.get('data') if kwargs.get('data') else {},
                    'base_url': self.base_url
                }
            }
        }
