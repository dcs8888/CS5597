import json
import pandas
import numpy
import queue
from random import randint

NUM_ROUTES = 100

class UserProfile:
    high = 0
    medium = 1
    low = 2
    quick = 0
    average = 1
    very = 2
    short = 0
    medium = 1
    long = 2
    clear = 0
    cloudy = 1
    rain = 2
    storm = 3
    snow = 4
    fog = 5
    windy = 6
    cold = 0
    cool = 1
    mild = 2
    warm = 3
    hot = 4
    morning = 0
    afternoon = 1
    evening = 2
    night = 3
    monday = 0
    tuesday = 1
    wednesday = 3
    thursday = 4
    friday = 5
    saturday = 6
    sunday = 7
    
    def __init__(self):
        self._queue = queue.Queue(maxsize=5)
        self._user_info = dict()
        self._recent = []

    def addNewUser(self, priorities):
        self._user_info['priority'] = priorities

    def addUserRouteInfo(self, matrix, route_info):
        if matrix in self._user_info:
            self._user_info[matrix] = self.getUserInfo()[matrix] + route_info
        else:
            self._user_info[matrix] = route_info
            
    def analyzeRecent(self):
        user = self.getUserRecent()

        print('\n\nActive User Recent List')
        print(user)
        
        
        # matrix set up [row][col]
        # row independent variables - Weather, Temperature, Traffic, Time of Day, Weekday
        # col dependent variables - Elevation, Bike Lanes, Time Consuming (time)
        
        # Analyze Recent data
        for route_data in user:
            for data in route_data:
                print('Data')
                print(str(data) + ': ' + str(route_data[data]))
                
                row, col = numpy.where(route_data[data] == 1)
                result = self.decode_row_col(data, row[0], col[0])
                
                print('Result')
                print(result)


    def decode_row_col(self, matrix, row, col):
        list = dict()
        list[matrix] = ['','']
        
        if 'BikeLanes_Traffic' in matrix:
            if row == self.high:
                list[matrix][0] = 'traffic_high'
            elif row == self.medium:
                list[matrix][0] = 'traffic_medium'
            elif row == self.low:
                list[matrix][0] = 'traffic_low'
            if col == self.high:
                list[matrix][1] = 'bikelanes_high'
            elif col == self.medium:
                list[matrix][1] = 'bikelanes_medium'
            elif col == self.low:
                list[matrix][1] = 'bikelanes_low'

        return list
    
    def getUserInfo(self):
        return self._user_info

    def getUserRecent(self):
        return self._recent
        
    def getUserPriority(self):
        return self._user_info['priority']

    def putQueue(self, item):
        # print('Old Queue size ' + str(self._queue.qsize()))

        if self._queue.full():
            oldest_item = self._queue.get()

            for key, value in oldest_item.items():

                #add oldest_item to route_info
                self.addUserRouteInfo(key, value)
        self._queue.put(item)

        # print('New Queue size ' + str(self._queue.qsize()))

        # Reset recent list
        self._recent = []

        # Store recent trips
        for recent in list(self._queue.queue):
            self._recent.append(recent)
        # print('Recent List')
        # print(self._recent)

def main():

    user_active = UserProfile()
    user_new = UserProfile()

    priority_active = ['time consuming', 'bike lanes', 'elevation']
    priority_new = ['bike lanes', 'elevation', 'time consuming']

    user_active.addNewUser(priority_active)
    user_new.addNewUser(priority_new)

    # Initialize route info matrices
    route_info_active_elevation_weather = numpy.zeros([7,3], dtype=int)
    user_active.addUserRouteInfo('Elevation_Weather', route_info_active_elevation_weather)

    route_info_active_time_weather = numpy.zeros([7,3], dtype=int)
    user_active.addUserRouteInfo('Time_Weather', route_info_active_time_weather)

    route_info_active_time_temp = numpy.zeros([5,3], dtype=int)
    user_active.addUserRouteInfo('Time_Temperature', route_info_active_time_temp)

    route_info_active_elevation_traffic = numpy.zeros([3,3], dtype=int)
    user_active.addUserRouteInfo('Elevation_Traffic', route_info_active_elevation_traffic)

    route_info_active_bikelanes_traffic = numpy.zeros([3,3], dtype=int)
    user_active.addUserRouteInfo('BikeLanes_Traffic', route_info_active_bikelanes_traffic)

    route_info_active_time_timeofday = numpy.zeros([4,3], dtype=int)
    user_active.addUserRouteInfo('Time_TimeOfDay', route_info_active_time_timeofday)

    route_info_active_time_weekday = numpy.zeros([7,3], dtype=int)
    user_active.addUserRouteInfo('Time_Weekday', route_info_active_time_weekday)

    for x in range(0, NUM_ROUTES):
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

        recent_active_info = dict()
        for matrix in matrices:
            num_rows = len(user_active.getUserInfo()[matrix])
            num_cols = len(user_active.getUserInfo()[matrix][0])

            # print('Rows: ' + str(num_rows))
            # print('Cols: ' + str(num_cols))

            recent_active_data = numpy.zeros([num_rows, num_cols], dtype=int)

            # print('Progressive User Info')
            # print(user_active.getUserInfo())
            # print(user_active.getUserInfo)

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

            recent_active_data[y_index][x_index] = 1
            recent_active_info[matrix] = recent_active_data

        user_active.putQueue(recent_active_info)
        
    user_active.analyzeRecent()
    

if __name__ == "__main__":
   main()