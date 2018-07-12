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

    user_1234 = UserProfile()

    priority_1234 = ['time consuming', 'bike lanes', 'elevation', 'trip length']

    user_1234.addNewUser(priority_1234)

    # Initialize route info matrices
    route_info_1234_elevation_weather = numpy.zeros([7,3], dtype=int)
    user_1234.addUserRouteInfo('Elevation_Weather', route_info_1234_elevation_weather)

    route_info_1234_time_weather = numpy.zeros([7,3], dtype=int)
    user_1234.addUserRouteInfo('Time_Weather', route_info_1234_time_weather)

    route_info_1234_time_temp = numpy.zeros([5,3], dtype=int)
    user_1234.addUserRouteInfo('Time_Temperature', route_info_1234_time_temp)

    route_info_1234_elevation_traffic = numpy.zeros([3,3], dtype=int)
    user_1234.addUserRouteInfo('Elevation_Traffic', route_info_1234_elevation_traffic)

    route_info_1234_bikelanes_traffic = numpy.zeros([3,3], dtype=int)
    user_1234.addUserRouteInfo('BikeLanes_Traffic', route_info_1234_bikelanes_traffic)

    route_info_1234_time_timeofday = numpy.zeros([4,3], dtype=int)
    user_1234.addUserRouteInfo('Time_TimeOfDay', route_info_1234_time_timeofday)

    route_info_1234_time_weekday = numpy.zeros([7,3], dtype=int)
    user_1234.addUserRouteInfo('Time_Weekday', route_info_1234_time_weekday)

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

        recent_1234_info = dict()
        for matrix in matrices:
            num_rows = len(user_1234.getUserInfo()[matrix])
            num_cols = len(user_1234.getUserInfo()[matrix][0])

            # print('Rows: ' + str(num_rows))
            # print('Cols: ' + str(num_cols))

            recent_1234_data = numpy.zeros([num_rows, num_cols], dtype=int)

            # print('Progressive User Info')
            # print(user_1234.getUserInfo())
            # print(user_1234.getUserInfo)

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

            recent_1234_data[y_index][x_index] = 1
            recent_1234_info[matrix] = recent_1234_data

        user_1234.putQueue(recent_1234_info)

    user_1234_recent = user_1234.getUserRecent()
    user_1234_history = user_1234.getUserInfo()

    print('Recent List')
    print(user_1234_recent)

    print('Historical Data')
    print(user_1234_history)

if __name__ == "__main__":
   main()