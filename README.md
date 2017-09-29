# Python Api Client

[![Build Status](https://travis-ci.org/luisfcolon/py_api_client.svg?branch=master)](https://travis-ci.org/luisfcolon/py_api_client)
[![Coverage Status](https://coveralls.io/repos/github/luisfcolon/py_api_client/badge.svg)](https://coveralls.io/github/luisfcolon/py_api_client)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/luisfcolon/py_api_client/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/luisfcolon/py_api_client.svg)](https://github.com/luisfcolon/py_api_client/issues)

Silly little python restful api client using `requests`

## Usage

Let's say you have a Restful API endpoint at:

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

To use the api client:

```python
client = ApiClient()
client.base_url = 'http://woot.com'

# get 
all_users = client.users.get()
single_user = client.users(1).get()

all_posts = client.posts.get()
single_post = client.posts(123).get()

# post/patch/put (same can be applied to posts)
user_data = { 'firstname': 'luis' }

new_user = client.users.post(**data)
edit_user = client.users(1).patch(**data)
edit_user = client.users(1).put(**data)

# delete
deleted_user = client.users(1).delete()

# etc
```
