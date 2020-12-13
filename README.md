# Python Restful Client

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)
[![Build Status](https://travis-ci.org/luisfcolon/py_restful_client.svg?branch=master)](https://travis-ci.org/luisfcolon/py_restful_client)
[![Coverage Status](https://coveralls.io/repos/github/luisfcolon/py_restful_client/badge.svg?branch=master)](https://coveralls.io/github/luisfcolon/py_restful_client?branch=master)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/luisfcolon/py_restful_client/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/luisfcolon/py_restful_client.svg)](https://github.com/luisfcolon/py_restful_client/issues)

Silly little python restful client using [Requests](http://docs.python-requests.org/en/master/)

## Usage

Let's say you have the following restful endpoints:

```
# get all users
http://woot.com/users

# get single user, also can update this user
http://woot.com/users/1

# get all blog posts
http://woot.com/posts

# get single post, update post
http://woot.com/posts/123
```

To use the restful client:

```python
client = RestfulClient()
client.base_url = 'http://woot.com'

# get

all_users = client.get('/users')
single_user = client.get('/users/1')

all_posts = client.get('/posts')
single_post = client.get('/posts/123')

# post, patch, put

user_data = {'firstname': 'luis'}

new_user = client.post('/users', data)
edit_user = client.patch('/users/1', data)
edit_user = client.put('/users/1', data)

# delete

deleted_user = client.delete('/users/1')
```

Using Basic Authentication is simple. You can create any auth object supported by Requests and pass it into the auth parameter.


```
auth = HTTPBasicAuth(username, password)
user_data = {'firstname': 'luis'}
new_user = client.post('/users', data, auth) 

# or

new_user = client.post('/users', data, auth=(username, password))

```

## Error Handling

I removed all error handling from this version.

The client's only purpose is to make an api call and return a response. The application using this client should decide how it wants to handle any errors.


