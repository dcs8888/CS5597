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
    wednesday = 2
    thursday = 3
    friday = 4
    saturday = 5
    sunday = 6
    
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
        recent_dict = dict()
        internal_dict = dict()
        final_dict = dict()

        # matrix set up [row][col]
        # row independent variables - Weather, Temperature, Traffic, Time of Day, Weekday
        # col dependent variables - Elevation, Bike Lanes, Time Consuming (time)
        
        # Analyze Recent data
        recent_num = 1
        for route_data in user:
            data_dict = dict()
            for data in route_data:
                row, col = numpy.where(route_data[data] == 1)
                row_new, col_new = self.decode_row_col(data, row[0], col[0])
                data_dict[data] = [row_new, col_new]
            recent_dict[recent_num] = data_dict
            recent_num += 1

        recent_pandas = pandas.DataFrame(recent_dict)
        
        print(recent_pandas)
        
        bikelanes_traffic = recent_pandas.loc[('BikeLanes_Traffic')]
        elevation_traffic = recent_pandas.loc[('Elevation_Traffic')]
        elevation_weather = recent_pandas.loc[('Elevation_Weather')]
        time_temperature = recent_pandas.loc[('Time_Temperature')]
        time_timeofday = recent_pandas.loc[('Time_TimeOfDay')]
        time_weather = recent_pandas.loc[('Time_Weather')]
        time_weekday = recent_pandas.loc[('Time_Weekday')]
        
        print(bikelanes_traffic)
        print(elevation_traffic)
        print(elevation_weather)
        print(time_temperature)
        print(time_timeofday)
        print(time_weather)
        print(time_weekday)
        
        multiplier_percent = 0.0
        multiplier = 100
        for route in bikelanes_traffic:
            print(bikelanes_traffic.name)
            print(route)
            
            internal_dict[(multiplier - multiplier * multiplier_percent)] = [route[0] , route[1]]
            
            multiplier_percent += 0.200
        final_dict[bikelanes_traffic.name] = internal_dict

        print(internal_dict)
            
            
        

    def decode_row_col(self, matrix, row, col):
        row_translate = ''
        col_translate = ''
        
        if 'BikeLanes_Traffic' in matrix:
            if row == self.high:
                row_translate = 'traffic_high'
            elif row == self.medium:
                row_translate = 'traffic_medium'
            elif row == self.low:
                row_translate = 'traffic_low'
            if col == self.high:
                col_translate = 'bikelanes_high'
            elif col == self.medium:
                col_translate = 'bikelanes_medium'
            elif col == self.low:
                col_translate = 'bikelanes_low'
        elif 'Time_Temperature' in matrix:
            if row == self.cold:
                row_translate = 'temperature_cold'
            elif row == self.cool:
                row_translate = 'temperature_cool'
            elif row == self.mild:
                row_translate = 'temperature_mild'
            elif row == self.warm:
                row_translate = 'temperature_warm'
            elif row == self.hot:
                row_translate = 'temperature_hot'
            if col == self.quick:
                col_translate = 'time_quick'
            elif col == self.average:
                col_translate = 'time_average'
            elif col == self.very:
                col_translate = 'time_very'
        elif 'Time_Weather' in matrix:
            if row == self.clear:
                row_translate = 'weather_clear'
            elif row == self.cloudy:
                row_translate = 'weather_cloudy'
            elif row == self.rain:
                row_translate = 'weather_rain'
            elif row == self.storm:
                row_translate = 'weather_storm'
            elif row == self.snow:
                row_translate = 'weather_snow'
            elif row == self.fog:
                row_translate = 'weather_fog'
            elif row == self.windy:
                row_translate = 'weather_windy'
            if col == self.quick:
                col_translate = 'time_quick'
            elif col == self.average:
                col_translate = 'time_average'
            elif col == self.very:
                col_translate = 'time_very'
        elif 'Time_Weekday' in matrix:
            if row == self.monday:
                row_translate = 'weekday_monday'
            elif row == self.tuesday:
                row_translate = 'weekday_tuesday'
            elif row == self.wednesday:
                row_translate = 'weekday_wednesday'
            elif row == self.thursday:
                row_translate = 'weekday_thursday'
            elif row == self.friday:
                row_translate = 'weekday_friday'
            elif row == self.saturday:
                row_translate = 'weekday_saturday'
            elif row == self.sunday:
                row_translate = 'weekday_sunday'
            if col == self.quick:
                col_translate = 'time_quick'
            elif col == self.average:
                col_translate = 'time_average'
            elif col == self.very:
                col_translate = 'time_very'
        elif 'Time_TimeOfDay' in matrix:
            if row == self.morning:
                row_translate = 'timeofday_morning'
            elif row == self.afternoon:
                row_translate = 'timeofday_afternoon'
            elif row == self.evening:
                row_translate = 'timeofday_evening'
            elif row == self.night:
                row_translate = 'timeofday_night'
            if col == self.quick:
                col_translate = 'time_quick'
            elif col == self.average:
                col_translate = 'time_average'
            elif col == self.very:
                col_translate = 'time_very'
        elif 'Elevation_Traffic' in matrix:
            if row == self.high:
                row_translate = 'traffic_high'
            elif row == self.medium:
                row_translate = 'traffic_medium'
            elif row == self.low:
                row_translate = 'traffic_low'
            if col == self.high:
                col_translate = 'elevation_high'
            elif col == self.medium:
                col_translate = 'elevation_medium'
            elif col == self.low:
                col_translate = 'elevation_low'
        elif 'Elevation_Weather' in matrix:
            if row == self.clear:
                row_translate = 'weather_clear'
            elif row == self.cloudy:
                row_translate = 'weather_cloudy'
            elif row == self.rain:
                row_translate = 'weather_rain'
            elif row == self.storm:
                row_translate = 'weather_storm'
            elif row == self.snow:
                row_translate = 'weather_snow'
            elif row == self.fog:
                row_translate = 'weather_fog'
            elif row == self.windy:
                row_translate = 'weather_windy'
            if col == self.high:
                col_translate = 'elevation_high'
            elif col == self.medium:
                col_translate = 'elevation_medium'
            elif col == self.low:
                col_translate = 'elevation_low'

        return row_translate, col_translate
    
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