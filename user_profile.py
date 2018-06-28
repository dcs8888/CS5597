import json
import pandas
import numpy

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

    current_user_id = 10511552199

    users = UserProfiles()
    users_pandas_data, routes_pandas_data = importData(users)
    
    current_user = users_pandas_data.loc[users_pandas_data['UserID'] == current_user_id]
    
    final = routes_pandas_data.loc[(routes_pandas_data['ElevationAvg'].values <= current_user['ElevationAvg'].values) & 
                                   (routes_pandas_data['ElevationMax'].values <= current_user['ElevationMax'].values) & 
                                   (routes_pandas_data['ElevationMin'].values >= current_user['ElevationMin'].values) & 
                                   (routes_pandas_data['CycleType'].values == current_user['CycleType'].values) & 
                                   (routes_pandas_data['CyclistLevel'].values == current_user['CyclistLevel'].values) & 
                                   (routes_pandas_data['PreferBikeLanes'].values == current_user['PreferBikeLanes'].values)
                                  ]

    final.to_json('out.json')


if __name__ == "__main__":
   main()