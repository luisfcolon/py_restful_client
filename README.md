# Python Api Client

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