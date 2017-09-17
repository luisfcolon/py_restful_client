# Python Api Client

[![Build Status](https://travis-ci.org/luisfcolon/py_api_client.svg?branch=master)](https://travis-ci.org/luisfcolon/py_api_client)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/luisfcolon/py_api_client/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/luisfcolon/py_api_client.svg)](https://github.com/luisfcolon/py_api_client/issues)

Silly little python api client using `requests`

## Usage

Let's say you have a Restful API endpoint at:

```
# get all users
http://woot.com/users

# get single user, also can update this user
http://woot.com/users/1
```

To use the api client:

```
client = ApiClient()
client.base_url = 'http://woot.com'

# get 
all_users = client.users.get()
single_user = client.users(1).get()


# post/patch/put
user_data = { 'firstname': 'luis' }

new_user = client.users.post(**data)
edit_user = client.users(1).patch(**data)
edit_user = client.users(1).put(**data)

# delete
deleted_user = client.users(1).delete()

# etc
```
