import json
import pandas
import numpy
import Queue

class User:
    def __init__(self, user_id):
        self.user_id = user_id

class UserProfiles:
    user_list = dict()

    def __init__(self):
        self.queue = Queue.Queue(maxsize=5)
        
    def putQueue(self, item):
        print(self.queue.qsize())
        if self.queue.full():
            print("got here")
            oldest_item = self.queue.get()

            #add oldest_item to route_info
                
            

        self.queue.put(item)

    def addNewUser(self, user, priorities):
        self.user_list[user] = {'priority': priorities}
        
    def addUserRouteInfo(self, user, route_info):
        self.user_list[user]['route_info'] = route_info

    def getUserPriorityList(self):
        return self.user_list
    
    def getUserQueue(self):
        return self.queue

def main():

    users = UserProfiles()
    priority_1234 = ['time consuming', 'bike lanes', 'elevation', 'trip length']
    priority_1111 = ['bike lanes', 'time consuming', 'trip length', 'elevation']
    
    users.addNewUser(1234, priority_1234)
    users.addNewUser(1111, priority_1111)
    
    users_list = users.getUserPriorityList()
    
    X = 12
    Y = 26
    
    route_info_1234 = numpy.random.rand(X, Y)
    print(route_info_1234)

    
            
    users.addUserRouteInfo(1234, route_info_1234)
    
    
    # for item in latest_items_1234:
        # users.putQueue(item)


        
if __name__ == "__main__":
   main()