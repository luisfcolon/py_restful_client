class ErrorResponse(object):
    def __init__(self, errors, status_code):
        self.errors = errors
        self.status_code = status_code
        self.text = None

    def json(self):
        return self.errors

    def __str__(self):
        return 'Status: {}, Errors: {}'.format(self.status_code, self.errors)
