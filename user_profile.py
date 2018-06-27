import json
import pandas

class User:
    def __init__(self, user_id):
        self.user_id = user_id

class UserProfiles:
    user_list = []

    def addUserList(self, user):
        self.user_list.append(user)

    def getUserList(self):
        return self.user_list

def importData(users):
    users_json_data = open('users.json').read()
    users_pandas_data = pandas.read_json(users_json_data)

    routes_json_data = open('routes.json').read()
    routes_pandas_data = pandas.read_json(routes_json_data)

    return users_pandas_data, routes_pandas_data

def main():

    current_user_id = 68643159499

    users = UserProfiles()
    users_pandas_data, routes_pandas_data = importData(users)
    
    current_user = users_pandas_data.loc[users_pandas_data['UserID'] == current_user_id]


    final = pandas.merge(current_user, routes_pandas_data, on=['CycleType', 'CyclistLevel'])

    final.to_json('out.json')


if __name__ == "__main__":
   main()