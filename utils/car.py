
class Car:
    def __init__(self, id):
        self.id = id
        self.location = (0, 0)

        self.ride = None
        self.is_riding = False

    def add_ride(self, ride):
        self.ride = ride

    def remove_ride(self):
        self.ride = None

    def step(self):
        if not self.ride:
            return
        
        if self.is_riding:
            self.__step_to(self.ride.end)
        else:
            self.__step_to(self.ride.start)

    def __step_to(self, coord):
        (x0, y0), (x1, y1) = self.location, coord
        dx, dy = x1 - x0, y1 - y0

        if dx != 0:
