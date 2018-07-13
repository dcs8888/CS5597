import json
import pandas
import numpy
import queue
from random import randint

class UserProfile:
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

    user_active_recent = user_active.getUserRecent()
    user_active_history = user_active.getUserInfo()
    user_active_priority = user_active.getUserPriority()

    print('Recent List')
    print(user_active_recent)

    print('Historical Data')
    print(user_active_history)
    
    print('Priority')
    print(user_active_priority)

if __name__ == "__main__":
   main()