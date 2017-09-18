from client.responses.error import ErrorResponse


def test_error_response_init():
    error = ErrorResponse('woops', 404)

    assert error.status_code == 404
    assert error.errors == 'woops'
    assert error.text == None


def test_error_response_json():
    error = ErrorResponse('woops', 404)
    errorJson = error.json()

    assert errorJson == 'woops'


def test_error_response_tostring():
    error = ErrorResponse('woops', 404)

    assert error.__str__() == 'Status: 404, Errors: woops'
