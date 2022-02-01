
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
            self.location = x0 + (dx // abs(dx)), y0
        elif dy != 0:
            self.location = x0, y0 + (dy // abs(dy))

    def can_finish(self, ride, time_step):
        distance_to_start = self.manhatten(self.location, ride.start)
        total_distance = distance_to_start + ride.distance

        return time_step + total_distance <= ride.latest_finish