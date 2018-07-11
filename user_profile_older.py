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
        
    route_info_1234 =   {'elevation':
                                {'high':
                                        {'weather':
                                            {'clear':10, 'cloudy':12, 'rain':0, 'storm':0, 'snow':0, 'fog':0, 'windy':1},
                                        'traffic':
                                            {'low':5, 'medium':4, 'high':1}},
                                'medium':
                                        {'weather':
                                            {'clear':16, 'cloudy':14, 'rain':0, 'storm':0, 'snow':0, 'fog':0, 'windy':1},
                                        'traffic':
                                            {'low':15, 'medium':12, 'high':22}},
                                'low':
                                        {'weather':
                                            {'clear':25, 'cloudy':17, 'rain':0, 'storm':0, 'snow':0, 'fog':2, 'windy':2},
                                        'traffic':
                                            {'low':22, 'medium':18, 'high':12}}
                                },
                        'bike lanes':      
                                {'high':
                                        {'traffic':
                                            {'low':26, 'medium':15, 'high':5}},
                                'medium':
                                        {'traffic':
                                            {'low':20, 'medium':14, 'high':8}},
                                'low':
                                        {'traffic':
                                            {'low':5, 'medium':8, 'high':3}}
                                },
                        'time consuming':   
                                {'quick':
                                        {'weather':
                                            {'clear':14, 'cloudy':30, 'rain':1, 'storm':0, 'snow':0, 'fog':4, 'windy':3},
                                        'temperature':
                                            {'cold':3, 'cool':5, 'mild':21, 'warm':11, 'hot':4},
                                        'time of day':
                                            {'morning':5, 'afternoon':5, 'evening':39, 'night':2},
                                        'weekday':
                                            {'monday':2, 'tuesday':3, 'wednesday':2, 'thursday':2, 'friday':4, 'saturday':20, 'sunday':18}},
                                'average':
                                        {'weather':
                                            {'clear':12, 'cloudy':15, 'rain':0, 'storm':0, 'snow':0, 'fog':2, 'windy':1},
                                        'temperature':
                                            {'cold':1, 'cool':2, 'mild':21, 'warm':8, 'hot':2},
                                        'time of day':
                                            {'morning':2, 'afternoon':2, 'evening':25, 'night':5},
                                        'weekday':
                                            {'monday':1, 'tuesday':2, 'wednesday':1, 'thursday':2, 'friday':2, 'saturday':11, 'sunday':13}},
                                'very':
                                        {'weather':
                                            {'clear':7, 'cloudy':10, 'rain':0, 'storm':0, 'snow':0, 'fog':0, 'windy':0},
                                        'temperature':
                                            {'cold':0, 'cool':1, 'mild':14, 'warm':7, 'hot':0},
                                        'time of day':
                                            {'morning':0, 'afternoon':0, 'evening':14, 'night':1},
                                        'weekday':
                                            {'monday':1, 'tuesday':0, 'wednesday':0, 'thursday':0, 'friday':1, 'saturday':8, 'sunday':7}}
                                }
                        }

    
            
    users.addUserRouteInfo(1234, route_info_1234)
    
    print(users_list)
    
    latest_items_1 =         {'elevation':
                                        {'low':
                                                {'weather':
                                                    {'clear':1},
                                                'traffic':
                                                    {'low':1}
                                                }
                                        },
                                                
                            'bike lanes':      
                                        {'medium':
                                                {'traffic':
                                                    {'low':1}
                                                }
                                        },
                            'time consuming':   
                                        {'very':
                                                {'weather':
                                                    {'clear':1},
                                                'temperature':
                                                    {'cool':1},
                                                'time of day':
                                                    {'morning':1},
                                                'weekday':
                                                    {'tuesday':1}}
                                        }
                            }
    latest_items_2 =         {'elevation':
                                            {'low':
                                                    {'weather':
                                                        {'cloudy':1},
                                                    'traffic':
                                                        {'high':1}
                                                    }
                                            },
                                                    
                                'bike lanes':      
                                            {'medium':
                                                    {'traffic':
                                                        {'high':1}
                                                    }
                                            },
                                'time consuming':   
                                            {'very':
                                                    {'weather':
                                                        {'cloudy':1},
                                                    'temperature':
                                                        {'cool':1},
                                                    'time of day':
                                                        {'morning':1},
                                                    'weekday':
                                                        {'tuesday':1}}
                                            }
                                }
    latest_items_3 =         {'elevation':
                                            {'low':
                                                    {'weather':
                                                        {'cloudy':1},
                                                    'traffic':
                                                        {'high':1}
                                                    }
                                            },
                                                    
                                'bike lanes':      
                                            {'medium':
                                                    {'traffic':
                                                        {'high':1}
                                                    }
                                            },
                                'time consuming':   
                                            {'very':
                                                    {'weather':
                                                        {'cloudy':1},
                                                    'temperature':
                                                        {'cool':1},
                                                    'time of day':
                                                        {'morning':1},
                                                    'weekday':
                                                        {'tuesday':1}}
                                            }
                                }
    latest_items_4 =         {'elevation':
                                            {'low':
                                                    {'weather':
                                                        {'cloudy':1},
                                                    'traffic':
                                                        {'high':1}
                                                    }
                                            },
                                                    
                                'bike lanes':      
                                            {'medium':
                                                    {'traffic':
                                                        {'high':1}
                                                    }
                                            },
                                'time consuming':   
                                            {'very':
                                                    {'weather':
                                                        {'cloudy':1},
                                                    'temperature':
                                                        {'cool':1},
                                                    'time of day':
                                                        {'morning':1},
                                                    'weekday':
                                                        {'tuesday':1}}
                                            }
                                }
    latest_items_5 =         {'elevation':
                                            {'low':
                                                    {'weather':
                                                        {'cloudy':1},
                                                    'traffic':
                                                        {'high':1}
                                                    }
                                            },
                                                    
                                'bike lanes':      
                                            {'medium':
                                                    {'traffic':
                                                        {'high':1}
                                                    }
                                            },
                                'time consuming':   
                                            {'very':
                                                    {'weather':
                                                        {'cloudy':1},
                                                    'temperature':
                                                        {'cool':1},
                                                    'time of day':
                                                        {'morning':1},
                                                    'weekday':
                                                        {'tuesday':1}}
                                            }
                                }
    latest_items_6 =         {'elevation':
                                            {'medium':
                                                    {'weather':
                                                        {'cloudy':1},
                                                    'traffic':
                                                        {'low':1}
                                                    }
                                            },
                                                    
                                'bike lanes':      
                                            {'medium':
                                                    {'traffic':
                                                        {'low':1}
                                                    }
                                            },
                                'time consuming':   
                                            {'very':
                                                    {'weather':
                                                        {'cloudy':1},
                                                    'temperature':
                                                        {'cool':1},
                                                    'time of day':
                                                        {'morning':1},
                                                    'weekday':
                                                        {'tuesday':1}}
                                            }
                                }
    latest_items_1234 = [latest_items_1, latest_items_2, latest_items_3, latest_items_4, latest_items_5, latest_items_6]
    for item in latest_items_1234:
        users.putQueue(item)
    
    queue = users.getUserQueue()


        
if __name__ == "__main__":
   main()