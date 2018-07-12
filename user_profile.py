import json
import pandas
import numpy
import queue
from random import randint

class UserProfile:
    def __init__(self, ):
        self.queue = queue.Queue(maxsize=5)
        self.user_info = dict()

    def addNewUser(self, priorities):
        self.user_info['priority'] = priorities
        
    def addUserRouteInfo(self, matrix, route_info):
        self.user_info[matrix] = route_info

    def getUserInfo(self):
        return self.user_info
    
    def getUserQueue(self):
        return self.queue
    
    def putQueue(self, item):
        print(self.queue.qsize())
        if self.queue.full():
            print("got here")
            oldest_item = self.queue.get()

            #add oldest_item to route_info

        self.queue.put(item)

def main():

    user_1234 = UserProfile()
    
    priority_1234 = ['time consuming', 'bike lanes', 'elevation', 'trip length']
    
    user_1234.addNewUser(priority_1234)
    
    # Initialize route info matrices
    route_info_1234_elevation_weather = [[0 for i in range(3)] for j in range(7)]
    user_1234.addUserRouteInfo('Elevation_Weather', route_info_1234_elevation_weather)
    
    route_info_1234_time_weather = [[0 for i in range(3)] for j in range(7)]
    user_1234.addUserRouteInfo('Time_Weather', route_info_1234_time_weather)
    
    route_info_1234_time_temp = [[0 for i in range(3)] for j in range(5)]
    user_1234.addUserRouteInfo('Time_Temperature', route_info_1234_time_temp)
    
    route_info_1234_elevation_traffic = [[0 for i in range(3)] for j in range(3)]
    user_1234.addUserRouteInfo('Elevation_Traffic', route_info_1234_elevation_traffic)
    
    route_info_1234_bikelanes_traffic = [[0 for i in range(3)] for j in range(3)]
    user_1234.addUserRouteInfo('BikeLanes_Traffic', route_info_1234_bikelanes_traffic)
    
    route_info_1234_time_timeofday = [[0 for i in range(3)] for j in range(4)]
    user_1234.addUserRouteInfo('Time_TimeOfDay', route_info_1234_time_timeofday)

    route_info_1234_time_weekday = [[0 for i in range(3)] for j in range(7)]
    user_1234.addUserRouteInfo('Time_Weekday', route_info_1234_time_weekday)
    
    user_1234_info = user_1234.getUserInfo()
    
    for x in range(1, 100):
        
        matrices = ['Elevation_Weather', 'Time_Weather', 'Time_Temperature', 'Elevation_Traffic', 'BikeLanes_Traffic', 'Time_TimeOfDay', 'Time_Weekday']
        
        x_index = 0
        y_index = 0
        
        # X Axis variables
        elevation_index = randint(0,2)
        bikelanes_index = randint(0,2)
        time_index = randint(0,2)
        
        # Y Axis variables
        weather_index = randint(0,6)
        temp_index = randint(0,4)
        traffic_index = randint(0,2)
        timeofday_index = randint(0,3)
        weekday_index = randint(0,6)
        
        for matrix in matrices:
            if 'Elevation' in matrix:
                x_index = elevation_index
            if 'BikeLanes' in matrix:
                x_index = bikelanes_index
            if 'Time_' in matrix:
                x_index = time_index
            if 'Weather' in matrix:
                y_index = weather_index
            if 'Temperature' in matrix:
                y_index = temp_index
            if 'Traffic' in matrix:
                y_index = traffic_index
            if 'TimeOfDay' in matrix:
                y_index = timeofday_index
            if 'Weekday' in matrix:
                y_index = weekday_index

            print(matrix)
            print(x_index)
            print(y_index)
            
            print(user_1234_info[matrix])
            
            user_1234_info[matrix][y_index][x_index] = 1
            
            print(user_1234_info[matrix])
                
            # user_1234_info.putQueue(
                
   

        
if __name__ == "__main__":
   main()