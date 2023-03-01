
class Home:

    def __init__(self, *args) -> None:
        self.doors: int
        self.windows: int
        self.bedRooms: int
        self.balconies: int
        self.floors: int
        self.hasGuestRoom: bool
        self.hasGarage: bool
        self.hasSwimmingPool: bool

    # builder decorator method  
    def builder(func):
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            return self
        return wrapper

    @builder
    def add_doors(self, doors: int):
        if doors < 1:
            raise "At least 1 door required"
        self.doors = doors
    
    @builder
    def add_floors(self, floors: int):
        self.floors = floors
    
    @builder
    def add_swimming_pool(self):
        self.hasSwimmingPool = True

    @builder
    def add_balconies(self, count: int):
        self.balconies = count
    
    @builder
    def add_bed_rooms(self, count: int):
        self.bedRooms = count
    
    @builder
    def add_guest_room(self):
        self.hasGuestRoom = True 
    
    @builder
    def add_garage(self):
        self.hasGarage = True 

def client():
    home1 = Home()
    home1.add_doors(4) \
        .add_floors(2) \
        .add_swimming_pool() \
        .add_balconies(3)
    print(vars(home1))

    home2 = Home()
    home2.add_balconies(2) \
        .add_swimming_pool() \
        .add_doors(2) \
        .add_floors(2) \
        .add_garage()
    print(vars(home2))

client()


"""
Builders in Python
"""

""" import numpy as np
x = np.arange(-6.2, 6.2, 0.1)

import matplotlib.pyplot as plt
plt.plot(x, np.sin(x))
plt.savefig('sine.png')
plt.gcf().subplots() """
