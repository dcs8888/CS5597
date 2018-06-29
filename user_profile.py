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

    current_user_id = 1690042923599

    users = UserProfiles()
    users_pandas_data, routes_pandas_data = importData(users)
    
    current_user = users_pandas_data.loc[users_pandas_data['UserID'] == current_user_id]
    priority_list = current_user['Priority']
    
    print(type(priority_list))
    
    test = None
    
    for item in priority_list[0].split(', '):
        
        if current_user[item].dtype == 'object':
            test = (routes_pandas_data[item].values == current_user[item].values)
        if (current_user[item].dtype == 'int64') & (item == 'ElevationMin'):
            test = (routes_pandas_data[item].values >= current_user[item].values)
        if (current_user[item].dtype == 'int64') & (item == 'ElevationMax'):
            test = (routes_pandas_data[item].values <= current_user[item].values)
        if (current_user[item].dtype == 'int64') & (item == 'ElevationAvg'):
            test = (routes_pandas_data[item].values <= current_user[item].values)

    final = routes_pandas_data.loc[ test ]
    
    
    # final = routes_pandas_data.loc[(routes_pandas_data['ElevationAvg'].values <= current_user['ElevationAvg'].values) & 
                                   # (routes_pandas_data['ElevationMax'].values <= current_user['ElevationMax'].values) & 
                                   # (routes_pandas_data['ElevationMin'].values >= current_user['ElevationMin'].values) & 
                                   # (routes_pandas_data['CycleType'].values == current_user['CycleType'].values) & 
                                   # (routes_pandas_data['CyclistLevel'].values == current_user['CyclistLevel'].values) & 
                                   # (routes_pandas_data['BikeLane'].values == current_user['BikeLane'].values)
                                  # ]

    final.to_json('out.json')


if __name__ == "__main__":
   main()