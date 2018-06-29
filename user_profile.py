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

    current_user_id = 1630101668599

    users = UserProfiles()
    users_pandas_data, routes_pandas_data = importData(users)
    
    current_user = users_pandas_data.loc[users_pandas_data['UserID'] == current_user_id]
    index = int(current_user.index.values)

    priority_list = current_user['Priority']
    
    first = routes_pandas_data.loc[(routes_pandas_data['ElevationAvg'].values <= current_user['ElevationAvg'].values) & 
                                   (routes_pandas_data['ElevationMax'].values <= current_user['ElevationMax'].values) & 
                                   (routes_pandas_data['ElevationMin'].values >= current_user['ElevationMin'].values)
                                   ]
    
    route_id = (first['RouteID'].values)
    print(route_id.size)
    
    if route_id.size == 0:
        first.to_json('out.json')
        return
    
    for item in priority_list[index].split(', '):

        final = first.loc[(first[item].values == current_user[item].values)]
        
        final_route_id = (final['RouteID'].values)
        print(final_route_id.size)
        
        if final_route_id.size == 0:
            first.to_json('out.json')
            return
        
        first = final
    final.to_json('out.json')

if __name__ == "__main__":
   main()