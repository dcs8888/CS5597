import json

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
    json_data = open('data.json').read()
    data = json.loads(json_data)
    for item in data:
        for sub_item in item:
            if 'UserID' in sub_item:
                user = User(item[sub_item])
                users.addUserList(user)
            if 'ElevationAvg' in sub_item:
                user.elevation_avg = item[sub_item]
            if 'ElevationMax' in sub_item:
                user.elevation_max = item[sub_item]
            if 'ElevationMin' in sub_item:
                user.elevation_min = item[sub_item]
            if 'CycleType' in sub_item:
                user.cycle_type = item[sub_item]
            if 'CyclistLevel' in sub_item:
                user.cyclist_level = item[sub_item]
            if 'TimeAvailable' in sub_item:
                user.time_available = item[sub_item]
            if 'PreferBikeLanes' in sub_item:
                user.prefer_bike_lanes = item[sub_item]
            if 'PreferBikeTrials' in sub_item:
                user.prefer_bike_trials = item[sub_item]
            if 'StartLocation' in sub_item:
                user.start_location = item[sub_item]
            if 'EndLocation' in sub_item:
                user.end_location = item[sub_item]
            if 'ReturnRoute' in sub_item:
                user.return_route = item[sub_item]
            if 'ReducedTraffic' in sub_item:
                user.reduced_traffic = item[sub_item]
            if 'RouteLocationPreference' in sub_item:
                user.route_location_preference = item[sub_item]
    
def main():
    users = UserProfiles()
    importData(users)

    list = users.getUserList()
    for user_data in list:
        print(user_data)
        print(user_data.user_id)
        print(user_data.elevation_avg)
        print(user_data.elevation_max)
        print(user_data.elevation_min)
        print(user_data.cycle_type)
        print(user_data.cyclist_level)
        print(user_data.time_available)
        print(user_data.prefer_bike_lanes)
        print(user_data.prefer_bike_trials)
        print(user_data.start_location)
        print(user_data.end_location)
        print(user_data.return_route)
        print(user_data.reduced_traffic)
        print(user_data.route_location_preference)
    
    
    
if __name__ == "__main__":
   main()